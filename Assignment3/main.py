from flask import Flask, render_template, request
from elasticsearch import Elasticsearch
import json

from pip._vendor import requests

app = Flask(__name__)
es = Elasticsearch()


@app.route('/', methods=["GET", "POST"])
def index():
    q = request.form.get("q")

    if q is not None:
        resp = es.search(index='shop', body={"query": {"match": {"master_pi": q}}})
        return render_template("index.html", q=q,response= resp)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port=8000)

