FROM python:3.10-slim

# Install Tesseract engine and language packs
RUN apt-get update && apt-get install -y --no-install-recommends \
    tesseract-ocr \
        tesseract-ocr-chi-tra \
            tesseract-ocr-eng \
                && apt-get clean \
                    && rm -rf /var/lib/apt/lists/*

                    WORKDIR /app
                    COPY . .
                    RUN pip install --no-cache-dir -r requirements.txt

                    EXPOSE 3000
                    CMD ["python", "main.py"]
                    
