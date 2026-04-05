# AI Resume Intelligence 🧠🤖

An automated resume screening and candidate-role mapping system built with Python and Machine Learning.

## 👥 The Team
- **Team Lead:** Siri (ML Logic & System Integration)
- **Member 2:** UI/UX & Frontend Development
- **Member 3:** Data Engineering & Research

## 🚀 Overview
Traditional resume screening is slow. **AI Resume Intelligence** uses Natural Language Processing (NLP) to automate this process. It extracts text from PDF/DOCX resumes, classifies them into job roles using **TF-IDF**, and validates candidate skills.

## ✨ Key Features
- **Smart Role Mapping:** Automatically assigns roles (e.g., Web Developer, Data Scientist).
- **50% Skill Match Threshold:** A quality filter that only assigns roles if the candidate meets 50% of the core requirements.
- **Batch Processing:** Analyze multiple resumes simultaneously.
- **Glassmorphism UI:** A futuristic, dark-themed dashboard built with Streamlit.
- **Exportable Reports:** Download the final analysis as a CSV file.

## 🛠️ Tech Stack
- **Frontend:** Streamlit, HTML/CSS
- **Backend:** Python
- **ML/NLP:** Scikit-learn (TF-IDF, Cosine Similarity)
- **Data:** Pandas, pdfplumber, docx2txt

## 📂 How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt