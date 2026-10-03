import re


def clean_text(text):
    """Clean and normalize extracted resume text."""

    if not text:
        return ""

    # Replace multiple whitespace characters with a single space
    text = re.sub(r"\s+", " ", text)

    # Remove unnecessary spaces before punctuation
    text = re.sub(r"\s+([,.!?;:])", r"\1", text)

    return text.strip()


def normalize_text(text):
    """Normalize text for keyword and ATS comparison."""

    text = clean_text(text)

    return text.lower()