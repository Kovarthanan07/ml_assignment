from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import os
import cv2
import yolov7
import glob

IMAGE_DIR = "images/"

app = FastAPI()

@app.get("/")
def hello():
    return "Machine Learning Assignment"


@app.post("/detect_objects")
async def upload_image(file: UploadFile = File(...)):
    file.filename = f"testing.jpg"
    contents = await file.read()

    # Getting the posted image and saving in a directory
    with open(f"{IMAGE_DIR}{file.filename}", "wb") as f:
        f.write(contents)

    submitted_image = img = cv2.imread(IMAGE_DIR + file.filename)
    submitted_image = cv2.cvtColor(submitted_image, cv2.COLOR_BGR2RGB)

    # load pretrained yolov7-tiny from hugging face
    model = yolov7.load('kadirnar/yolov7-tiny-v0.1', hf_model=True)

    # set model parameters
    model.conf = 0.25  # NMS confidence threshold
    model.iou = 0.45  # NMS IoU threshold
    model.classes = None  # (optional list) filter by class

    results = model(submitted_image)

    # inference with larger input size and test time augmentation
    results = model(submitted_image, size=1280, augment=True)

    # detection results
    predictions = results.pred[0]
    boxes = predictions[:, :4]  # x1, y1, x2, y2
    scores = predictions[:, 4]
    categories = predictions[:, 5]

    # save image with detection bounding boxes on image
    results.save(IMAGE_DIR + "results")

    return "Detected image is saved in images/results directory"


@app.get("/detection_results")
async def get_image():
    # get random file from the image directory
    path = f"{IMAGE_DIR}/results"

    # getting the latest image added in the directory
    files_path = os.path.join(path, '*')
    files = sorted(
        glob.iglob(files_path), key=os.path.getctime, reverse=True)

    return FileResponse(files[0])