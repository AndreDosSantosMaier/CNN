import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dropout, Dense, Flatten, MaxPooling2D, Conv2D
from tensorflow.keras.models import Sequential

# Inicializando a CNN
np.random.seed(1337)
classifier = Sequential()

classifier.add(Conv2D(32, (3, 3), input_shape=(128, 128, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))
classifier.add(Conv2D(16, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))
classifier.add(Conv2D(8, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))

classifier.add(Flatten())

# Camada oculta
classifier.add(Dense(units=128, activation='relu'))
classifier.add(Dropout(0.5))

# Camada de saída
classifier.add(Dense(units=10, activation='softmax'))

classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
print(classifier.summary())

# Part 2 - Ajustando o conjunto de dados
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
    r'E:\Downloads\kaggle\tomato\train',
    target_size=(128, 128),
    batch_size=64,
    class_mode='categorical')
label_map = (training_set.class_indices)

print(label_map)

test_set = test_datagen.flow_from_directory(
    r'E:\Downloads\kaggle\tomato\val',
    target_size=(128, 128),
    batch_size=64,
    class_mode='categorical')

classifier.fit(
    training_set,
    steps_per_epoch=20,
    epochs=800,
    validation_data=test_set,
    validation_steps=100)

# Save the entire model, not just the weights
model_path = './model/keras_potato_trained_model.h5'
classifier.save(model_path)
print(f'Saved trained model as {model_path}')
