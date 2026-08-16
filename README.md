# AI Resume Intelligence 🧠🤖

An automated resume screening and candidate-role mapping system built with Python and Machine Learning.

## 👥 The Team
## 👥 Contributors

* **Jampa Siri Chandana Priya** ([@24A31A4210](https://github.com/24A31A4210)) — **Project Lead & AI System Architect**
  * Overall system design, AI model selection, and End-to-End Integration.
* **Guru Tulasi Hima Bindu** ([@24A31A4209](https://github.com/24A31A4209)) — **NLP Specialist & Logic Developer**
  * Core logic implementation, Text cleaning, and Keyword mapping using NLP.
* **Piradi Sai Rupa Sri** ([@24A31A4227](https://github.com/24A31A4227)) — **UI/UX & Frontend Developer**
  * Building the interactive Streamlit dashboard and futuristic CSS animations.
* **Chitturi Dhanu Sree** ([@24A31A4207](https://github.com/24A31A4207)) — **Data Engineering & Performance Analyst**
  * Dataset preparation, preprocessing, and model accuracy testing.
* **Chikkala Mary Blessica** ([@24A31A4206](https://github.com/24A31A4206)) — **Technical Documentation & Deployment**
  * Project requirement analysis, README documentation, and Environment configuration.

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
