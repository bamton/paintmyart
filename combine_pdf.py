#!/usr/bin/env python3
"""
Combine all Winter Survival Kit pages into a single PDF.
Includes all 63 PNG pages plus 3 Word Search PDFs.
"""

import os
import sys
from PIL import Image
from PyPDF2 import PdfReader, PdfWriter
import io

def add_image_to_pdf(pdf_writer, image_path, x=0, y=0):
    """Add an image to a new page in the PDF"""
    try:
        img = Image.open(image_path)
        # Convert image to RGB if it's not
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Get image dimensions
        img_width, img_height = img.size

        # Create a new page
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import letter

        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)

        # Calculate dimensions to fit the page
        page_width, page_height = letter
        scale = min(page_width / img_width, page_height / img_height) * 0.95

        new_width = img_width * scale
        new_height = img_height * scale

        # Center the image
        x = (page_width - new_width) / 2
        y = (page_height - new_height) / 2

        can.drawImage(image_path, x, y, new_width, new_height)
        can.save()

        # Move to the beginning of the StringIO buffer
        packet.seek(0)
        new_page = PdfReader(packet)
        pdf_writer.add_page(new_page.pages[0])

        return True
    except Exception as e:
        print(f"Error adding {image_path}: {e}")
        return False

def main():
    # Define the folders in order
    folders = [
        ("01-Christmas-Winter", 8),
        ("02-Winter-Remix", 8),
        ("03-Winter-Activities", 5),
        ("04-Dinosaurs", 8),
        ("05-Unicorns-Dragons", 6),
        ("06-Animals", 8),
        ("07-Princess-Pirates", 6),
        ("08-Vehicles", 5),
        ("09-Space", 4),
        ("10-Easy-Wins", 5)
    ]

    base_path = "winter-survival-kit"
    output_pdf = os.path.join(base_path, "FULL-KIT-ALL-PAGES.pdf")

    # Create a PDF writer
    pdf_writer = PdfWriter()

    # Track the current page number
    current_page = 1

    print("Adding PNG pages...")

    # Add all PNG pages in order
    for folder_name, count in folders:
        folder_path = os.path.join(base_path, folder_name)
        for i in range(1, count + 1):
            # Calculate the global page number
            if folder_name == "01-Christmas-Winter":
                page_num = i
            elif folder_name == "02-Winter-Remix":
                page_num = 8 + i
            elif folder_name == "03-Winter-Activities":
                page_num = 16 + i
            elif folder_name == "04-Dinosaurs":
                page_num = 21 + i
            elif folder_name == "05-Unicorns-Dragons":
                page_num = 29 + i
            elif folder_name == "06-Animals":
                page_num = 35 + i
            elif folder_name == "07-Princess-Pirates":
                page_num = 43 + i
            elif folder_name == "08-Vehicles":
                page_num = 49 + i
            elif folder_name == "09-Space":
                page_num = 54 + i
            elif folder_name == "10-Easy-Wins":
                page_num = 58 + i

            filename = f"{page_num:02d}-*.png"
            found_file = None

            # Find the matching file
            for f in os.listdir(folder_path):
                if f.startswith(f"{page_num:02d}-") and f.endswith(".png"):
                    found_file = os.path.join(folder_path, f)
                    break

            if found_file and add_image_to_pdf(pdf_writer, found_file):
                print(f"Added page {current_page:02d}: {os.path.basename(found_file)}")
                current_page += 1
            else:
                print(f"WARNING: Could not find or add page {page_num:02d}")

    print("\nAdding Word Search PDFs...")

    # Add Word Search PDFs
    word_search_folder = os.path.join(base_path, "11-Word-Search")
    word_search_pdfs = [
        "word-search-kids.pdf",
        "word-search-adults-bonus.pdf",
        "word-search-puzzles.pdf"
    ]

    for pdf_name in word_search_pdfs:
        pdf_path = os.path.join(word_search_folder, pdf_name)
        if os.path.exists(pdf_path):
            try:
                pdf_reader = PdfReader(pdf_path)
                for page in pdf_reader.pages:
                    pdf_writer.add_page(page)
                    print(f"Added page {current_page:02d}: {pdf_name}")
                    current_page += 1
            except Exception as e:
                print(f"Error adding {pdf_name}: {e}")
        else:
            print(f"WARNING: {pdf_name} not found")

    # Write the combined PDF
    print(f"\nWriting combined PDF to {output_pdf}...")
    with open(output_pdf, "wb") as output_file:
        pdf_writer.write(output_file)

    print(f"\n✅ Success! Created {output_pdf} with {current_page - 1} total pages")

    # Verify the output
    if os.path.exists(output_pdf):
        file_size = os.path.getsize(output_pdf) / (1024 * 1024)  # MB
        print(f"File size: {file_size:.2f} MB")

if __name__ == "__main__":
    main()