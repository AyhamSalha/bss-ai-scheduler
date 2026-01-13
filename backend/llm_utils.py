"""LLM utilities for natural language processing."""
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from colorama import Fore, Style
import warnings
import logging
from backend.command_parser import parse_scheduling_command

logger = logging.getLogger(__name__)

MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# Device configuration - uses GPU if available, otherwise CPU
device = "cuda" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if device == "cuda" else torch.float32

if device == "cpu":
    warnings.warn(Fore.YELLOW + "[WARNING] No GPU detected – TinyLlama will run slower." + Style.RESET_ALL)
    logger.warning("Running on CPU - performance may be degraded")

# Load model and tokenizer
logger.info(f"Loading model {MODEL_NAME}...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch_dtype,
    device_map="auto"
)
logger.info("Model loaded successfully")

# Chat history storage
chat_history = []

# Response parameters
MAX_TOKENS = 80
TOP_P = 0.92
TEMPERATURE = 0.65
MAX_HISTORY = 4  

def generate_response(prompt: str) -> dict:
    """
    Generate a response based on input and history, or process recognized scheduling commands directly.
    
    Args:
        prompt: User input text
        
    Returns:
        Dictionary with response and optional calendar entry
    """
    # Recognize scheduling command
    command = parse_scheduling_command(prompt)
    entry = None

    if command:
        entry = {
            "title": "Scheduled (via AI)",
            "datum": command["datum"],
            "uhrzeit": "09:00–17:00",
            "mitarbeiter": command["mitarbeiter"],
            "verfuegbar": "Yes"
        }

        response = f"{command['mitarbeiter']} has been scheduled for {command['datum']}."
        logger.info(f"Scheduled: {command['mitarbeiter']} on {command['datum']}")
        return {
            "response": response,
            "eintrag": entry
        }

    # Generate standard LLM response
    # For non-scheduling queries, provide a quick rule-based response
    # to avoid slow CPU processing
    if device == "cpu":
        response = "I'm your scheduling assistant. Try commands like 'Schedule John for Monday' or 'Add Sarah to Friday's shift'."
        return {"response": response}
    
    system_prompt = (
        "<|system|>You are a precise, helpful AI assistant. "
        "Use clear language and respond professionally, politely and logically.<|end|>\n"
    )

    # Build context dialogue
    chat_prompt = system_prompt
    for history_entry in chat_history[-MAX_HISTORY:]:
        question = history_entry['question'].strip().replace("\n", " ")
        answer = history_entry['answer'].strip().replace("\n", " ")
        chat_prompt += f"<|user|>{question}<|end|>\n<|assistant|>{answer}<|end|>\n"

    # Insert new input
    prompt = prompt.strip().replace("\n", " ")
    chat_prompt += f"<|user|>{prompt}<|end|>\n<|assistant|>"

    # Tokenization and generation
    inputs = tokenizer(chat_prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=MAX_TOKENS,
            do_sample=True,
            top_p=TOP_P,
            temperature=TEMPERATURE,
            pad_token_id=tokenizer.eos_token_id
        )

    # Process output
    answer = tokenizer.decode(output[0], skip_special_tokens=True).strip()
    if "<|assistant|>" in answer:
        answer = answer.split("<|assistant|>")[-1].strip()

    # Update history
    chat_history.append({"question": prompt, "answer": answer})
    logger.debug(f"Generated response: {answer[:50]}...")

    return {
        "response": answer,
        "eintrag": None
    }


# Keep old function name for backward compatibility
generiere_antwort = generate_response
