from pypdf import PdfReader


def extract_text(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text


def combine_documents(pdf_files):
    combined_text = ""

    for pdf in pdf_files:
        combined_text += extract_text(pdf)
        combined_text += "\n\n"

    return combined_text


def summarize(text, max_words=250):
    words = text.split()

    if len(words) <= max_words:
        return text

    return " ".join(words[:max_words]) + "..."
