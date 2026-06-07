# 🏛️ Ancient Inscription OCR - Software Manual

## 1. Introduction
This software package is a complete solution for the recognition and exploration of ancient Marathi inscriptions. It consists of two primary modules:
1.  **Data Explorer**: An interactive database of 2,043 verified inscriptions.
2.  **ML Model Dashboard**: A performance evaluation suite for the Attention-based Transformer model.

## 2. Installation
Before running the software, ensure you have Python 3.8+ installed and run the following in your terminal:

```bash
pip install -r ../OCR_Software_Package/requirements.txt
```

## 3. Running the Software
You have two ways to start the application:

### Method A: Unified Application (Recommended)
Run the `launcher.py` script. It provides a simple menu to switch between the Explorer and the ML Dashboard.

### Method B: Manual Start
If you wish to run the **Data Explorer** manually to search inscriptions:
1. Open terminal in `OCR_Data_Software_Package`.
2. Run: `python -m http.server 8000`
3. Open browser to: `http://localhost:8000`

> **⚠️ IMPORTANT:** Do not open the HTML files directly (by double-clicking them). This causes a "Database Loading Error" because browsers block local file access for security. Always use the server commands above.

## 4. Module Features

### 🔍 Data Explorer (Port 8000)
*   **Search**: Find specific words like "पुरुश" or "गोत्र" across all 2,043 entries.
*   **Look-up**: Enter a filename (e.g., `2040.jpg`) to see the OCR result and confidence.
*   **Export**: Download data as JSON, CSV, or Python modules.

### 🤖 ML Dashboard (Port 8080)
*   **Real-time Inference**: Enter a filename to see how the model processes the script.
*   **Analytics**: View Accuracy, CER (Character Error Rate), and Loss curves.
*   **Comparison**: See how this model performs against baseline CRNN and Transformer models.

## 5. Troubleshooting

**Error: "Database loading error"**
*   **Cause**: You opened the file directly in the browser using `file://` protocol.
*   **Fix**: Run the Python server command and use `http://localhost:8000`.

**Error: "Port 8000 already in use"**
*   **Fix**: Close other terminal windows or run on a different port: `python -m http.server 8001`.

**Marathi text looks like boxes?**
*   **Fix**: Ensure you have a Devanagari-compatible font installed (e.g., Nirmala UI or Noto Sans).

---
*Developed as part of the 7th Semester Computer Science Inscription Project.*
*Date: April 2026*