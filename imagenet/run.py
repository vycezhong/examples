import os

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
bzs = [8]

for model in models:
    file = "logs/" + model + ".log"
    for bz in bzs:
        print(model, bz)
        try:
            os.system(
                "python main.py -a %s -b %d --gpu 0 /data2/ILSVRC2012 2>/dev/null >> %s" % (model, bz, file))
        except:
            print("OOM")
