# OCR Data Software Package

## Overview
This package contains organized OCR image-text mappings extracted from the Inscription Project dataset.
All 2043 inscriptions have been mapped and organized into multiple formats for easy access and integration.

## Folder Structure

```
OCR_Data_Software_Package/
├── images/              # Symlinks or references to original images
├── texts/               # Individual text files for each image (.txt)
├── mappings/            # Consolidated mapping files (JSON, CSV, Python)
├── data_exports/        # Exported data in various formats
├── tools/               # Python utilities for data manipulation
├── docs/                # Documentation
└── README.md           # This file
```

## Files

### Main Index Files (in `mappings/`)
- **ocr_mappings.json** - Complete mapping in JSON format (Unicode text)
- **ocr_mappings.csv** - Tabular format (Image_Filename, OCR_Text, Confidence)
- **ocr_mappings.py** - Python module for programmatic access

### Individual Text Files (in `texts/`)
- Named by image number (e.g., `1.txt`, `2.txt`, ..., `2043.txt`)
- Each contains image metadata and the recognized OCR text

## Usage

### Python
```python
from tools.ocr_mappings import get_text, search_text, get_all_images

# Get text for a specific image
text = get_text('2040.jpg')
print(text)

# Search for inscriptions containing specific text
results = search_text('चे गोत्र')
for img_name, data in results:
    print(f"{img_name}: {data['text']}")

# Get all images
images = get_all_images()
print(f"Total images: {len(images)}")
```

### CSV/Excel
Open `mappings/ocr_mappings.csv` in Excel, Google Sheets, or any spreadsheet application.

### JSON
Load `mappings/ocr_mappings.json` in any JSON parser or REST API.

## Data Format

### JSON Structure
```json
{
  "metadata": {
    "total_entries": 2043,
    "format_version": "1.0"
  },
  "mappings": {
    "1.jpg": {
      "filename": "1.jpg",
      "text": "Marathi/Sanskrit inscription text",
      "confidence": 85.0
    }
  }
}
```

### CSV Format
```
Image_Filename,OCR_Text,Confidence
1.jpg,स्वास्निधी राजमान्य...,85.0
2.jpg,च श्रीमंता विनंती...,86.0
```

## Sample Entry - Image 2040

**Image:** 2040.jpg  
**Confidence:** 99.0%  
**Text:** चे गोत्र पुरुश यांसी कजिया करितील अगर दतपुत्राचा संशये चितात आणून उपस्वर्ग लावितील

## Statistics

- **Total Inscriptions:** 2043
- **Format:** Images (.jpg) with Marathi/Devanagari text
- **Encoding:** UTF-8
- **Character Set:** Devanagari (Marathi/Sanskrit)
- **Confidence Range:** 85.0% - 99.0%

## Tools Provided

### extract_and_organize.py
Regenerates the mappings from the original `data_mapping.js` file.

```bash
python tools/extract_and_organize.py
```

### search_inscriptions.py (Optional)
Command-line tool to search inscriptions.

```bash
python tools/search_inscriptions.py "search_term"
```

## Integration

### Web Application
Use `mappings/ocr_mappings.json` as an API endpoint or load directly in JavaScript.

### Database
Import `mappings/ocr_mappings.csv` into PostgreSQL, MySQL, MongoDB, or any database.

### Data Analysis
Use Python with pandas:
```python
import pandas as pd

df = pd.read_csv('mappings/ocr_mappings.csv')
print(df.describe())
```

## Version History

- **v1.0** (2026-04-30) - Initial software package generation
  - Extracted from regenerated data_mapping.js with corrected UTF-8 encoding
  - All 2043 inscriptions properly mapped with Devanagari text

## Notes

- All text is encoded in UTF-8
- Devanagari script properly handled with Unicode escape sequences (\uXXXX)
- Confidence scores range from 85% to 99%
- Images are referenced by filename (1.jpg, 2.jpg, etc.)

## Support

For questions or data verification, refer to the source `data_mapping.js` file.

---
**Generated:** 2026-04-30
