# 🧠 AI Resume Evaluator

An intelligent, resume-to-JD matching tool that gives you an ATS-style score, highlights missing skills, and suggests improvements — all with a clean, interactive UI.

---

## 🚀 Features

- 📄 **Upload your resume (PDF)**
- 📋 **Paste a job description**
- 🎯 **Get an ATS Match Score (0–100)**
- ✅ **See found vs missing skills**
- 💡 **Get improvement suggestions**
- 📂 **Check for missing resume sections** (Summary, Skills, Projects, etc.)
- 🧽 **Smart filtering** of noisy JD phrases (e.g., "team player", "passionate")
- 🧠 **Soft match expansion** for vague terms like "software development"
- 🎨 Built using **Streamlit**, with responsive layout and modern color theme

---

## 📦 Setup Instructions

1. **Clone the repo:**
```bash
git clone https://github.com/your-username/ai-resume-evaluator.git
cd ai-resume-evaluator
```

2. **Create and activate a virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the app locally:**
```bash
streamlit run app.py
```

---

## 🛠 Project Structure

```
ai_resume_evaluator/
├── app.py                        # Streamlit UI
├── score_resume_match.py        # ATS scoring logic with fuzzy matching and weighted importance
├── jd_keyword_extractor.py      # Keyword extractor using KeyBERT + tech skill filtering
├── extract_text_from_pdf.py     # Resume parser using PyMuPDF
├── generate_suggestions.py      # Suggest improvements based on missing skills
├── detect_sections.py           # Detect if key resume sections exist
├── tech_skills.py               # Validated tech skill set for filtering
├── skill_weights.py             # Custom importance weights for core skills
├── requirements.txt             # Python dependencies
└── README.md
```

---

## 📚 Tech Stack

- **Streamlit** – UI & layout
- **KeyBERT** – Extracting keywords from JD
- **PyMuPDF** – PDF resume text extraction
- **Difflib** – Fuzzy text matching
- **Python 3.8+** – Base runtime

---

## 📌 To-Do / Coming Soon

- [ ] Keyword highlighting inside resume preview
- [ ] Export report as PDF
- [ ] Role-specific skill matching refinement
- [ ] Live deployment via Streamlit Cloud

---

## 🙌 Contributions
Pull requests welcome! Feel free to suggest improvements or feature requests.

---

## 📝 License
MIT © 2024