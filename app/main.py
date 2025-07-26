# app/main.py
import os
import json
from utils import extract_headings

INPUT_DIR = "app/input"
OUTPUT_DIR = "app/output"

def process_all_pdfs():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for file in os.listdir(INPUT_DIR):
        if file.lower().endswith(".pdf"):
            input_path = os.path.join(INPUT_DIR, file)
            output_path = os.path.join(OUTPUT_DIR, file.replace(".pdf", ".json"))

            title, outline = extract_headings(input_path)
            result = {
                "title": title,
                "outline": outline
            }

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)

            print(f"Processed: {file}")

if __name__ == "__main__":
    process_all_pdfs()
