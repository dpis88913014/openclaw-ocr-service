# OpenClaw OCR Service

基於 Tesseract 的 OCR 微服務，支援繁體中文與英文辨識。透過 FastAPI 提供 REST API，可輕鬆整合至 OpenClaw 或其他應用。

## 功能特色

- 🔤 支援**繁體中文**與**英文** OCR 辨識
- 🚀 基於 **FastAPI** 的高效能 REST API
- 🐳 **Docker** 容器化部署，一鍵啟動
- 📦 輕量化設計，易於整合

## API 使用方式

### POST `/ocr`

接收 Base64 編碼的圖片，回傳 OCR 辨識結果。

**Request Body:**
```json
{
  "image_base64": "data:image/png;base64,iVBORw0KGgo..."
}
```

**Response:**
```json
{
  "text": "辨識出的文字內容"
}
```

## 快速開始

### Docker 部署（推薦）

```bash
docker build -t openclaw-ocr-service .
docker run -p 3000:3000 openclaw-ocr-service
```

### 本地開發

```bash
# 需要先安裝 Tesseract OCR
# Ubuntu: sudo apt-get install tesseract-ocr tesseract-ocr-chi-tra tesseract-ocr-eng
# macOS: brew install tesseract

pip install -r requirements.txt
python main.py
```

服務啟動後即可透過 `http://localhost:3000/ocr` 呼叫 API。

## 技術架構

| 元件 | 技術 |
|------|------|
| Web 框架 | FastAPI |
| OCR 引擎 | Tesseract OCR |
| 容器化 | Docker (python:3.10-slim) |
| 支援語言 | 繁體中文 (chi_tra)、英文 (eng) |

## 環境變數

| 變數名 | 預設值 | 說明 |
|--------|--------|------|
| `PORT` | `3000` | 服務監聽的連接埠 |

## License

MIT
