import streamlit as st
import pandas as pd
from utils.extractor import extract_text_from_file
from utils.ml_logic import classify_and_score

# Page Config
st.set_page_config(page_title="AI Resume Intelligence", layout="wide")

# ==========================================
# 💎 PREMIUM DESIGN
# ==========================================
st.markdown("""
<style>
    .stApp { background: radial-gradient(circle at 50% 50%, #1e1e3f 0%, #0c0c1e 100%); }
    .hero-title {
        font-size: 50px; font-weight: 800; text-align: center;
        background: linear-gradient(to right, #00f2fe, #4facfe, #7c3aed);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .glass-box {
        background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px; padding: 25px; backdrop-filter: blur(15px);
    }
</style>
""", unsafe_allow_html=True)

# Skills Database (Target Roles)
ROLES_DB = {
    "Data Scientist": ["Python", "Machine Learning", "SQL", "Statistics", "Deep Learning", "NLP"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "React", "Node.js", "Database Management"],
    "Project Manager": ["Agile", "Scrum", "Leadership", "Risk Management", "Communication"],
    "Marketing Specialist": ["SEO", "Branding", "Digital Marketing", "Content Strategy", "Google Ads"],
    "System Analyst": ["System Design", "SDLC", "Requirements Gathering", "UML", "SQL"]
}

st.markdown("<h1 class='hero-title'>AI RESUME INTELLIGENCE 🧠🤖</h1>", unsafe_allow_html=True)

c1, c2 = st.columns([0.8, 1.5], gap="large")

with c1:
    st.markdown('<div class="glass-box">', unsafe_allow_html=True)
    st.subheader("🎯 Target Role & Upload")
    
    # 1. Role Selection Dropdown added before uploading
    selected_role = st.selectbox(
        "Select Target Role for Evaluation:",
        options=list(ROLES_DB.keys())
    )
    
    # Show required skills for the selected role as a reference
    with st.expander(f"View Required Skills for {selected_role}"):
        st.write(", ".join(ROLES_DB[selected_role]))

    st.markdown("---")
    files = st.file_uploader("Upload Resumes", accept_multiple_files=True)
    run_btn = st.button("✨ START ANALYSIS")
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown("### 🔍 Live Analysis Results")
    
    if run_btn and files:
        results_data = []
        for file in files:
            with st.spinner(f"Scanning {file.name}..."):
                text = extract_text_from_file(file)
                
                # Get expected skills for the chosen target role
                expected_skills = ROLES_DB.get(selected_role, [])

                # Skill Matching Logic against the selected role
                found_skills = [s for s in expected_skills if s.lower() in text.lower()]
                missing_skills = [s for s in expected_skills if s.lower() not in text.lower()]
                
                # 50% Threshold Check for the target role
                match_percentage = (len(found_skills) / len(expected_skills)) * 100 if expected_skills else 0
                
                if match_percentage >= 50:
                    verdict = f"✅ Perfect for {selected_role}"
                else:
                    verdict = f"❌ Not a Good Fit for {selected_role}"

                results_data.append({
                    "Candidate File": file.name,
                    "Target Role": selected_role,
                    "Match %": f"{match_percentage:.1f}%",
                    "Verdict": verdict,
                    "Skills Found ✅": ", ".join(found_skills) if found_skills else "None",
                    "Missing Skills ❌": ", ".join(missing_skills) if missing_skills else "None"
                })
        
        # Display Results Table
        st.markdown("#### 📋 Candidate Summary Report")
        df = pd.DataFrame(results_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # CSV Download
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(label="📥 Download CSV", data=csv, file_name="role_evaluation_report.csv", mime="text/csv")
    else:
        st.info("Select a role, upload resumes, and click 'Start Analysis'.")