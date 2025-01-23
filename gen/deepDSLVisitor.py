# Generated from D:/University/Compiler Design/DeepDSL/Grammar/deepDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .deepDSLParser import deepDSLParser
else:
    from deepDSLParser import deepDSLParser

# This class defines a complete generic visitor for a parse tree produced by deepDSLParser.

class deepDSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by deepDSLParser#network.
    def visitNetwork(self, ctx:deepDSLParser.NetworkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deepDSLParser#layer.
    def visitLayer(self, ctx:deepDSLParser.LayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deepDSLParser#training.
    def visitTraining(self, ctx:deepDSLParser.TrainingContext):
        return self.visitChildren(ctx)



del deepDSLParser