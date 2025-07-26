# 📘 PDF Outline Extractor – Round 1A Hackathon

This tool extracts a **structured outline** from PDF files using `pdfplumber`. The output includes the **document title** and **main headings (H1, H2, H3)** in a machine-readable JSON format.

---

## 📁 Project Structure

```
project_root/
├── app/
│   ├── main.py        # Entry point
│   └── utils.py       # Helper logic for heading extraction
├── input/             # Place PDFs here
├── output/            # Extracted outline JSONs saved here
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 🚀 How to Run (Without Docker)

### 1. Setup Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# OR
source venv/bin/activate  # macOS/Linux
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add PDF

Place your PDF file (e.g., `sample.pdf`) in the `input/` folder.

### 4. Run the Script

```bash
python app/main.py
```

The result will be saved to `output/sample.json`.

---

## 🐳 Run with Docker

### 1. Build Docker Image

```bash
docker build -t pdf-outline-extractor .
```

### 2. Run Docker Container

```bash
docker run --rm -v %cd%/input:/app/input -v %cd%/output:/app/output pdf-outline-extractor
```

> Replace `%cd%` with `${PWD}` if you're on macOS/Linux.

---

## ✅ Output Format

```json
{
  "title": "Sample PDF Title",
  "outline": [
    {
      "level": "H1",
      "text": "Introduction",
      "page": 0
    },
    {
      "level": "H2",
      "text": "Background",
      "page": 1
    }
  ]
}
```

---

## 📦 Dependencies

- Python 3.8–3.11
- `pdfplumber==0.10.3`
- `pdfminer.six==20221105`

---

## 🛠 Troubleshooting

- ❗**ModuleNotFoundError**: Run `pip install -r requirements.txt`
- ❗**input folder not found**: Make sure `input/` exists and has your `.pdf`
- ❗**ExecutionPolicy error**: Use `activate.bat` instead of PowerShell to activate venv on Windows.

---

## 🧠 Purpose

Built for **Adobe India Hackathon Round 1A** – to automatically detect document structure and key headings from scanned or digital PDFs.

---
