from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/spending')
def spending():
    return render_template('spending.html')


if __name__ == '__main__':
    app.run()
