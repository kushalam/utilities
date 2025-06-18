# data_from_image.py
# This script reads data from an image using OCR and saves it to a CSV file.

import pytesseract
from PIL import Image
import csv
import sys

# Usage: python data_from_image.py <input_image> <output_csv>
def main():
    if len(sys.argv) != 3:
        print("Usage: python data_from_image.py <input_image> <output_csv>")
        sys.exit(1)
    input_image = sys.argv[1]
    output_csv = sys.argv[2]

    # Load image
    image = Image.open(input_image)

    # Extract text using pytesseract
    text = pytesseract.image_to_string(image)

    # Split text into lines
    lines = text.strip().split('\n')

    # Write lines to CSV
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for line in lines:
            # Split line into columns by whitespace (customize as needed)
            writer.writerow(line.split())
    print(f"Extracted data saved to {output_csv}")

if __name__ == "__main__":
    main()
