import keras_cv
import tensorflow as tf
from tensorflow import keras
import tensorflow_datasets as tfds

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

augmenter = keras_cv.layers.Augmenter(
  layers=[
      keras_cv.layers.RandomFlip(),
      keras_cv.layers.RandAugment(value_range=(0, 255)),
      keras_cv.layers.CutMix(),
      keras_cv.layers.MixUp()
    ]
)

def augment_data(images, labels):
  labels = tf.one_hot(labels, 3)
  inputs = {"images": images, "labels": labels}
  outputs = augmenter(inputs)
  return outputs['images'], outputs['labels']