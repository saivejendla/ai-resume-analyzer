from src.ats_analyzer import analyze_skill_match


def test_skill_matching():

    resume = """
    Python SQL Machine Learning
    Prompt Engineering RAG
    """

    job_description = """
    Looking for an AI Engineer with Python,
    SQL, Machine Learning, RAG,
    Hugging Face and Embeddings experience.
    """

    result = analyze_skill_match(resume, job_description)

    print("Required:", result["required_skills"])
    print("Matched:", result["matched_skills"])
    print("Missing:", result["missing_skills"])
    print("Match Score:", result["match_score"])

    assert "python" in result["matched_skills"]
    assert "hugging face" in result["missing_skills"]


if __name__ == "__main__":
    test_skill_matching()