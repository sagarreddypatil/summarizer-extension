from transformers import T5ForConditionalGeneration, T5Tokenizer
import time

with open("sample.txt") as f:
    sample_text = f.read()

model_load_start = time.time()

model = T5ForConditionalGeneration.from_pretrained("t5-small")
tokenizer = T5Tokenizer.from_pretrained("t5-small")

print(f"Model loaded in {round(time.time() - model_load_start, 2)}s")

inputs = tokenizer.encode(
    "summarize: " + sample_text, return_tensors="pt", max_length=512
)

summarize_start = time.time()
outputs = model.generate(
    inputs,
    max_length=250,
    min_length=100,
    length_penalty=1.0,
    num_beams=3,
    early_stopping=True,
)
output_text = tokenizer.decode(outputs[0].tolist())
reduction = 1 - len(output_text) / len(sample_text)
print(
    f"---------------------------------Summarization took {round(time.time() - summarize_start, 2)}s at {round(reduction, 4) * 100}% reduction---------------------------------"
)
print(output_text)
