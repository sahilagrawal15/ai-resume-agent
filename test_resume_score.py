from extract_keywords_from_jd import extract_keywords_from_jd
from extract_text_from_pdf import extract_text_from_pdf
from score_resume_match import score_resume_match
from generate_suggestions import generate_suggestions
from detect_sections import detect_sections

# --- JD input ---
jd_text = """
We are seeking a Backend Engineer to join our growing fintech platform team. The ideal candidate will have at least 3 years of experience working with scalable backend systems using Java and Spring Boot.

Responsibilities include designing microservices architectures, integrating with RESTful APIs, and deploying applications using Docker and AWS services such as Lambda, EC2, and S3.

You should be comfortable working in CI/CD environments and have hands-on experience with infrastructure as code (Terraform preferred). Familiarity with Kafka, PostgreSQL, Redis, and monitoring tools like Prometheus or Grafana is a plus.

We work in a fast-paced Agile environment, so good collaboration skills and familiarity with tools like JIRA, GitHub, and Confluence is expected.
"""


# --- Resume path ---
resume_path = "/Users/sahilagrawal/Documents/IT/Resume/java-resume/Sahil_Agrawal_Resume.pdf"  # Update to your actual path

# --- Run pipeline ---
jd_keywords = extract_keywords_from_jd(jd_text)
resume_text = extract_text_from_pdf(resume_path)
target_role = "backend_engineer"
score, found, missing = score_resume_match(jd_keywords, resume_text, role=target_role)
section_results = detect_sections(resume_text)

# --- Display results ---
print(f"\n🧠 ATS Match Score: {score}/100")
print("✅ Found Keywords:", found)
print("❌ Missing Keywords:", missing)

print("\n📂 Resume Sections Check:")
for section, present in section_results.items():
    icon = "✅" if present else "❌"
    print(f"{icon} {section.capitalize()}")

# --- AI bullet suggestions ---
suggestions = generate_suggestions(missing)
print("\n🛠 AI-Generated Resume Suggestions:")
for s in suggestions:
    print(s)
