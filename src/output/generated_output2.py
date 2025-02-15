import tensorflow as tf
import numpy as np


class NewNetwork:
	def __init__(self):
		self.model = tf.keras.Sequential()
		self.model.add(tf.keras.layers.Dense(units=512, activation='Relu', input_shape=(64,64,)))
		self.model.add(tf.keras.layers.Dense(units=256, activation='Tanh'))
		self.model.add(tf.keras.layers.Dense(units=128, activation='Sigmoid'))
		self.model.add(tf.keras.layers.Dense(units=5, activation='Softmax'))

	def compile_model(self):
		self.model.compile(optimizer='sgd',
			loss='MeanSquaredError',
			metrics = ['loss'])

	def train_model(self, x_train, y_train, x_val, y_val):
		self.model.fit(
			x_train, y_train,
			validation_data=(x_val, y_val),
			epochs=50,
			batch_size=16
		)

	def generate_dataset(self):
		(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
		return x_train, x_train, y_train, y_test 

	def visualize_model(self, x, y):
		print(f"visualizing model on a {x} * {y} grid.")

	def evaluate_model(self, x_test, y_test):
		results = self.model.evaluate(x_test, y_test, verbose=0)
		print(f"Evaluation results:\n {results}")

if __name__ == "__main__":
	network = NewNetwork()
	x_train, x_test, y_train, y_test = network.generate_dataset()
	network.compile_model()
	network.train_model(x_train, y_train, x_test, y_test)
	network.evaluate_model(x_test, y_test)
