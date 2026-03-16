from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = r"C:/Users/hp/Desktop/5th_minor_project_1/Project-2/models/models--facebook--bart-large-cnn/snapshots/37f520fa929c961707657b28798b30c003dd100b"

tokenizer = AutoTokenizer.from_pretrained(model_name, local_files_only=True)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name, local_files_only=True)

print("✅ Model loaded successfully from local path!")

