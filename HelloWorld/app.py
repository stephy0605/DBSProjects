from flask import Flask

app = Flask(__name__)

@app.route('/')
def green_screen():
    return '<html><body style="background-color: red; height: 100vh;"></body></html>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
