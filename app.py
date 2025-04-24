import streamlit as st
from extract_keywords_from_jd import extract_keywords_from_jd
from extract_text_from_pdf import extract_text_from_pdf
from score_resume_match import score_resume_match
from generate_suggestions import generate_suggestions
from detect_sections import detect_sections

st.set_page_config(page_title="AI Resume Evaluator", layout="wide")

st.markdown("""
<style>
body {
    background-color: #fdfdfd;
    color: #1a1a1a;
}
.big-title {
    font-size: 2.75rem !important;
    color: #1a202c;
    font-weight: 700;
    margin-bottom: 0.25rem;
}
.sub-title {
    font-size: 1.1rem;
    color: #2d3748;
    margin-bottom: 2rem;
}
.boxed {
    background-color: #ffffff;
    padding: 1rem;
    border-radius: 0.5rem;
    border: 1px solid #e2e8f0;
}
.section-title {
    font-size: 1.3rem;
    font-weight: 600;
    margin-top: 1.2rem;
    margin-bottom: 0.4rem;
    color: #2d3748;
}
.metric-box {
    background-color: #edf2f7;
    color: #2c5282;
    padding: 1.5rem;
    border-radius: 0.5rem;
    text-align: center;
    font-size: 1.6rem;
    font-weight: 700;
    border: 1px solid #cbd5e0;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.02);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">📊 AI Resume Evaluator</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Score your resume instantly, find missing keywords, and get high-impact improvement tips — all from one page.</div>', unsafe_allow_html=True)

# Upload Resume & JD
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 📤 Upload Resume (PDF)")
    resume_file = st.file_uploader("", type=["pdf"])
    st.markdown("### 🎯 Target Role")
    role = st.selectbox("", ["backend_engineer", "data_engineer", "frontend_engineer"], label_visibility="collapsed")

with col2:
    st.markdown("### 📄 Paste Job Description")
    jd_text = st.text_area("Paste full job description", height=250)

if st.button("🚀 Analyze"):
    if resume_file and jd_text:
        with st.spinner("Analyzing your resume against the JD..."):
            resume_text = extract_text_from_pdf(resume_file)
            jd_keywords = extract_keywords_from_jd(jd_text)
            score, found, missing = score_resume_match(jd_keywords, resume_text, role=role)
            suggestions = generate_suggestions(missing)
            sections = detect_sections(resume_text)

        # Score and Skill Display
        col_a, col_b = st.columns([1, 2])

        with col_a:
            st.markdown("<div class='section-title'>🎯 ATS Match Score</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='metric-box'>{score} / 100</div>", unsafe_allow_html=True)

            st.markdown("<div class='section-title'>✅ Found Skills</div>", unsafe_allow_html=True)
            st.success(", ".join(found) if found else "None")

            st.markdown("<div class='section-title'>❌ Missing Skills</div>", unsafe_allow_html=True)
            st.error(", ".join(missing) if missing else "None")

        with col_b:
            st.markdown("<div class='section-title'>📂 Resume Sections</div>", unsafe_allow_html=True)
            col_s1, col_s2 = st.columns(2)
            section_items = list(sections.items())
            half = len(section_items) // 2 + len(section_items) % 2
            for name, present in section_items[:half]:
                icon = "✅" if present else "❌"
                col_s1.markdown(f"- {icon} {name.capitalize()}")
            for name, present in section_items[half:]:
                icon = "✅" if present else "❌"
                col_s2.markdown(f"- {icon} {name.capitalize()}")

            st.markdown("<div class='section-title'>💡 Suggestions to Improve</div>", unsafe_allow_html=True)
            for s in suggestions:
                st.markdown(f"- {s}")

        with st.expander("📋 Preview Parsed Resume Text"):
            st.code(resume_text[:3000] + ("..." if len(resume_text) > 3000 else ""), language="markdown")

    else:
        st.warning("Please upload a resume and paste the job description to proceed.")
