# This is a sample Python script.
from flask import Flask,request,redirect
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
app = Flask(__name__)
@app.before_request

def before_request():
    if request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    app.run(host='0.0.0.0',port=80)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
