SKILL_ALIASES = {
    "python": ["python"],
    "sql": ["sql"],
    "pandas": ["pandas"],
    "numpy": ["numpy"],
    "machine learning": ["machine learning", "ml"],
    "generative ai": ["generative ai", "genai", "gen ai"],
    "llm": ["llm", "llms", "large language model", "large language models"],
    "prompt engineering": ["prompt engineering", "prompt design"],
    "rag": ["rag", "retrieval augmented generation"],
    "embeddings": ["embedding", "embeddings"],
    "hugging face": ["hugging face", "huggingface"],
    "vector database": [
        "vector database",
        "vector databases",
        "vector db",
        "vector dbs",
    ],
    "git": ["git", "github"],
    "power bi": ["power bi", "powerbi"],
}


def contains_skill(text, aliases):
    return any(alias in text for alias in aliases)


def analyze_skill_match(resume_text, job_description):
    resume_text = resume_text.lower()
    job_description = job_description.lower()

    required_skills = []
    matched_skills = []
    missing_skills = []

    for skill, aliases in SKILL_ALIASES.items():

        if contains_skill(job_description, aliases):
            required_skills.append(skill)

            if contains_skill(resume_text, aliases):
                matched_skills.append(skill)
            else:
                missing_skills.append(skill)

    match_score = (
        round(len(matched_skills) / len(required_skills) * 100, 2)
        if required_skills
        else 0
    )

    return {
        "required_skills": required_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_score": match_score,
    }