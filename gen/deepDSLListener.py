# Generated from D:/University/Compiler Design/DeepDSL/Grammar/deepDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .deepDSLParser import deepDSLParser
else:
    from deepDSLParser import deepDSLParser

# This class defines a complete listener for a parse tree produced by deepDSLParser.
class deepDSLListener(ParseTreeListener):

    # Enter a parse tree produced by deepDSLParser#network.
    def enterNetwork(self, ctx:deepDSLParser.NetworkContext):
        pass

    # Exit a parse tree produced by deepDSLParser#network.
    def exitNetwork(self, ctx:deepDSLParser.NetworkContext):
        pass


    # Enter a parse tree produced by deepDSLParser#layer.
    def enterLayer(self, ctx:deepDSLParser.LayerContext):
        pass

    # Exit a parse tree produced by deepDSLParser#layer.
    def exitLayer(self, ctx:deepDSLParser.LayerContext):
        pass


    # Enter a parse tree produced by deepDSLParser#training.
    def enterTraining(self, ctx:deepDSLParser.TrainingContext):
        pass

    # Exit a parse tree produced by deepDSLParser#training.
    def exitTraining(self, ctx:deepDSLParser.TrainingContext):
        pass



del deepDSLParser