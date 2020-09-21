from flask import Flask, request, jsonify
from model import SummarizationModel
import time

app = Flask(__name__)
model = SummarizationModel()


@app.route("/", methods=["GET"])
def method_name():
    return "Hello World!"


@app.route("/summarize", methods=["POST"])
def summarize():
    request_json = request.get_json(force=True)

    start_time = time.time()
    summary = model.summarize(text=request_json["text"])
    time_taken = time.time() - start_time

    text = request_json["text"]
    reduction = 1 - len(summary) / len(text)

    return (
        jsonify({"summary": summary, "time": time_taken, "reduction": reduction}),
        200,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")