from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def classify_and_score(resume_text, roles_dict):
    """Matches resume text against pre-defined roles using TF-IDF."""
    role_names = list(roles_dict.keys())
    role_descriptions = list(roles_dict.values())
    
    # Text Processing
    all_docs = [resume_text] + role_descriptions
    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,2))
    vectors = vectorizer.fit_transform(all_docs)
    
    # Calculate Similarity
    # Compare first vector (Resume) with the rest (Role Vectors)
    similarity_scores = cosine_similarity(vectors[0:1], vectors[1:])[0]
    
    # Identify best match
    best_idx = similarity_scores.argmax()
    
    return {
        "assigned_role": role_names[best_idx],
        "score": round(similarity_scores[best_idx] * 100, 2)
    }