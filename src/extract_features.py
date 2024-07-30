import re

def extract_features(text):
    features = {}
    
    invoice_number_match = re.search(r'(?i)rechnung\s+Nr\.\s+(\d+)', text)
    if invoice_number_match:
        features['invoice_number'] = invoice_number_match.group(1)
    else:
        features['invoice_number'] = None  # or handle this case as needed

    # Add more features extraction here as needed

    return features
