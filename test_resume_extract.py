from extract_text_from_pdf import extract_text_from_pdf

resume_path = "/Users/sahilagrawal/Documents/IT/Resume/java-resume/Sahil_Agrawal_Resume.pdf"

resume_text = extract_text_from_pdf(resume_path) 

print("==== Resume Text (First 500 characters) ====")
print(resume_text[:500])
