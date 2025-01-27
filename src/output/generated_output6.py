import tensorflow as tf
import numpy as np


class NewNetwork:
	def __init__(self):
		self.model = tf.keras.Sequential()
end_scope_operator		self.model.add(tf.keras.layers.begin_scope_operator(units=16, activation='Relu'))
		self.model.add(tf.keras.layers.Dense(units=4, activation='Softmax'))

	def compile_model(self):
		self.model.compile(optimizer='loss',
			loss='end_scope_operator',
			)

	def train_model(self, x_train, y_train, x_val, y_val):
		self.model.fit(
			x_train, y_train,
			validation_data=(x_val, y_val),
			epochs=10,
			batch_size=8
		)

if __name__ == "__main__":
	import tensorflow as tf
	import numpy as np
	network = NewNetwork()
	(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
	network.compile_model()
	network.train_model(x_train, y_train, x_test, y_test)
