from flask import Flask, request, jsonify
from src.inference import predict
import torch

app = Flask(__name__)
model = torch.load("models/finetuned/model.pth")
model.eval()

@app.route("/predict", methods=["POST"])
def predict_api():
    file = request.files['file']
    frame = np.array(file.read())
    result = predict(model, frame)
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
