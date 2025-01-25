import tensorflow as tf
import numpy as np


class NewNetwork:
	def __init__(self):
		self.model = tf.keras.Sequential()
		self.model.add(tf.keras.layers.Dense(units=256, activation='Relu', input_shape=(28, 28)))
		self.model.add(tf.keras.layers.Dense(units=128, input_shape=(28, 28)))
		self.model.add(tf.keras.layers.Dense(units=10, activation='Softmax'))

	def compile_model(self):
		self.model.compile(optimizer='adam',
			loss='SparseCategoricalCrossentropy',
			metrics = ['loss','accuracy'])

	def train_model(self, x_train, y_train, x_val, y_val):
		self.model.fit(
			x_train, y_train,
			validation_data=(x_val, y_val),
			epochs=10,
			batch_size=32
		)
