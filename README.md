# Invoice Similarity Matching

## Overview

This project develops a system to identify and match similar invoices based on their content and structure.

## File Structure

- `data/`: Directory containing PDF invoices.
- `src/`: Directory containing the source code.
  - `extract_text.py`: Script to extract text from PDF invoices.
  - `extract_features.py`: Script to extract features from the text.
  - `compare_invoices.py`: Script to calculate the similarity between invoices.
  - `main.py`: Main script to run the comparison.
- `README.md`: This file.
- `requirements.txt`: List of required Python packages.

## Installation

1. Create a virtual environment (optional):
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Place the PDF invoices you want to compare in the `data/` directory.
2. Run the main script to find the most similar invoice:
    ```sh
    python src/main.py
    ```
3. The script will output the most similar invoice and the similarity score.
