import base64
from random import randrange
from string import ascii_lowercase
from typing import Annotated, Union

import cv2
import numpy as np
import pytesseract
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from random_word import RandomWords

# from doctr.io import DocumentFile
# from doctr.models import ocr_predictor

# model = ocr_predictor(pretrained=True)

r = RandomWords()


class Drawing(BaseModel):
    image: str
    words: str | None = None


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/words")
def get_words():
    # return {"words": ascii_lowercase[randrange(len(ascii_lowercase))]}

    word = r.get_random_word()
    if len(word) > 3:
        word = word[:3]
    return {"words": word}


@app.get("/")
def index(request: Request):
    img_cv = cv2.imread(r"ocr_image.png")

    # By default OpenCV stores images in BGR format and since pytesseract assumes RGB format,
    # we need to convert from BGR to RGB format/mode:
    img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
    contents = pytesseract.image_to_string(img_rgb, config=r"--psm 10", lang="ewe")
    print(contents)

    # OR
    # img_rgb = Image.frombytes("RGB", img_cv.shape[:2], img_cv, "raw", "BGR", 0, 0)
    # print(pytesseract.image_to_string(img_rgb))

    return templates.TemplateResponse(
        "index.html",
        {"request": request},
    )


@app.post("/ocr")
def read_item(body: Drawing):
    if body.image.startswith("data:"):
        params, data = body.image.split(",", 1)
        params = params[5:] or "text/plain;charset=US-ASCII"
        params = params.split(";")
        # if not '=' in params[0] and '/' in params[0]:
        #     mimetype = params.pop(0)
        # else:
        #     mimetype = 'text/plain'
        # if 'base64' in params:
        #     print(data)
        #     # handle base64 parameters first
        #     data = data.decode('base64')
        # for param in params:
        #     if param.startswith('charset='):
        #         # handle characterset parameter
        #         data = parse.unquote(data).decode(param.split('=', 1)[-1])

        # print(data)

        # # Assume `base64_string` is the base64 string you want to convert
        # # Decode the base64 string to bytes
        # b64_string = body.image
        # b64_string += "=" * ((4 - len(body.image) % 4) % 4) #ugh
        image_bytes = base64.b64decode(data)

        # # Convert bytes to numpy array
        image_array = np.frombuffer(image_bytes, dtype=np.uint8)

        # # Decode image array using OpenCV
        img = cv2.imdecode(image_array, cv2.IMREAD_GRAYSCALE)
        cv2.imwrite("ocr_image.png", img)

        # single_img_doc = DocumentFile.from_images("test.png")
        # result = model(single_img_doc)
        # print(result)
        # print("here")

        # img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # cv2.imshow('Image', thresh)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        contents = pytesseract.image_to_string(thresh, config=r"--psm 10", lang="ewe")
        print(contents)

        return {"words": contents}

    # # # Display or save the image as needed

    # print(body)
    return {"words": body.words}
