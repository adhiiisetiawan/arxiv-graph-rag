import os
import re
import PyPDF2
import unicodedata

def convert_arxiv_papers_to_txt(folder_path, output_folder):
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            txt_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".txt")

            with open(pdf_path, "rb") as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                text = ""
                for page in pdf_reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        # Normalize text to remove undefined characters
                        page_text = unicodedata.normalize('NFKD', page_text)
                        # Filter out non-text characters
                        page_text = re.sub(r'[^a-zA-Z0-9\s.,;:!?\'"-]', '', page_text)
                        text += page_text

            with open(txt_path, "w") as txt_file:
                txt_file.write(text)

            print(f"Converted {pdf_path} to {txt_path}")

# Usage example
folder_path = "arxiv_papers"
output_folder = "vlm_papers_txt"
os.makedirs(output_folder, exist_ok=True)
convert_arxiv_papers_to_txt(folder_path, output_folder)