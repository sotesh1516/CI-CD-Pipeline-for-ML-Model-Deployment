from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import torch
import torchvision.models as models
import torchvision.transforms as transforms
import os, io

#Load pre-trained ResNet18
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
model.eval()

app = Flask(__name__)

CORS(app)

@app.route("/predict", methods=['POST'])
def predict():
    img_filestorage = request.files['image']
    img_stream = img_filestorage.stream #stream attribute behaves like a standard python object
    img = Image.open(img_stream).convert('RGB') #creates a PIL object
    transforms = transforms.ToTensor()
    img_tensor = transforms(img)
    print(type(img_tensor))

    print(img)

    return jsonify({"prediction": 20})


if __name__ == "__main__":
    app.run(debug=True, port=5000)