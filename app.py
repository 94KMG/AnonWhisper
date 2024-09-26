from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "익명 대화의 미로에 오신 것을 환영합니다!"

if __name__ == '__main__':
    app.run(debug=True)
