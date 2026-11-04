from fastapi import FastAPI, Request
from pydantic import BaseModel
import torch
import re

from transformers import T5ForConditionalGeneration, T5Tokenizer
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Text Summarizer App",
    description="Text Summarization using T5",
    version="1.0"
)

templates = Jinja2Templates(directory="templates")

model_path = "varsha100704/Text-summarization-t5"

model = T5ForConditionalGeneration.from_pretrained(model_path)
tokenizer = T5Tokenizer.from_pretrained(model_path)


# Device
if torch.backends.mps.is_available():
    device = torch.device("mps")
elif torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

print("Using device:", device)

model = model.to(device)
model.eval()


class DialogueInput(BaseModel):
    dialogue: str


def clean_data(text):
    text = re.sub(r"\r\n|\r|\n", " ", text)  # lines
    text = re.sub(r"\s+", " ", text)         # spaces
    text = re.sub(r"<.*?>", " ", text)       # HTML tags
    text = text.strip().lower()

    return text


def summarize_dialogue(dialogue: str) -> str:

    dialogue = clean_data(dialogue)

    # Tokenization
    inputs = tokenizer(
        dialogue,
        padding="max_length",
        max_length=512,
        truncation=True,
        return_tensors="pt"
    ).to(device)

    # Generate summary
    with torch.no_grad():
        targets = model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=150,
            num_beams=4,
            early_stopping=True
        )

    # Decode output
    summary = tokenizer.decode(
        targets[0],
        skip_special_tokens=True
    )

    return summary


# API endpoints
@app.post("/summarize/")
async def summarize(dialogue_input: DialogueInput):

    if not dialogue_input.dialogue.strip():
        return {"error": "Please enter some dialogue."}

    summary = summarize_dialogue(dialogue_input.dialogue)

    return {"summary": summary}


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

