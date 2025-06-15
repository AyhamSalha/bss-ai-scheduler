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
