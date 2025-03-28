from flask import Flask, render_template, make_response
import os
os.environ['PATH'] += os.pathsep + r'C:\msys64\mingw64\bin'
from weasyprint import HTML
import random
app = Flask(__name__)


def name_gen():
    s = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','Q','W','E','R','T','Y','U','I','O','P']
    res = ''
    for _ in range(0,32):
        res += random.choice(s)
    return res
# Главная страница

@app.route('/')
def index():
    return render_template('index.html')


# Маршрут для генерации PDF
@app.route('/dashboard/')
def dashbord():
    pushlanding = {
        "campaignId": "12345",
        "templateId": "67890"
    }
    mapplanding = {
        'campaignId': '12312',
        'templateId': '12312'
    }
    return render_template("alfa_template.html", pushlanding=pushlanding, mapplanding=mapplanding)

@app.route('/history/')
def history():
    return render_template('history.html')







@app.route('/transfers/client/workflow')
def workflow():
    pushlanding = {
        "campaignId": "12345",
        "templateId": "67890"
    }
    mapplanding = {
        'campaignId': '12312',
        'templateId': '12312'
    }
    return render_template("index3.html", pushlanding=pushlanding, mapplanding=mapplanding)


if __name__ == '__main__':
    print(name_gen())
    app.run(host='0.0.0.0', port=5000)