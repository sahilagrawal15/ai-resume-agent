import re

SECTION_HEADERS = {
    "summary": ["summary", "objective", "professional summary"],
    "skills": ["skills", "technical skills", "core competencies"],
    "experience": ["experience", "work experience", "professional experience"],
    "projects": ["projects", "personal projects", "side projects"],
    "education": ["education", "academic background", "qualifications"],
    "certifications": ["certifications", "licenses", "courses"]
}

def detect_sections(resume_text):
    """
    Detects which major resume sections are present in the text.

    Returns:
        dict: section_name -> True/False
    """
    text = resume_text.lower()
    results = {}

    for section, patterns in SECTION_HEADERS.items():
        found = any(re.search(rf"\b{re.escape(p)}\b", text) for p in patterns)
        results[section] = found

    return results
