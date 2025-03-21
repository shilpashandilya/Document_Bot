# Document-Based Chatbot

This project is a **Document-Based Chatbot** built using **Flask** (for the backend) and **HTML/CSS** (for the frontend). It allows users to upload a document (PDF), and then interact with the chatbot to ask questions based on the content of the document. The chatbot will provide responses derived from the document's content.

## Features

- Upload a PDF document.
- Ask questions based on the content of the document.
- Get relevant, fact-based responses from the document.
- Simple, intuitive user interface.

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Model**: Open-source transformer-based models for question answering (e.g., `DistilBERT`, `T5`, etc.)
- **Libraries**:
  - `transformers` (for NLP and model inference)
  - `Flask` (for the web framework)
  - `PyPDF2` or `pdfplumber` (for PDF text extraction)
  - `faiss` (for indexing and similarity search)
  - `numpy`, `pandas` (for data handling)

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/your-username/document-chatbot.git
    cd document-chatbot
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - **Windows**:
      ```bash
      .\venv\Scripts\activate
      ```
    - **macOS/Linux**:
      ```bash
      source venv/bin/activate
      ```

4. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Flask application**:
    ```bash
    python app.py
    ```

2. **Open the application in your browser**:
    - Go to `http://127.0.0.1:5000` in your web browser.
    - You should be able to upload a PDF and ask questions related to its content.

3. **Interacting with the chatbot**:
    - Upload a PDF document using the "Upload PDF" button.
    - After uploading, type your questions in the chat window, and the chatbot will respond based on the document.

## Example

### Step 1: Upload Document

- Use the "Upload PDF" button to upload a document.

### Step 2: Ask a Question

- Once the document is uploaded, ask questions like:
    - "What is the main topic of this document?"
    - "Explain the concept of plate tectonics mentioned in the document."

### Step 3: Get Answer

- The chatbot will analyze the document and provide a relevant response based on its content.

## Screenshots

Here is a screenshot of the chat interface:

![Screenshot](assets/screenshot.png)

<img width="724" alt="image" src="https://github.com/user-attachments/assets/7398e199-feca-4aa6-90e2-ee2ef2204971" />
<img width="691" alt="image" src="https://github.com/user-attachments/assets/0153be6d-f6e3-4d93-8a3d-d94739c54b47" />




## Contributing

If you'd like to contribute to the project:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Hugging Face for providing transformer models.
- Flask for the web framework.
- All contributors and open-source libraries that made this project possible.

