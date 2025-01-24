class DeepDSLCodeGenerator:
    def __init__(self):
        self.non_operands = ['network', 'layer', 'training', 'dataset', 'visualize', 'evaluate']
        self.operand_stack = []
        self.code_stack = []

    def generate_code(self, post_order_array):
        for item in post_order_array:
            if item in self.non_operands:
                self.code_stack.append(self.generate_code_based_on_non_operand(item["label"]))
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
        if item == "network":
            self.generate_network()
        elif item == "layer":
            self.generate_layer()
        elif item == "training":
            self.generate_training()
        elif item == "dataset":
            self.generate_load_dataset()
        elif item == "visualize":
            self.generate_visualize()
        elif item == "evaluate":
            self.generate_evaluate()

    @staticmethod
    def generate_code_import():
        result = ( "import tensorflow as tf\n"
                   "import numpy as np\n"
                   "import matplotlib.pyplot as plt\n"
                   "from tensorflow.keras.models import Sequential\n"
                   "from tensorflow.keras.layers import Flatten, Dense\n")
        return result

    def generate_load_dataset(self):
        result = "(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()"
        return result


    @staticmethod
    def generate_check_shape(self):
        result = ("print(\"Feature matrix (x_train):\", x_train.shape)\n"
                  "print(\"Target matrix (y_train):\", y_train.shape)\n"
                  "print(\"Feature matrix (x_test):\", x_test.shape)\n"
                  "print(\"Target matrix (y_test):\", y_test.shape)\n")
        return result

    def generate_network(self):
        result = f"model = Sequential({self.generate_layer()})\n"
        return result

    def generate_layer(self):
        layer_type = self.operand_stack.pop()
        units = self.operand_stack.pop()
        activation = self.operand_stack.pop()
        input_shape = self.operand_stack.pop() if layer_type == "Dense" else None
        result = ''

        if input_shape:
            result += f"model.add(Dense({units}, activation='{activation}', input_shape={input_shape}))\n"
        else:
            result += f"model.add({layer_type}({units}, activation='{activation}'))\n"

        return result

    def generate_training(self):
        optimizer = self.operand_stack.pop()
        loss = self.operand_stack.pop()
        metrics = self.operand_stack.pop()
        epochs = self.operand_stack.pop()
        batch_size = self.operand_stack.pop()

        result = ''
        result += f"model.compile(optimizer='{optimizer}', loss='{loss}', metrics={metrics})\n"
        result += f"model.fit(x_train, y_train, epochs={epochs}, batch_size={batch_size})\n"

        return result

    def generate_visualize(self):
        return ''

    def generate_evaluate(self):
        result = "model.evaluate(x_test, y_test)\n"
        return result
