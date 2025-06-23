import os
import uuid
from pathlib import Path
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env.local")

UPLOAD_DIR = Path(os.getenv("UPLOAD_DIR", "uploads"))
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

app = FastAPI()

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    ext = Path(file.filename).suffix
    unique_name = f"{uuid.uuid4().hex}{ext}"
    destination = UPLOAD_DIR / unique_name
    with destination.open("wb") as buffer:
        while True:
            chunk = await file.read(8192)
            if not chunk:
                break
            buffer.write(chunk)
    return JSONResponse({"file_path": str(destination)})

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("UPLOAD_PORT", "5001"))
    uvicorn.run(app, host="0.0.0.0", port=port)
