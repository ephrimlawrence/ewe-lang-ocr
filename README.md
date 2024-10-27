# Ewe Language OCR
> A OCR for the Ewe language using Tesseract OCR

The project consists of two parts, training of the Tesseract OCR engine (with english as the base model) to recognize the Ewe language, and the second part is a web application that uses the trained model to recognize text in images.

## Web application setup
1. Install Tesseract OCR
2. Run `pip install -r requirements.txt` to install the required packages.
3. In the `app` directory, run `sh start-server.sh` to start the web application.

## Training Setup
1. Clone [tesstrain](https://github.com/tesseract-ocr/tesstrain) into the root directory
2. Execute `sh train-model.sh` to start the training process. The final model will be copied to the `app` directory.
