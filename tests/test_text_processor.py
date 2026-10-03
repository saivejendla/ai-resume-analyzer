from src.text_processor import clean_text, normalize_text


def test_text_cleaning():
    sample = "Python   SQL\n\nMachine Learning"

    cleaned = clean_text(sample)
    normalized = normalize_text(sample)

    assert cleaned == "Python SQL Machine Learning"
    assert normalized == "python sql machine learning"

    print("Text preprocessing test passed!")


if __name__ == "__main__":
    test_text_cleaning()