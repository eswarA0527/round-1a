# app/utils.py
import pdfplumber
from collections import defaultdict

def extract_headings(pdf_path):
    headings = []
    font_size_counts = defaultdict(int)
    lines_data = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            words = page.extract_words(extra_attrs=["size", "fontname"])
            if not words:
                continue

            # Group words by line (by 'top' position)
            lines = defaultdict(list)
            for word in words:
                top = round(word['top'], 1)
                lines[top].append(word)

            for top, line_words in lines.items():
                text = " ".join(w['text'] for w in sorted(line_words, key=lambda x: x['x0'])).strip()
                if not text:
                    continue

                max_size = max(w['size'] for w in line_words)
                font_size_counts[max_size] += 1
                lines_data.append({
                    "text": text,
                    "font_size": max_size,
                    "page": page_num
                })

    # Determine heading sizes (top 2-3 largest font sizes used in the document)
    sorted_font_sizes = sorted(font_size_counts.items(), key=lambda x: (-x[0], -x[1]))
    top_sizes = [fs[0] for fs in sorted_font_sizes[:3]]
    size_to_level = {}
    if len(top_sizes) > 0: size_to_level[top_sizes[0]] = "H1"
    if len(top_sizes) > 1: size_to_level[top_sizes[1]] = "H2"
    if len(top_sizes) > 2: size_to_level[top_sizes[2]] = "H3"

    # Filter headings
    for line in lines_data:
        level = size_to_level.get(line['font_size'])
        if level:
            headings.append({
                "level": level,
                "text": line['text'],
                "page": line['page']
            })

    title = headings[0]['text'] if headings else "Untitled"
    return title, headings
