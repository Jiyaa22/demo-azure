from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hadoop UGDX rocks 🚀"

if __name__ == "__main__":
    app.run()