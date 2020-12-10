import os
import re
import numpy as np
import pandas as pd

models = [
    "alexnet",
    "vgg11",
    "vgg16",
    "vgg19",
    "vgg11_bn",
    "vgg16_bn",
    "vgg19_bn",
    "resnet18",
    "resnet50",
    "resnet101",
    "resnet152",
    "squeezenet1_0",
    "densenet121",
    "densenet169",
    "densenet201",
    "mobilenet_v2",
    "resnext50_32x4d",
    "resnext101_32x8d"
]

lst = []
for model in models:
    file = model + ".log"
    if not os.path.exists(file):
        continue
    with open(file, "r") as f:
        content = f.read()
    items = re.findall("\d+\.\d+ MiB", content)
    items = [float(item.split()[0]) for item in items]
    lst.append(items)

df = pd.DataFrame(lst)
df.to_csv("all.csv", sep=',', index=False)

