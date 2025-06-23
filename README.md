Resume Screening App

An intelligent web-based application that automates the initial phase of the recruitment process by matching resumes with a job description using NLP techniques like TF-IDF and Cosine Similarity.

Features

Upload resumes in PDF format
Enter job description manually
Set a custom threshold (e.g., 50%) to filter applicants
View match percentage and selection status
Simple and attractive UI with background images
Lightweight Flask backend with modular code structure
Tech Stack

Frontend: HTML, CSS (with background styling)
Backend: Python (Flask)
Libraries:
PyMuPDF (fitz) for PDF text extraction
scikit-learn for TF-IDF and cosine similarity
Flask-CORS for handling cross-origin requests
Project Structure

resume-screening-app/ │ ├── backend/ │ ├── app.py # Flask backend │ ├── matcher.py # Resume vs JD matching logic │ ├── resume_parser.py # PDF text extractor │ ├── templates/ │ │ ├── index.html # Main upload page │ │ └── result.html # Results display │ └── static/ │ └── style.css # Custom CSS

Create a virtual environment (optional but recommende) python -m venv venv venv\Scripts\activate
2.Install required libraries pip install flask flask-cors pymupdf scikit-learn

3.Install required libraries pip install flask flask-cors pymupdf scikit-learn

4.Run the app python app.py

5.Visit the app http://127.0.0.1:5000/

Sample Data Sample resumes (selected_resume.pdf & rejected_resume.pdf) and job description are provided in /sample-data. Default threshold: 50%

Future Enhancements Support for .docx and other formats

Login system for recruiters

Cloud deployment (AWS/Heroku)

Smart matching using ML models like BERT

Admin dashboard and historical resume tracking

License This project is for educational and academic use.
