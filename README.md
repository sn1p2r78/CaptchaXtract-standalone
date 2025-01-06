# CaptchaXtract-Standalone

This is the standalone user-version of the CaptchaXtract project. It enables local use of the service, including options for text-extraction, and image-to-text conversion.

## Features

- Local IMG file to text conversion using Tesseract OCR
- Fully self-contained deployment options

## Setup

Install the package via pip:
 ``sh
pip install captcha-xtract-standalone
```

## Usage

Example usage to analyze text using the module:

```pe
text = captcha_xtract.extract(image_path)
print(text)
```