from src.pdf_parser import extract_text_from_pdf


def test_pdf_text_extraction():
    text = extract_text_from_pdf("data/sample_resume.pdf")

    assert text
    assert len(text) > 100

    print("PDF extraction test passed!")


if __name__ == "__main__":
    test_pdf_text_extraction()