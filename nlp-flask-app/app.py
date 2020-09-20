from flask import Flask, request, jsonify
from model import SummarizationModel
import time

app = Flask(__name__)
model = SummarizationModel()


@app.route("/summarize", methods=["POST"])
def summarize():
    text = request.get_json()["text"]

    start_time = time.time()
    summary = model.summarize(text)
    time_taken = time.time() - start_time
    reduction = 1 - len(summary) / len(text)

    return (
        jsonify({"summary": summary, "time": time_taken, "reduction": reduction}),
        200,
    )


if __name__ == "__main__":
    app.run()