import os
import pickle
import argparse
import pandas as pd
import torch
from PIL import Image
from torchvision import models, transforms

modelPool = ["vgg16", "vgg19", "resnet18", "regnetx8"]
label_url = 'https://s3.amazonaws.com/deep-learning-models/image-models/imagenet_class_index.json'


def downloadModel(model_name, model_path):
    print("Downloading model:")
    if model_name == "vgg16":
        pickle.dump(models.vgg16(weights=models.VGG16_Weights).eval(), open(model_path, "wb"))
    if model_name == "vgg19":
        pickle.dump(models.vgg19(weights=models.VGG19_BN_Weights).eval(), open(model_path, "wb"))
    if model_name == "resnet18":
        pickle.dump(models.resnet18(weights=models.ResNeXt50_32X4D_Weights).eval(), open(model_path, "wb"))
    if model_name == "regnetx8":
        pickle.dump(models.regnet_x_8gf(weights=models.RegNet_X_8GF_Weights).eval(), open(model_path, "wb"))

class IRNode:
    def __init__(self, model_name, dir):
        if model_name in modelPool:
            if not os.path.exists(dir):
                os.mkdir(dir)
            model_path = os.path.join(dir, model_name + ".dat")
            if not os.path.exists(model_path):
                downloadModel(model_name, model_path)
            self.model = pickle.load(open(model_path, "rb"))
        else:
            self.model = None
            
    def preprocessImage(self, image):
        tmp_image = image.convert("RGB")
        preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        return preprocess(tmp_image).unsqueeze(0)

    def predict(self, image):
        if image is None:
            return None
        if self.model is None:
            return None
        imagenet_df = pd.read_json(label_url).T
        output = self.model(self.preprocessImage(image))
        output_prob = torch.nn.functional.softmax(output[0], dim=0)
        index = int(torch.argmax(output_prob))
        return imagenet_df.iloc[index][1]

