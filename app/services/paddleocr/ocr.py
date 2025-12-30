from paddleocr import PaddleOCR

ocr = PaddleOCR(
    use_angle_cls=True,
    lang='id'
)

def extract_text(image_path: str):
    try:
        result = ocr.ocr(image_path)

        texts = []

        if not result or not isinstance(result, list):
            return texts

        # PaddleX OCR Pipeline format
        for page in result:
            if isinstance(page, dict) and 'rec_texts' in page:
                for text in page['rec_texts']:
                    if text and isinstance(text, str):
                        texts.append(text.strip())

        return texts

    except Exception as e:
        print("OCR ERROR:", str(e))
        import traceback
        traceback.print_exc()
        return []
