from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is a CI/CD Pipeline with Kubernetes test. \n Im making changes too!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

