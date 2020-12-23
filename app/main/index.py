from flask import Blueprint, request, render_template, flash, redirect, url_for
from app.main.tojpg import convertPDF


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
