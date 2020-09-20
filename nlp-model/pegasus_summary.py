from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch
import time

with open("sample.txt") as f:
    sample_text = f.read()

model_load_start = time.time()

model_name = "google/pegasus-cnn_dailynews"
tokenizer = PegasusTokenizer.from_pretrained(model_name)

model = PegasusForConditionalGeneration.from_pretrained(model_name)
print(f"Model loaded in {round(time.time() - model_load_start, 2)}s")

summarize_start = time.time()

tokens = tokenizer.encode(sample_text, truncation=True)

summarized = model.generate(
    input_ids=torch.LongTensor([tokens]),
    attention_mask=torch.IntTensor([[1] * len(tokens)]),
    min_length=100,
    max_length=250,
    num_beams=3,
    early_stopping=True,
    length_penalty=1.0,
)[0]

summarized = tokenizer.decode(summarized, skip_special_tokens=True)
reduction = 1 - len(summarized) / len(sample_text)
print(
    f"---------------------------------Summarization took {round(time.time() - summarize_start, 2)}s at {round(reduction, 4) * 100}% reduction---------------------------------"
)
print(summarized)