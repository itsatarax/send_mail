from flask import Flask, render_template, request
import tablib
import json
import os
from email_read import get_csv_data
from mail import isValid

app = Flask(__name__)


valid = []
invalid = []


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        f = request.files['file']
        if not os.path.isdir('./uploads'):
            os.mkdir('./uploads')
        path = os.path.join('./uploads', f.filename)
        f.save(path)
        emails = get_csv_data(f.filename)
        valid.clear()
        invalid.clear()
        for i in emails:
            if isValid(i):
                valid.append(i)
            else:
                invalid.append(i)
        print(valid, len(valid))
        print("\n")
        print(invalid, len(invalid))
        return render_template('index.html')

    return render_template('upload.html')


@app.route("/valid", methods=['GET'])
def val():
    return render_template('show_email.html', your_list=valid, leng=len(valid))


@app.route("/invalid", methods=['GET'])
def inval():
    return render_template('show_email.html', your_list=invalid, leng=len(invalid))


if __name__ == "__main__":
    app.run(debug=True)
