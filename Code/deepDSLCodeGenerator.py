class DeepDSLCodeGenerator:
    def __init__(self):
        self.non_operands = []
        self.operand_stack = []
        self.code_stack = []
