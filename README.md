# Scanned PDF Text Extrater 
# PDF to Docx Converter (non readable pdf, scanned document pdfs)

This is a Python application that converts non-readable PDF files, such as scanned documents, into readable Word documents. It achieves this by first converting the PDF files into images and then extracting the text from the images to create the Word documents. The application provides a user-friendly interface where you can upload PDF files, select the files you want to convert, and initiate the conversion process. Once the conversion is completed, the converted Word documents can be downloaded from the application.

## Installation

1. Clone the repository:

    ```shell
    git clone https://github.com/arjun-mavonic/scanned-pdf-text-extractor.git
    ```

2. Navigate to the project directory:

    ```shell
    cd scanned-pdf-text-extractor
    ```

3. Create a virtual environment:

    ```shell
    python -m venv venv
    ```

4. Activate the virtual environment:

    - For Windows:

      ```shell
      venv\Scripts\activate
      ```

    - For macOS/Linux:

      ```shell
      source venv/bin/activate
      ```

5. Install the dependencies:

    ```shell
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:

    ```shell
    streamlit run main.py
    ```

2. Upload a PDF file using the file uploader component.

3. Select the PDF files you want to convert to images by checking the checkboxes.

4. Click the "Convert" button to start the conversion process.

5. Once the conversion is completed, the converted Word documents will be available for download in the right column.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
---
title: Scanned Pdf Text Extractor
emoji: 🐨
colorFrom: yellow
colorTo: gray
sdk: streamlit
sdk_version: 1.35.0
app_file: app.py
pinned: false
license: mit
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
