from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def groups():
    if request.method == 'GET':

    if request.method == 'POST':

    return redirect(url_for('error'))

@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run()
