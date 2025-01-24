class DeepDSLCodeGenerator:
    def __init__(self):
        self.non_operands = [
            'layer',
            'training',
            'visualize',
            'input_shape',
            'evaluate',
            'dataset',
        ]

        self.operand_stack = []
        self.code_stack = []
        self.shape_stack = []

    def is_operand(self, item):
        return item not in self.non_operands

    @staticmethod
    def generate_initial(self):
        imports = "import tensorflow as tf\n" + \
                  "import numpy as np\n"

        class_def = f"class NewNetwork:\n" + \
                    f"\tdef __init__(self):\n" + \
                    f"\t\tself.model = tf.keras.Sequential()\n"
        return imports + class_def

    def generate_code(self, post_order_array):
        for item in post_order_array:
            label = item["label"]
            if not self.is_operand(label):
                self.generate_code_based_on_non_operand(label)
            else:
                self.operand_stack.append(label)

        result = ''
        for code in self.code_stack:
            if code is not None:
                result += code

        with open("output.txt", "w") as f:
            f.write(self.generate_initial(self))
            f.write(result)
        return result

    def generate_code_based_on_non_operand(self, item):
        if item == "layer":
            self.generate_layer()
        elif item == "input_shape":
            self.generate_input_shape()

    def generate_input_shape(self):
        y = self.operand_stack.pop()
        x = self.operand_stack.pop()
        code_string = f"input_shape=({x}, {y})"
        self.shape_stack.append(code_string)

    def generate_layer(self):
        layer_activation = self.operand_stack.pop()
        layer_units = self.operand_stack.pop()
        layer_type = self.operand_stack.pop()

        layer_input_shape = ''
        if len(self.shape_stack) > 0:
            layer_input_shape = f', {self.shape_stack.pop()}'

        layer_def = f"\t\tself.model.add(tf.keras.layers.{layer_type}(units={layer_units}, activation=\'{layer_activation}\'{layer_input_shape}))\n"
        self.code_stack.append(layer_def)