from pypdf import PdfReader
import sys


def extract_text(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text


def summarize(text, max_words=150):
    words = text.split()

    if len(words) <= max_words:
        return text

    return " ".join(words[:max_words]) + "..."


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <pdf_file>")
        return

    pdf_file = sys.argv[1]

    text = extract_text(pdf_file)

    summary = summarize(text)

    print("\nSummary:\n")
    print(summary)


if __name__ == "__main__":
    main()
