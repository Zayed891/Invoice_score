from extract_text import extract_text_from_pdf
from extract_features import extract_features
from compare_invoices import calculate_similarity
import os

def main():
    print("Starting the main function...")
data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
pdf_files = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith('.pdf')]
print(f"PDF files found: {pdf_files}")

invoices = []
for pdf_file in pdf_files:
    text = extract_text_from_pdf(pdf_file)
    print(f"Extracted text from {pdf_file}")
    features = extract_features(text)
    print(f"Extracted features: {features}")
    invoices.append({
        'file': pdf_file,
        'text': text,
        'features': features
    })

def find_most_similar_invoice(new_invoice_text, new_invoice_file, invoices):
    similarities = [
        (invoice['file'], calculate_similarity(new_invoice_text, invoice['text']))
        for invoice in invoices if invoice['file'] != new_invoice_file
    ]
    print(f"Similarities calculated: {similarities}")
    most_similar = max(similarities, key=lambda item: item[1])
    return most_similar

new_invoice_file = os.path.join(data_dir, 'invoice_77073.pdf')  # Change this to your test file
new_invoice_text = extract_text_from_pdf(new_invoice_file)
print(f"Extracted text from new invoice: {new_invoice_text}")
most_similar_invoice, similarity_score = find_most_similar_invoice(new_invoice_text, new_invoice_file, invoices)

print(f"The most similar invoice to {new_invoice_file} is {most_similar_invoice} with a similarity score of {similarity_score}")

if __name__ == "__main__":
    main()
