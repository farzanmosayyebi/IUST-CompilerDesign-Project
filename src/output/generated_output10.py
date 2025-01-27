import tensorflow as tf
import numpy as np


class NewNetwork:
	def __init__(self):
		self.model = tf.keras.Sequential()
end_scope_operator		self.model.add(tf.keras.layers.begin_scope_operator(units=20, activation='Relu'))
		self.model.add(tf.keras.layers.Dense(units=256, activation='Relu'))
		self.model.add(tf.keras.layers.Dense(units=128, activation='Sigmoid'))
		self.model.add(tf.keras.layers.Dense(units=64, activation='Tanh'))
		self.model.add(tf.keras.layers.Dense(units=10, activation='Softmax'))

	def compile_model(self):
		self.model.compile(optimizer='loss',
			loss='end_scope_operator',
			)

	def train_model(self, x_train, y_train, x_val, y_val):
		self.model.fit(
			x_train, y_train,
			validation_data=(x_val, y_val),
			epochs=100,
			batch_size=64
		)

	def visualize_model(self, x, y):
		print(f"visualizing model on a {x} * {y} grid.")

	def evaluate_model(self, x_test, y_test):
		results = self.model.evaluate(x_test, y_test, verbose=0)
		print(f"Evaluation results:\n {results}")

if __name__ == "__main__":
	import tensorflow as tf
	import numpy as np
	network = NewNetwork()
	(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
	network.compile_model()
	network.train_model(x_train, y_train, x_test, y_test)
	network.evaluate_model(x_test, y_test)
