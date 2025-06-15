#Biblitheken + Zugriff auf LLM und effizinter Ablauf auf GPU/CPU
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

#Modell wird festgelegt: 'Gemma 2b'
MODEL_NAME = "google/gemma-2b"

#Passender Tokenizer + Tokenizer wandelt Text in zahlen um. 
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

#Das Modell wird geladen + durch 'torch_dtype=torch.float16' weniger Speicherverbrauch und durch 'device_map="auto"' entscheidet Huggingface ob GPU oder CPU verwendet wird. 
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16,
    device_map="auto"
)

#Antwortgeneriereung durch das LLM + Eingabetext in Token umwandeln und wieder rückgängig, sowie Prompt entfernen (falls enthalten).
def generiere_antwort(prompt: str) -> str:
    
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=100,
            do_sample=True,
            top_p=0.9,
            temperature=0.7
        )
    
    antwort = tokenizer.decode(output[0], skip_special_tokens=True)

    if antwort.startswith(prompt):
        antwort = antwort[len(prompt):].strip()

    return antwort
