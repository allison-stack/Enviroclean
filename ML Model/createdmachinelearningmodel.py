# import the libraries into Python 
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import cv2
import matplotlib.pyplot as plt


base_dir = 'DATASET'
train_dir = os.path.join(base_dir, 'TRAIN')
test_dir = os.path.join(base_dir, 'TEST')

train_organic_dir = os.path.join(train_dir, 'O')
train_recycle_dir = os.path.join(train_dir, 'R')

test_organic_dir = os.path.join(test_dir, 'O')
test_recycle_dir = os.path.join(test_dir, 'R')

model = tf.keras.models.Sequential([

    tf.keras.layers.Conv2D(16, (3,3), activation='relu',input_shape=(150,150,3)),
    tf.keras.layers.MaxPooling2D(2,2),

    tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),

    tf.keras.layers.Flatten(),

    tf.keras.layers.Dense(512, activation='relu'),

    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer="adam",
              loss='binary_crossentropy',
              metrics = ['accuracy'])

# we rescale all our images with the rescale parameter
train_datagen = ImageDataGenerator(rescale = 1.0/255)
test_datagen  = ImageDataGenerator(rescale = 1.0/255)

# we use flow_from_directory to create a generator for training
train_generator = train_datagen.flow_from_directory(train_dir,
                                                    batch_size=20,
                                                    class_mode='binary',
                                                    target_size=(150, 150))

# we use flow_from_directory to create a generator for validation
test_generator =  test_datagen.flow_from_directory(test_dir,
                                                         batch_size=20,
                                                         class_mode='binary',
                                                         target_size=(150, 150))


history = model.fit(
            train_generator, # pass in the training generator
            steps_per_epoch=100,
            epochs=15,
            validation_data=test_generator, # pass in the validation generator
            validation_steps=50,
            verbose=2
            )

model.save("classified model")
