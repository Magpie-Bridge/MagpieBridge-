# FCN
import tensorflow.keras as keras
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.layers import BatchNormalization, ZeroPadding2D
from tensorflow.keras.layers import LeakyReLU
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.models import Sequential
import numpy as np


class Classifier_FCN:
    def __init__(self, input_shape, nb_classes, output_directory):
        self.output_directory = output_directory
        self.input_shape = input_shape
        self.nb_classes = nb_classes
        self.model = self.build_model()

    def build_model(self):
        model = Sequential()
        model.add(Conv2D(128, kernel_size=3, strides=4,
                         input_shape=tuple(self.input_shape), padding="same"))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Conv2D(64, kernel_size=3, strides=4, padding="same"))
        model.add(ZeroPadding2D(padding=((0, 1), (0, 1))))
        model.add(BatchNormalization(momentum=0.8))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dropout(0.25))
        model.add(Conv2D(64, kernel_size=3, strides=4, padding="same"))
        model.add(ZeroPadding2D(padding=((0, 1), (0, 1))))
        model.add(BatchNormalization(momentum=0.8))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dropout(0.25))
        model.add(Conv2D(32, kernel_size=3, strides=2, padding="same"))
        model.add(BatchNormalization(momentum=0.8))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Conv2D(16, kernel_size=3, strides=1, padding="same"))
        model.add(BatchNormalization(momentum=0.8))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Flatten())
        model.add(Dense(self.nb_classes, activation='sigmoid'))
        model.summary()
        reduce_lr = keras.callbacks.ReduceLROnPlateau(
            monitor='loss', factor=0.5, patience=50, min_lr=0.0001)
        file_path = self.output_directory + 'best_model.hdf5'
        model_checkpoint = keras.callbacks.ModelCheckpoint(
            filepath=file_path, monitor='loss', save_best_only=True)
        self.callbacks = [reduce_lr, model_checkpoint]
        model.compile(loss='categorical_crossentropy',
                      optimizer=keras.optimizers.Adam(),
                      metrics=['accuracy'])
        return model

    def fit(self, x_train, y_train, batch, epochs):
        batch_size = batch
        nb_epochs = epochs
        self.model.fit(x_train, y_train, batch_size=batch_size,
                       epochs=nb_epochs, callbacks=self.callbacks)
        print('模型已保存到下面目录')
        print(self.output_directory + 'best_model.hdf5')

    def predict(self, x):
        y = self.model.predict(x)
        y = np.argmax(y, axis=1)
        return y

    def load_model(self, file_path):
        self.model = keras.models.load_model(file_path)
        self.model.summary()
        print("")
