from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import os
from random import randint
import uuid

IMAGE_DIR = "images/"

app = FastAPI()


@app.get("/")
def hello():
    return "Machine Learning Assignment"


@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    file.filename = f"testing.jpg"
    contents = await file.read()

    # save the file
    with open(f"{IMAGE_DIR}{file.filename}", "wb") as f:
        f.write(contents)

    return {"filename": file.filename}


@app.get("/show")
async def get_image():
    # get random file from the image directory
    files = os.listdir(IMAGE_DIR)
    random_index = randint(0, len(files) - 1)

    path = f"{IMAGE_DIR}testing.jpg"

    return FileResponse(path)