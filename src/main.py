import os
from extract_text import extract_text_from_pdf
from extract_features import extract_features
from compare_invoices import calculate_similarity

def main():
    print("Starting the main function...")

    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Set the data directory path relative to the script directory
    data_dir = os.path.join(script_dir, '..', 'data')

    if not os.path.exists(data_dir):
        print(f"Error: Directory {data_dir} does not exist.")
        return

    pdf_files = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith('.pdf')]

    if not pdf_files:
        print(f"No PDF files found in directory {data_dir}.")
        return

    invoices = []
    for pdf_file in pdf_files:
        text = extract_text_from_pdf(pdf_file)
        features = extract_features(text)
        invoices.append({
            'file': pdf_file,
            'text': text,
            'features': features
        })

    new_invoice_file = os.path.join(data_dir, 'invoice_102857.pdf')
    if not os.path.exists(new_invoice_file):
        print(f"Error: New invoice file {new_invoice_file} does not exist.")
        return

    new_invoice_text = extract_text_from_pdf(new_invoice_file)
    most_similar_invoice, similarity_score = find_most_similar_invoice(new_invoice_text, invoices)

    print(f"The most similar invoice to {new_invoice_file} is {most_similar_invoice} with a similarity score of {similarity_score}")

def find_most_similar_invoice(new_invoice_text, invoices):
    similarities = [(invoice['file'], calculate_similarity(new_invoice_text, invoice['text'])) for invoice in invoices]
    most_similar = max(similarities, key=lambda item: item[1])
    return most_similar

if __name__ == "__main__":
    main()
