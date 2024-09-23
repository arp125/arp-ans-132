from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def register():
    return render_template("index.html")

if __name__ == "__main__":
    ip = "172.31.17.27"
    port = "80"
    app.run(ip, port)