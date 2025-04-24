from extract_keywords_from_jd import extract_keywords_from_jd

jd_text = """
We're hiring a backend engineer experienced in Java, Spring Boot, AWS, and REST APIs. 
Must be comfortable with microservices, Docker, and CI/CD pipelines.
"""

keywords = extract_keywords_from_jd(jd_text)

print("=== Cleaned Keywords ===")
for kw in keywords:
    print("-", kw)

