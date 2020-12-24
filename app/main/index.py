from flask import Blueprint, request, render_template, flash, redirect, url_for
from app.main.tojpg import convertPDF
import numpy as np
import cv2


main = Blueprint('main', __name__, url_prefix='/')


@main.route('/', methods=['GET'])
def index():
    # /main/index.html은 사실 /project_name/app/templates/main/index.html을 가리킵니다.
    return render_template('index.html')


@main.route('/tojpg')
def tojpg():
    convertPDF()
    response = '변환 완료'
    return render_template('index.html', response=response)


@main.route('/edge')
def detectEdge():
    image = cv2.imread('./app/static/img/cut_first_frame_dpi500/1.jpg')
    orig = image.copy()

    r = 800.0 / image.shape[0]
    dim = (int(image.shape[1] * r), 800)
    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    edged = cv2.Canny(gray, 75, 200)

    print("Edge Detection")

    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Edged', cv2.WINDOW_NORMAL)
    cv2.imshow("Image", image)
    cv2.imshow("Edged", edged)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
