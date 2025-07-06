from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from colorama import Fore, Style
import warnings

MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

#Geräteeinstellung – nutzt GPU wenn verfügbar, sonst CPU
device = "cuda" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if device == "cuda" else torch.float32

if device == "cpu":
    warnings.warn(Fore.YELLOW + "[WARNUNG] Keine GPU – TinyLlama läuft langsamer." + Style.RESET_ALL)

#Modell + Tokenizer laden (Mit dem Tokenizer wird Text in Zahlen überstezt)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch_dtype,
    device_map="auto"
)

#Chatverlauf wird gespeichert 
chat_history = []

#Antwortparameter
MAX_TOKENS = 80
TOP_P = 0.92
TEMPERATURE = 0.65
MAX_HISTORY = 4  

def generiere_antwort(prompt: str) -> str:
    """
    Generiert eine Antwort basierend auf Eingabe und Verlauf im TinyLlama-Stil.
    """
    #Systemrolle, damit beeinflussen wir das Systemverhalten
    system_prompt = (
        "<|system|>Du bist ein präziser, hilfreicher, deutscher KI-Assistent. "
        "Verwende klare Sprache und antworte professionell, höflich und logisch.<|end|>\n"
    )

    #Kontext-Dialog aufbauen
    chat_prompt = system_prompt
    for eintrag in chat_history[-MAX_HISTORY:]:
        frage = eintrag['frage'].strip().replace("\n", " ")
        antwort = eintrag['antwort'].strip().replace("\n", " ")
        chat_prompt += f"<|user|>{frage}<|end|>\n<|assistant|>{antwort}<|end|>\n"

    #Neue Nutzereingabe
    prompt = prompt.strip().replace("\n", " ")
    chat_prompt += f"<|user|>{prompt}<|end|>\n<|assistant|>"

    #Tokenisierung + Generierung
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

    #Ausgabe verarbeiten
    antwort = tokenizer.decode(output[0], skip_special_tokens=True).strip()

    #Nur den letzten Assistant-Teil extrahieren
    if "<|assistant|>" in antwort:
        antwort = antwort.split("<|assistant|>")[-1].strip()

    #Verlauf aktualisieren
    chat_history.append({"frage": prompt, "antwort": antwort})

    return antwort
