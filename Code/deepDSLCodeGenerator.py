class DeepDSLCodeGenerator:
    def __init__(self):
        self.non_operands = []
        self.operand_stack = []
        self.code_stack = []


    def getImportHeader(self):
        result = ( "import tensorflow as tf\n"
                   "import numpy as np\n"
                   "import matplotlib.pyplot as plt\n"
                   "from tensorflow.keras.models import Sequential\n"
                   "from tensorflow.keras.layers import Flatten, Dense\n")
        return result