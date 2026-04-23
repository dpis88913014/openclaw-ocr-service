from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pytesseract
from PIL import Image
import base64
import io
import os

app = FastAPI()

class OCRRequest(BaseModel):
    image_base64: str

@app.post("/ocr")
async def perform_ocr(request: OCRRequest):
    try:
        # 解碼 Base64 圖片
        header, encoded = request.image_base64.split(",", 1) if "," in request.image_base64 else (None, request.image_base64)
        image_data = base64.b64decode(encoded)
        image = Image.open(io.BytesIO(image_data))

        # 執行 Tesseract OCR (支援繁中與英文)
        # 注意：我們只做初步辨識，糾錯邏輯建議放在 OpenClaw 端呼叫 LLM
        text = pytesseract.image_to_string(image, lang='chi_tra+eng')
        
        return {"text": text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))