import json
import urllib3

#response data is a stream of bytes
response = urllib3.request("GET", 'https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt')

# The data is bytes → decode to string
data = response.data.decode('utf-8')

# Split by newlines to get a list of class names
class_list = data.strip().split('\n')
class_dict = {idx: name for idx, name in enumerate(class_list)}

with open("imagenet_class_idx.json", "w") as f:
    json.dump(class_dict, f, indent=4)