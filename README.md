# State Farm Distracted Driver Classification
## Satchel Grant

### Overview
This was a project using TensorFlow to recognize and classify distracted drivers from the [State Farm Distracted Driver Dataset](https://www.kaggle.com/c/state-farm-distracted-driver-detection) on Kaggle.


The [notebook](./driver_classification.html) is designed to be readable and understandable. I recommend any viewers open the notebook using jupyter or open the html of the notebook in their browsers.

### Preprocessing Steps

To preprocess the images, I reduced their pixel resolution for quicker training and reduced memory consumption. I then normalized and centered the images for improved training speeds and accuracy.

### Model Architecture

The final model architecture was inspired by both the LeNet and Inception Net models. It consisted of a convolution neural network with the following layers and layer sizes:

| Layer         		|     Description	        					|
|:---------------------:|:---------------------------------------------:|
| Input         		| 120x120x3 image   							|
| Convolution 1x1, 3x3, 5x5     	| 1x1 stride, same padding, depth 6, outputs 120x120x18 	|
| ELU					|												|
| Max pooling 2x2	      	| 2x2 stride,  outputs 60x60x18 				|
| Convolution 1x1, 3x3, 5x5     	| 1x1 stride, same padding, depth 8, outputs 60x60x24 	|
| ELU					|												|
| Max pooling 2x2	      	| 2x2 stride,  outputs 30x30x24 				|
| Convolution 1x1, 3x3, 5x5     	| 1x1 stride, same padding, depth 8, outputs 30x30x24 	|
| ELU					|												|
| Max pooling 2x2	      	| 2x2 stride,  outputs 15x15x24 				|
| Dropout	      	| 0.5 probability 				|
| Fully connected		| 5400x100, outputs x100        									|
| ELU					|												|
| Fully connected		| 100x10, outputs x10        									|
