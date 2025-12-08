#!/usr/bin/env python3
"""
Combine all Winter Survival Kit pages into a single PDF using only PIL.
Includes all 63 PNG pages.
"""

import os
from PIL import Image

def main():
    # Define the folders and files in order
    folders = [
        ("01-Christmas-Winter", [1, 8]),
        ("02-Winter-Remix", [9, 16]),
        ("03-Winter-Activities", [17, 21]),
        ("04-Dinosaurs", [22, 29]),
        ("05-Unicorns-Dragons", [30, 35]),
        ("06-Animals", [36, 43]),
        ("07-Princess-Pirates", [44, 49]),
        ("08-Vehicles", [50, 54]),
        ("09-Space", [55, 58]),
        ("10-Easy-Wins", [59, 63])
    ]

    base_path = "winter-survival-kit"
    output_pdf = os.path.join(base_path, "FULL-KIT-ALL-PAGES.pdf")

    # List to hold all images
    images = []

    print("Collecting PNG pages...")

    # Collect all PNG images in order
    for folder_name, (start_num, end_num) in folders:
        folder_path = os.path.join(base_path, folder_name)
        print(f"\nProcessing {folder_name}...")

        for page_num in range(start_num, end_num + 1):
            # Find the file for this page number
            found_file = None
            for f in os.listdir(folder_path):
                if f.startswith(f"{page_num:02d}-") and f.endswith(".png"):
                    found_file = os.path.join(folder_path, f)
                    break

            if found_file:
                try:
                    img = Image.open(found_file)
                    # Convert to RGB if necessary
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    images.append(img)
                    print(f"  ✓ Added page {page_num:02d}: {os.path.basename(found_file)}")
                except Exception as e:
                    print(f"  ✗ Error with {found_file}: {e}")
            else:
                print(f"  ✗ WARNING: Could not find page {page_num:02d}")

    print(f"\nFound {len(images)} PNG images")

    # Save the first image as PDF with the rest appended
    if images:
        print(f"\nSaving combined PDF to {output_pdf}...")
        images[0].save(
            output_pdf,
            "PDF",
            resolution=150.0,
            save_all=True,
            append_images=images[1:]
        )

        # Close all images
        for img in images:
            img.close()

        print(f"\n✅ Success! Created {output_pdf}")

        # Verify the output
        if os.path.exists(output_pdf):
            file_size = os.path.getsize(output_pdf) / (1024 * 1024)  # MB
            print(f"File size: {file_size:.2f} MB")
    else:
        print("ERROR: No images found to combine")

if __name__ == "__main__":
    main()