from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import torch
import torchvision.models as models
import torchvision.transforms as transforms
import os, io

from imagenet_class_idx import imageNet


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
    transform_img_to_tensor = transforms.ToTensor()
    img_tensor = transform_img_to_tensor(img)
    img_tensor = img_tensor.unsqueeze(0) #insert a new dimension of size 1 at position(dim) in the arg provided
    output = model(img_tensor)
    max_val, predicted_idx = torch.max(output, 1)
    print(predicted_idx)

    return jsonify({"prediction": imageNet[str(predicted_idx.item())]})


if __name__ == "__main__":
    app.run(debug=True, port=5000)