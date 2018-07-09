This is a very simple implementation of object detection and localization, built using pretrained keras archs and basic image manipulation. The intended audience is students in Lambda School's machine learning course. The project proceeds in three steps:

1. Build a function that takes in an image, resizes it to 196x196, and returns a float describing the confidence with which Keras believes the image contains a dog. Do this using the Keras pretrained ResNet50 architecture.

2. Build a function that takes in an image and a parameter in ["TL", "TR", "BL", "BR"] and returns the top left 2/3 x 2/3, the top left, the top right, the bottom left, or the bottom right, depending on the parameter value. To visualize this partitioning, imagine that we lay a tic tac toe board over the image. Then the TL partition corresponds to the roughly 67% of the image lying in the top-left-most four squares.

3. Approximately locates the dog in the photo by checking whether the or


For reference on ResNet50, see https://www.pyimagesearch.com/2017/03/20/imagenet-vggnet-resnet-inception-xception-keras/. 

For example usage, see https://keras.io/applications/.

This material was made under an MIT License. All images are borrowed freely from Wikipedia.