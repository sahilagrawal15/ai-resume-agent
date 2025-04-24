from extract_keywords_from_jd import extract_keywords_from_jd
from extract_text_from_pdf import extract_text_from_pdf
from score_resume_match import score_resume_match

# Sample job description (can replace with real one) 
jd_text = """
Looking for a backend engineer skilled in Java, Spring Boot, AWS, REST APIs, and Docker.
Experience with microservices and CI/CD pipelines is a plus.
"""

# Extract JD keywords
jd_keywords = extract_keywords_from_jd(jd_text)

# Load resume
resume_text = extract_text_from_pdf("/Users/sahilagrawal/Documents/IT/Resume/java-resume/Sahil_Agrawal_Resume.pdf")  

# Score
score, found, missing = score_resume_match(jd_keywords, resume_text)

# Results
print(f"\n🧠 ATS Match Score: {score}/100")
print("✅ Found Keywords:", found)
print("❌ Missing Keywords:", missing)
