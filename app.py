from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    """ Return a friendly HTTP greeting. """
    who = request.args.get("who", "World")
    return f"Hello test from repo 2 {who}!\n"


if __name__ == "__main__":
    # Used when running locally only. When deploying to Cloud Run,
    # a webserver process such as Gunicorn will serve the app.
    app.run(host="localhost", port=8080, debug=True)