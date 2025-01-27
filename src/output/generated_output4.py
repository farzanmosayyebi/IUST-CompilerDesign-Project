import tensorflow as tf
import numpy as np


class NewNetwork:
	def __init__(self):
		self.model = tf.keras.Sequential()
end_scope_operator		self.model.add(tf.keras.layers.begin_scope_operator(units=10, activation='Tanh'))
		self.model.add(tf.keras.layers.Dense(units=1, activation='Linear'))

	def compile_model(self):
		self.model.compile(optimizer='loss',
			loss='end_scope_operator',
			)

	def train_model(self, x_train, y_train, x_val, y_val):
		self.model.fit(
			x_train, y_train,
			validation_data=(x_val, y_val),
			epochs=100,
			batch_size=32
		)

	def generate_dataset(self):
		(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
		return x_train, x_train, y_train, y_test 

if __name__ == "__main__":
	import tensorflow as tf
	import numpy as np
	network = NewNetwork()
	x_train, x_test, y_train, y_test = network.generate_dataset()
	network.compile_model()
	network.train_model(x_train, y_train, x_test, y_test)
