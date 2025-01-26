import tensorflow as tf
import numpy as np


class NewNetwork:
	def __init__(self):
		self.model = tf.keras.Sequential()
		self.model.add(tf.keras.layers.Dense(units=512, activation='Relu', input_shape=(64, 64)))
		self.model.add(tf.keras.layers.Dense(units=256, activation='Tanh'))
		self.model.add(tf.keras.layers.Dense(units=128, activation='Sigmoid'))
		self.model.add(tf.keras.layers.Dense(units=5, activation='Softmax'))

	def compile_model(self):
		self.model.compile(optimizer='loss',
			loss='end_scope_operator',
			)

	def train_model(self, x_train, y_train, x_val, y_val):
		self.model.fit(
			x_train, y_train,
			validation_data=(x_val, y_val),
			epochs=50,
			batch_size=16
		)
