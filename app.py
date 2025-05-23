from flask import Flask, render_template, request
from resume_parser import extract_text_from_pdf
from matcher import match_resume

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    jd = request.form['job_description']
    threshold = int(request.form['threshold'])
    file = request.files['resume']
    
    resume_text = extract_text_from_pdf(file)
    match_percentage = match_resume(resume_text, jd)
    
    status = "Selected" if match_percentage >= threshold else "Rejected"
    
    return render_template('result.html', percentage=match_percentage, status=status)

# ✅ This should be at the very end of your file
if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True)
