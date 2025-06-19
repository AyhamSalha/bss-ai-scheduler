#Bibliotheken + Zugriff auf LLM und effizienter Ablauf auf GPU/CPU
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os
from dotenv import load_dotenv

#.env-Datei laden
load_dotenv()

#HuggingFace Token aus .env lesen
HF_TOKEN = os.getenv("HF_TOKEN")

#Modellname: Leichtere Version wegen Hardware
MODEL_NAME = "google/gemma-2b-it"

#Tokenizer laden
tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME,
    token=HF_TOKEN
)

#Modell laden – direkt (kein Offloading)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    token=HF_TOKEN,
    torch_dtype=torch.float16,
    device_map="auto" 
)

#Funktion zur Antwortgenerierung
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
