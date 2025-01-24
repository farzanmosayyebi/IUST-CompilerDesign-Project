class DeepDSLCodeGenerator:
    def __init__(self):
        self.non_operands = ['network','layer']
        self.operand_stack = []
        self.code_stack = []

    def generate_code(self, post_order_array):
        for item in post_order_array:
            if item in self.non_operands:
                self.generate_code_based_on_non_operand(item["label"])
            else:
                self.operand_stack.append(item["label"])

        result = ''
        for code in self.code_stack:
            if code is not None:
                result += code

        with open("output.txt", "w") as generated_output:
            generated_output.write(self.generate_code_import())
            generated_output.write(result)
        return result

    def generate_code_based_on_non_operand(self, item):
        return item

    @staticmethod
    def generate_code_import():
        result = ( "import tensorflow as tf\n"
                   "import numpy as np\n"
                   "import matplotlib.pyplot as plt\n"
                   "from tensorflow.keras.models import Sequential\n"
                   "from tensorflow.keras.layers import Flatten, Dense\n")
        return result

    def load_dataset(self):
        result = "(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()"


    def check_shape(self):
        result = ("print(\"Feature matrix (x_train):\", x_train.shape)\n"
                  "print(\"Target matrix (y_train):\", y_train.shape)\n"
                  "print(\"Feature matrix (x_test):\", x_test.shape)\n"
                  "print(\"Target matrix (y_test):\", y_test.shape)\n")