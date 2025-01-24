from Repository.ast import AST
from Repository.make_ast_subtree import make_ast_subtree
from gen.deepDSLListener import deepDSLListener
from gen.deepDSLParser import deepDSLParser


class DeepDSLCustomListener(deepDSLListener):
    def __init__(self, rule_names):
        self.overridden_rules = ['layer', 'types', 'units','training', 'activation',
                                 'visualize', 'input_shape', 'evaluate', 'metric_choice' ,'epochs',
                                 'dataset', 'source', 'preprocessing_func']
        self.rule_names = rule_names
        self.ast = AST()

    def exitEveryRule(self, ctx):
        rule_name = self.rule_names[ctx.getRuleIndex()]
        if rule_name not in self.overridden_rules:
            make_ast_subtree(self.ast, ctx, rule_name)

    def exitLayer(self, ctx):
        make_ast_subtree(self.ast, ctx, "layer", keep_node=True)

    def exitTypes(self, ctx):
        make_ast_subtree(self.ast, ctx,"types", keep_node=True)

    def exitUnits(self, ctx):
        make_ast_subtree(self.ast, ctx, "units", keep_node=True)

    def exitActivation(self, ctx):
        make_ast_subtree(self.ast, ctx, "activation", keep_node=True)

    def exitTraining(self, ctx):
        make_ast_subtree(self.ast, ctx, "training", keep_node=True)

    def exitVisualize(self, ctx):
        make_ast_subtree(self.ast, ctx, "visualize", keep_node=True)

    def exitInput_shape(self, ctx:deepDSLParser.Input_shapeContext):
        make_ast_subtree(self.ast, ctx, "input_shape", keep_node=True)

    def exitMetric_choice(self, ctx:deepDSLParser.Input_shapeContext):
        make_ast_subtree(self.ast, ctx, "metric_choice", keep_node=True)

    def exitDataset(self, ctx:deepDSLParser.Input_shapeContext):
        make_ast_subtree(self.ast, ctx, "dataset", keep_node=True)

    def exitSource(self, ctx:deepDSLParser.Input_shapeContext):
        make_ast_subtree(self.ast, ctx, "source", keep_node=True)

    def exitPreprocessing_func(self, ctx:deepDSLParser.Input_shapeContext):
        make_ast_subtree(self.ast, ctx, "preprocessing_func", keep_node=True)

    def exitEpochs(self,ctx):
        make_ast_subtree(self.ast, ctx, "epochs", keep_node=True)

    def exitEvaluate(self, ctx:deepDSLParser.EvaluateContext):
        make_ast_subtree(self.ast, ctx, "evaluate", keep_node=True)

