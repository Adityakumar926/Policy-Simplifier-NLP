from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

cache_dir = "./models"  # This will create a folder called models in same location

# Download and save the model + tokenizer
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn", cache_dir=cache_dir)
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn", cache_dir=cache_dir)

print("✅ Model downloaded and saved to ./models")

