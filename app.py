import os
import PyPDF2
import faiss
import numpy as np
from flask import Flask, render_template, request, jsonify
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load models once
embedder = SentenceTransformer('all-MiniLM-L6-v2')
#tokenizer = AutoTokenizer.from_pretrained("HuggingFaceH4/zephyr-7b-beta")
#llm_model = AutoModelForCausalLM.from_pretrained("HuggingFaceH4/zephyr-7b-beta")
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
llm_model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")



# Global FAISS index and mapping
faiss_index = None
doc_chunks = []

# PDF Text Extractor and Chunker
def extract_and_chunk_text(pdf_path, chunk_size=500):
    reader = PyPDF2.PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text()
    
    # Split into chunks
    words = full_text.split()
    chunks = [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

# FAISS Index Builder
def build_faiss_index(chunks):
    embeddings = embedder.encode(chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return index, chunks

# LLM Answer Generator with strict context
def generate_answer(context, question):
    prompt = f"""You are a helpful assistant. Answer the question ONLY using the provided context.

Context:
{context}

Question:
{question}

Answer:"""

    inputs = tokenizer(prompt, return_tensors="pt").to('cpu')
    #outputs = llm_model.generate(**inputs, max_new_tokens=300)
    outputs = llm_model.generate(**inputs, max_new_tokens=150)

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response.split("Answer:")[-1].strip()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_document():
    global faiss_index, doc_chunks
    file = request.files['document']
    if file and file.filename.endswith('.pdf'):
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        doc_chunks = extract_and_chunk_text(file_path)
        faiss_index, doc_chunks = build_faiss_index(doc_chunks)
        return jsonify({'message': 'PDF uploaded and processed successfully!'})
    return jsonify({'message': 'Invalid file format. Please upload a PDF.'})

@app.route('/get_response', methods=['POST'])
def get_response():
    user_question = request.form.get('user_message')

    if not faiss_index:
        return jsonify({'response': 'Please upload a document first.'})
    
    # Embed the question and search
    question_embedding = embedder.encode([user_question])
    D, I = faiss_index.search(np.array(question_embedding), k=3)
    retrieved_chunks = "\n".join([doc_chunks[idx] for idx in I[0]])

    # Generate answer
    answer = generate_answer(retrieved_chunks, user_question)
    return jsonify({'response': answer})

if __name__ == '__main__':
    app.run(debug=True)
