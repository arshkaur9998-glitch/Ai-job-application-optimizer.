from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from utils.resume_analyzer import analyze_resume
from utils.cover_letter_gen import generate_cover_letter
from utils.interview import start_mock_interview, evaluate_answer

load_dotenv()

app = Flask(__name__)
CORS(app)

# Routes
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "AI Job Application Optimizer API"})

@app.route('/api/analyze-resume', methods=['POST'])
def analyze_resume_route():
    try:
        data = request.json
        resume_text = data.get('resume_text', '')
        
        if not resume_text:
            return jsonify({"error": "Resume text is required"}), 400
        
        analysis = analyze_resume(resume_text)
        return jsonify(analysis)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/generate-cover-letter', methods=['POST'])
def generate_cover_letter_route():
    try:
        data = request.json
        resume_text = data.get('resume_text', '')
        job_description = data.get('job_description', '')
        
        if not resume_text or not job_description:
            return jsonify({"error": "Resume and job description are required"}), 400
        
        cover_letter = generate_cover_letter(resume_text, job_description)
        return jsonify({"cover_letter": cover_letter})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/mock-interview/start', methods=['POST'])
def start_interview():
    try:
        data = request.json
        job_role = data.get('job_role', '')
        
        if not job_role:
            return jsonify({"error": "Job role is required"}), 400
        
        questions = start_mock_interview(job_role)
        return jsonify({"questions": questions})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/mock-interview/evaluate', methods=['POST'])
def evaluate_answer_route():
    try:
        data = request.json
        question = data.get('question', '')
        answer = data.get('answer', '')
        
        if not question or not answer:
            return jsonify({"error": "Question and answer are required"}), 400
        
        feedback = evaluate_answer(question, answer)
        return jsonify(feedback)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
