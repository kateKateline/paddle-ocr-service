from fastapi import FastAPI, UploadFile, File, HTTPException
import shutil
import uuid
import os

from app.services.paddleocr.ocr import extract_text

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/ocr")
async def ocr_image(file: UploadFile = File(...)):
    file_path = None
    try:
        # Generate unique filename
        filename = f"{uuid.uuid4()}_{file.filename}"
        file_path = os.path.join(UPLOAD_DIR, filename)

        # Save uploaded file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Verify file was saved
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            raise HTTPException(status_code=400, detail="File upload failed or file is empty")

        # Extract text using OCR
        texts = extract_text(file_path)

        # Combine texts into a single string (or return as list)
        # If you want single string: text_result = "\n".join(texts) if texts else ""
        # For now, returning as list as per original code
        text_result = texts if texts else []

        return {
            "success": True,
            "text": text_result
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "text": []
        }
    finally:
        # Clean up uploaded file after processing
        if file_path and os.path.exists(file_path):
            try:
                os.remove(file_path)
            except Exception:
                pass  # Ignore cleanup errors

            
