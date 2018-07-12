import numpy as np
from PIL import Image

from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions

import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

def process_img_path(img_path):
	return image.load_img(img_path, target_size=(224, 224))

def img_contains_banana(img):
	x = image.img_to_array(img)
	x = np.expand_dims(x, axis=0)
	x = preprocess_input(x)
	model = ResNet50(weights='imagenet')
	features = model.predict(x)
	results = decode_predictions(features, top=3)[0]
	for entry in results:
		if entry[1]=='banana':
			return entry[2]
	return 0.0

if __name__ == "__main__":
	test_path = "sample_data/positive_examples/example2.jpeg"
	test_img = process_img_path(test_path)
	test_result = img_contains_banana(test_img)
	print("Banana confidence = {}".format(test_result))