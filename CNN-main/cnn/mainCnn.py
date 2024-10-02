import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPool2D, Dropout
from tensorflow.keras.models import Sequential
import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np
from typing import Tuple


train_images_dir = "assets\Training"
val_images_dir = "assets\Testing"

DirectoryIterator = keras.preprocessing.image.DirectoryIterator

def get_images(dir: str) -> DirectoryIterator:
    images_dir = dir

    datagen = ImageDataGenerator(rescale=1./255, validation_split=0.3)

    batch_size = 16
    img_height = 128
    img_width = 128

    dataset = datagen.flow_from_directory(
        images_dir,
        target_size=(img_height, img_width),
        batch_size=batch_size,
        class_mode='categorical',
        shuffle=True,
    )

train_data = get_images(train_images_dir)
val_data = get_images(val_images_dir)

tf.random.set_seed(113)

model = Sequential([
    Conv2D(input_shape=(128, 128, 3), filters=32, kernel_size=(3, 3), activation='relu', padding='same'),
    MaxPool2D(pool_size=(2, 2), strides=2),
    Conv2D(filters=32, kernel_size=(3, 3), activation='relu', padding='same'),
    MaxPool2D(pool_size=(2, 2), strides=2),
    Conv2D(filters=64, kernel_size=(3, 3), activation='relu', padding='same'),
    MaxPool2D(pool_size=(2, 2), strides=2),
    Flatten(),
    Dense(units=64, activation='relu'),
    Dropout(rate=0.2),
    Dense(units=4, activation='softmax')
])


model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.001), loss=keras.losses.categorical_crossentropy, metrics=['accuracy'])

history = model.fit(x=train_data, validation_data=val_data, steps_per_epoch=20,
    epochs=800, validation_steps=100, verbose=1)

def plot_training_history(history, figsize=(12, 4)):
    # Plot training & validation accuracy values
    plt.figure(figsize=figsize)

    # Accuracy
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='Train Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.title('Model Accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(loc='upper left')

    # Loss
    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='Train Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.title('Model Loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(loc='upper left')

    plt.show()
plot_training_history(history)

model.save('modelo.keras')