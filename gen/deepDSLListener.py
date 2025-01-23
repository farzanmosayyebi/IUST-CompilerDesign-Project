# Generated from D:/University/Compiler Design/git/IUST-CompilerDesign-Project/Grammar/deepDSL.g4 by ANTLR 4.13.2
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


    # Enter a parse tree produced by deepDSLParser#dataset.
    def enterDataset(self, ctx:deepDSLParser.DatasetContext):
        pass

    # Exit a parse tree produced by deepDSLParser#dataset.
    def exitDataset(self, ctx:deepDSLParser.DatasetContext):
        pass


    # Enter a parse tree produced by deepDSLParser#visualize.
    def enterVisualize(self, ctx:deepDSLParser.VisualizeContext):
        pass

    # Exit a parse tree produced by deepDSLParser#visualize.
    def exitVisualize(self, ctx:deepDSLParser.VisualizeContext):
        pass


    # Enter a parse tree produced by deepDSLParser#evaluate.
    def enterEvaluate(self, ctx:deepDSLParser.EvaluateContext):
        pass

    # Exit a parse tree produced by deepDSLParser#evaluate.
    def exitEvaluate(self, ctx:deepDSLParser.EvaluateContext):
        pass


    # Enter a parse tree produced by deepDSLParser#optimizer.
    def enterOptimizer(self, ctx:deepDSLParser.OptimizerContext):
        pass

    # Exit a parse tree produced by deepDSLParser#optimizer.
    def exitOptimizer(self, ctx:deepDSLParser.OptimizerContext):
        pass


    # Enter a parse tree produced by deepDSLParser#loss.
    def enterLoss(self, ctx:deepDSLParser.LossContext):
        pass

    # Exit a parse tree produced by deepDSLParser#loss.
    def exitLoss(self, ctx:deepDSLParser.LossContext):
        pass


    # Enter a parse tree produced by deepDSLParser#metric_choice.
    def enterMetric_choice(self, ctx:deepDSLParser.Metric_choiceContext):
        pass

    # Exit a parse tree produced by deepDSLParser#metric_choice.
    def exitMetric_choice(self, ctx:deepDSLParser.Metric_choiceContext):
        pass


    # Enter a parse tree produced by deepDSLParser#epochs.
    def enterEpochs(self, ctx:deepDSLParser.EpochsContext):
        pass

    # Exit a parse tree produced by deepDSLParser#epochs.
    def exitEpochs(self, ctx:deepDSLParser.EpochsContext):
        pass


    # Enter a parse tree produced by deepDSLParser#batch_size.
    def enterBatch_size(self, ctx:deepDSLParser.Batch_sizeContext):
        pass

    # Exit a parse tree produced by deepDSLParser#batch_size.
    def exitBatch_size(self, ctx:deepDSLParser.Batch_sizeContext):
        pass


    # Enter a parse tree produced by deepDSLParser#validation_split.
    def enterValidation_split(self, ctx:deepDSLParser.Validation_splitContext):
        pass

    # Exit a parse tree produced by deepDSLParser#validation_split.
    def exitValidation_split(self, ctx:deepDSLParser.Validation_splitContext):
        pass


    # Enter a parse tree produced by deepDSLParser#source.
    def enterSource(self, ctx:deepDSLParser.SourceContext):
        pass

    # Exit a parse tree produced by deepDSLParser#source.
    def exitSource(self, ctx:deepDSLParser.SourceContext):
        pass


    # Enter a parse tree produced by deepDSLParser#preprocessing.
    def enterPreprocessing(self, ctx:deepDSLParser.PreprocessingContext):
        pass

    # Exit a parse tree produced by deepDSLParser#preprocessing.
    def exitPreprocessing(self, ctx:deepDSLParser.PreprocessingContext):
        pass


    # Enter a parse tree produced by deepDSLParser#type.
    def enterType(self, ctx:deepDSLParser.TypeContext):
        pass

    # Exit a parse tree produced by deepDSLParser#type.
    def exitType(self, ctx:deepDSLParser.TypeContext):
        pass


    # Enter a parse tree produced by deepDSLParser#units.
    def enterUnits(self, ctx:deepDSLParser.UnitsContext):
        pass

    # Exit a parse tree produced by deepDSLParser#units.
    def exitUnits(self, ctx:deepDSLParser.UnitsContext):
        pass


    # Enter a parse tree produced by deepDSLParser#activation.
    def enterActivation(self, ctx:deepDSLParser.ActivationContext):
        pass

    # Exit a parse tree produced by deepDSLParser#activation.
    def exitActivation(self, ctx:deepDSLParser.ActivationContext):
        pass


    # Enter a parse tree produced by deepDSLParser#input_shape.
    def enterInput_shape(self, ctx:deepDSLParser.Input_shapeContext):
        pass

    # Exit a parse tree produced by deepDSLParser#input_shape.
    def exitInput_shape(self, ctx:deepDSLParser.Input_shapeContext):
        pass



del deepDSLParser