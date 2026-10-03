from src.pdf_parser import extract_text_from_pdf
from src.text_processor import clean_text
from src.ats_analyzer import analyze_skill_match


resume_text = extract_text_from_pdf("data/sample_resume.pdf")
resume_text = clean_text(resume_text)

with open(
    "data/sample_job_description.txt",
    "r",
    encoding="utf-8"
) as file:
    job_description = file.read()

result = analyze_skill_match(resume_text, job_description)

print("\n--- ATS Analysis ---")
print("Required Skills:", result["required_skills"])
print("Matched Skills:", result["matched_skills"])
print("Missing Skills:", result["missing_skills"])
print("Skill Match Score:", result["match_score"], "%")