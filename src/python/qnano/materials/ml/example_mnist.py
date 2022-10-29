"""MNIST pixel intensity data for images of a digit (0-9).

Each image is 28x28 pixels.
Train on 60k images.
Test on 10k images.

"""

# import numpy as np
import tensorflow as tf
from tensorflow import keras

EPOCHS = 200
BATCH_SIZE = 128
VERBOSE = 1
DIGIT_CLASSES = 10
N_HIDDEN = 128
VALIDATION_SPLIT = 0.2
NUM_PIXELS = 28
RESHAPED = NUM_PIXELS * NUM_PIXELS

mnist = keras.datasets.mnist
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

X_train = X_train.reshape(60000, RESHAPED).astype("float32")
X_test = X_test.reshape(10000, RESHAPED).astype("float32")

# Normalize to [0 ,1]
X_train /= 255
X_test /= 255

print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')

# One-hot representation of the labels
Y_train = tf.keras.utils.to_categorical(Y_train, DIGIT_CLASSES)
Y_test = tf.keras.utils.to_categorical(Y_test, DIGIT_CLASSES)


model = tf.keras.models.Sequential()

model.add(keras.layers.Dense(
    DIGIT_CLASSES,
    input_shape=(RESHAPED,),
    kernel_initializer='zeros',
    name='dense_layer',
    activation='softmax'))
