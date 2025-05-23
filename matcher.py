from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_resume(resume_text, job_description):
    documents = [job_description, resume_text]

    # Create TF-IDF vectors
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Compute cosine similarity (job vs resume)
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    # Return percentage
    return round(float(similarity[0][0]) * 100, 2)
