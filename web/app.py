from flask import Flask, send_from_directory, render_template
app = Flask(__name__, static_url_path='', static_folder="../web")



@app.route("/", defaults={'path':''})
def home(path):
    return send_from_directory("", "index.html")
    # return render_template("index.html")

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run( debug=True)