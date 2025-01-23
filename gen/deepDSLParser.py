# Generated from D:/University/Compiler Design/git/IUST-CompilerDesign-Project/Grammar/deepDSL.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,38,194,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,1,0,4,0,41,8,
        0,11,0,12,0,42,1,0,1,0,3,0,47,8,0,1,0,3,0,50,8,0,1,0,3,0,53,8,0,
        1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,63,8,1,1,1,3,1,66,8,1,1,1,1,
        1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,5,5,107,8,5,10,5,12,5,110,9,5,1,5,1,5,1,5,
        1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,
        1,8,5,8,132,8,8,10,8,12,8,135,9,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,
        9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,
        12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,
        15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,
        17,1,17,1,17,5,17,186,8,17,10,17,12,17,189,9,17,1,17,1,17,1,17,1,
        17,0,0,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,0,184,
        0,36,1,0,0,0,2,56,1,0,0,0,4,69,1,0,0,0,6,79,1,0,0,0,8,86,1,0,0,0,
        10,98,1,0,0,0,12,115,1,0,0,0,14,120,1,0,0,0,16,125,1,0,0,0,18,139,
        1,0,0,0,20,144,1,0,0,0,22,149,1,0,0,0,24,154,1,0,0,0,26,159,1,0,
        0,0,28,164,1,0,0,0,30,169,1,0,0,0,32,174,1,0,0,0,34,179,1,0,0,0,
        36,37,5,1,0,0,37,38,5,28,0,0,38,40,5,2,0,0,39,41,3,2,1,0,40,39,1,
        0,0,0,41,42,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,44,1,0,0,0,44,
        46,3,4,2,0,45,47,3,6,3,0,46,45,1,0,0,0,46,47,1,0,0,0,47,49,1,0,0,
        0,48,50,3,8,4,0,49,48,1,0,0,0,49,50,1,0,0,0,50,52,1,0,0,0,51,53,
        3,10,5,0,52,51,1,0,0,0,52,53,1,0,0,0,53,54,1,0,0,0,54,55,5,3,0,0,
        55,1,1,0,0,0,56,57,5,4,0,0,57,58,5,28,0,0,58,59,5,2,0,0,59,60,3,
        28,14,0,60,62,3,30,15,0,61,63,3,32,16,0,62,61,1,0,0,0,62,63,1,0,
        0,0,63,65,1,0,0,0,64,66,3,34,17,0,65,64,1,0,0,0,65,66,1,0,0,0,66,
        67,1,0,0,0,67,68,5,3,0,0,68,3,1,0,0,0,69,70,5,5,0,0,70,71,5,2,0,
        0,71,72,3,12,6,0,72,73,3,14,7,0,73,74,3,16,8,0,74,75,3,18,9,0,75,
        76,3,20,10,0,76,77,3,22,11,0,77,78,5,3,0,0,78,5,1,0,0,0,79,80,5,
        6,0,0,80,81,5,28,0,0,81,82,5,2,0,0,82,83,3,24,12,0,83,84,3,26,13,
        0,84,85,5,3,0,0,85,7,1,0,0,0,86,87,5,7,0,0,87,88,5,2,0,0,88,89,5,
        8,0,0,89,90,5,9,0,0,90,91,5,10,0,0,91,92,5,34,0,0,92,93,5,11,0,0,
        93,94,5,34,0,0,94,95,5,12,0,0,95,96,5,13,0,0,96,97,5,3,0,0,97,9,
        1,0,0,0,98,99,5,14,0,0,99,100,5,2,0,0,100,101,5,15,0,0,101,102,5,
        9,0,0,102,103,5,10,0,0,103,108,5,33,0,0,104,105,5,11,0,0,105,107,
        5,33,0,0,106,104,1,0,0,0,107,110,1,0,0,0,108,106,1,0,0,0,108,109,
        1,0,0,0,109,111,1,0,0,0,110,108,1,0,0,0,111,112,5,12,0,0,112,113,
        5,13,0,0,113,114,5,3,0,0,114,11,1,0,0,0,115,116,5,16,0,0,116,117,
        5,9,0,0,117,118,5,31,0,0,118,119,5,13,0,0,119,13,1,0,0,0,120,121,
        5,17,0,0,121,122,5,9,0,0,122,123,5,32,0,0,123,124,5,13,0,0,124,15,
        1,0,0,0,125,126,5,15,0,0,126,127,5,9,0,0,127,128,5,10,0,0,128,133,
        5,33,0,0,129,130,5,11,0,0,130,132,5,33,0,0,131,129,1,0,0,0,132,135,
        1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,136,1,0,0,0,135,133,
        1,0,0,0,136,137,5,12,0,0,137,138,5,13,0,0,138,17,1,0,0,0,139,140,
        5,18,0,0,140,141,5,9,0,0,141,142,5,34,0,0,142,143,5,13,0,0,143,19,
        1,0,0,0,144,145,5,19,0,0,145,146,5,9,0,0,146,147,5,34,0,0,147,148,
        5,13,0,0,148,21,1,0,0,0,149,150,5,20,0,0,150,151,5,9,0,0,151,152,
        5,35,0,0,152,153,5,13,0,0,153,23,1,0,0,0,154,155,5,21,0,0,155,156,
        5,9,0,0,156,157,5,36,0,0,157,158,5,13,0,0,158,25,1,0,0,0,159,160,
        5,22,0,0,160,161,5,9,0,0,161,162,5,27,0,0,162,163,5,13,0,0,163,27,
        1,0,0,0,164,165,5,23,0,0,165,166,5,9,0,0,166,167,5,29,0,0,167,168,
        5,13,0,0,168,29,1,0,0,0,169,170,5,24,0,0,170,171,5,9,0,0,171,172,
        5,34,0,0,172,173,5,13,0,0,173,31,1,0,0,0,174,175,5,25,0,0,175,176,
        5,9,0,0,176,177,5,30,0,0,177,178,5,13,0,0,178,33,1,0,0,0,179,180,
        5,26,0,0,180,181,5,9,0,0,181,182,5,10,0,0,182,187,5,34,0,0,183,184,
        5,11,0,0,184,186,5,34,0,0,185,183,1,0,0,0,186,189,1,0,0,0,187,185,
        1,0,0,0,187,188,1,0,0,0,188,190,1,0,0,0,189,187,1,0,0,0,190,191,
        5,12,0,0,191,192,5,13,0,0,192,35,1,0,0,0,9,42,46,49,52,62,65,108,
        133,187
    ]

class deepDSLParser ( Parser ):

    grammarFileName = "deepDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'network'", "'{'", "'}'", "'layer'", 
                     "'training'", "'dataset'", "'visualize'", "'grid'", 
                     "':'", "'['", "','", "']'", "';'", "'evaluate'", "'metrics'", 
                     "'optimizer'", "'loss'", "'epochs'", "'batch_size'", 
                     "'validation_split'", "'source'", "'preprocessing'", 
                     "'type'", "'units'", "'activation'", "'input_shape'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "PREPROCESSING_FN", 
                      "ID", "LAYER_TYPE", "ACTIVATION_FN", "OPTIMIZER", 
                      "LOSS_FN", "METRICS", "INT", "FLOAT", "STRING", "WS", 
                      "COMMENT" ]

    RULE_network = 0
    RULE_layer = 1
    RULE_training = 2
    RULE_dataset = 3
    RULE_visualize = 4
    RULE_evaluate = 5
    RULE_optimizer = 6
    RULE_loss = 7
    RULE_metric_choice = 8
    RULE_epochs = 9
    RULE_batch_size = 10
    RULE_validation_split = 11
    RULE_source = 12
    RULE_preprocessing = 13
    RULE_type = 14
    RULE_units = 15
    RULE_activation = 16
    RULE_input_shape = 17

    ruleNames =  [ "network", "layer", "training", "dataset", "visualize", 
                   "evaluate", "optimizer", "loss", "metric_choice", "epochs", 
                   "batch_size", "validation_split", "source", "preprocessing", 
                   "type", "units", "activation", "input_shape" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    PREPROCESSING_FN=27
    ID=28
    LAYER_TYPE=29
    ACTIVATION_FN=30
    OPTIMIZER=31
    LOSS_FN=32
    METRICS=33
    INT=34
    FLOAT=35
    STRING=36
    WS=37
    COMMENT=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class NetworkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(deepDSLParser.ID, 0)

        def training(self):
            return self.getTypedRuleContext(deepDSLParser.TrainingContext,0)


        def layer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(deepDSLParser.LayerContext)
            else:
                return self.getTypedRuleContext(deepDSLParser.LayerContext,i)


        def dataset(self):
            return self.getTypedRuleContext(deepDSLParser.DatasetContext,0)


        def visualize(self):
            return self.getTypedRuleContext(deepDSLParser.VisualizeContext,0)


        def evaluate(self):
            return self.getTypedRuleContext(deepDSLParser.EvaluateContext,0)


        def getRuleIndex(self):
            return deepDSLParser.RULE_network

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNetwork" ):
                listener.enterNetwork(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNetwork" ):
                listener.exitNetwork(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNetwork" ):
                return visitor.visitNetwork(self)
            else:
                return visitor.visitChildren(self)




    def network(self):

        localctx = deepDSLParser.NetworkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_network)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(deepDSLParser.T__0)
            self.state = 37
            self.match(deepDSLParser.ID)
            self.state = 38
            self.match(deepDSLParser.T__1)
            self.state = 40 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 39
                self.layer()
                self.state = 42 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==4):
                    break

            self.state = 44
            self.training()
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 45
                self.dataset()


            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 48
                self.visualize()


            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 51
                self.evaluate()


            self.state = 54
            self.match(deepDSLParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LayerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(deepDSLParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(deepDSLParser.TypeContext,0)


        def units(self):
            return self.getTypedRuleContext(deepDSLParser.UnitsContext,0)


        def activation(self):
            return self.getTypedRuleContext(deepDSLParser.ActivationContext,0)


        def input_shape(self):
            return self.getTypedRuleContext(deepDSLParser.Input_shapeContext,0)


        def getRuleIndex(self):
            return deepDSLParser.RULE_layer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLayer" ):
                listener.enterLayer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLayer" ):
                listener.exitLayer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLayer" ):
                return visitor.visitLayer(self)
            else:
                return visitor.visitChildren(self)




    def layer(self):

        localctx = deepDSLParser.LayerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_layer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(deepDSLParser.T__3)
            self.state = 57
            self.match(deepDSLParser.ID)
            self.state = 58
            self.match(deepDSLParser.T__1)
            self.state = 59
            self.type_()
            self.state = 60
            self.units()
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 61
                self.activation()


            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 64
                self.input_shape()


            self.state = 67
            self.match(deepDSLParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TrainingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def optimizer(self):
            return self.getTypedRuleContext(deepDSLParser.OptimizerContext,0)


        def loss(self):
            return self.getTypedRuleContext(deepDSLParser.LossContext,0)


        def metric_choice(self):
            return self.getTypedRuleContext(deepDSLParser.Metric_choiceContext,0)


        def epochs(self):
            return self.getTypedRuleContext(deepDSLParser.EpochsContext,0)


        def batch_size(self):
            return self.getTypedRuleContext(deepDSLParser.Batch_sizeContext,0)


        def validation_split(self):
            return self.getTypedRuleContext(deepDSLParser.Validation_splitContext,0)


        def getRuleIndex(self):
            return deepDSLParser.RULE_training

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTraining" ):
                listener.enterTraining(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTraining" ):
                listener.exitTraining(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTraining" ):
                return visitor.visitTraining(self)
            else:
                return visitor.visitChildren(self)




    def training(self):

        localctx = deepDSLParser.TrainingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_training)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(deepDSLParser.T__4)
            self.state = 70
            self.match(deepDSLParser.T__1)
            self.state = 71
            self.optimizer()
            self.state = 72
            self.loss()
            self.state = 73
            self.metric_choice()
            self.state = 74
            self.epochs()
            self.state = 75
            self.batch_size()
            self.state = 76
            self.validation_split()
            self.state = 77
            self.match(deepDSLParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DatasetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(deepDSLParser.ID, 0)

        def source(self):
            return self.getTypedRuleContext(deepDSLParser.SourceContext,0)


        def preprocessing(self):
            return self.getTypedRuleContext(deepDSLParser.PreprocessingContext,0)


        def getRuleIndex(self):
            return deepDSLParser.RULE_dataset

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataset" ):
                listener.enterDataset(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataset" ):
                listener.exitDataset(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataset" ):
                return visitor.visitDataset(self)
            else:
                return visitor.visitChildren(self)




    def dataset(self):

        localctx = deepDSLParser.DatasetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_dataset)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(deepDSLParser.T__5)
            self.state = 80
            self.match(deepDSLParser.ID)
            self.state = 81
            self.match(deepDSLParser.T__1)
            self.state = 82
            self.source()
            self.state = 83
            self.preprocessing()
            self.state = 84
            self.match(deepDSLParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VisualizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(deepDSLParser.INT)
            else:
                return self.getToken(deepDSLParser.INT, i)

        def getRuleIndex(self):
            return deepDSLParser.RULE_visualize

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVisualize" ):
                listener.enterVisualize(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVisualize" ):
                listener.exitVisualize(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVisualize" ):
                return visitor.visitVisualize(self)
            else:
                return visitor.visitChildren(self)




    def visualize(self):

        localctx = deepDSLParser.VisualizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_visualize)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(deepDSLParser.T__6)
            self.state = 87
            self.match(deepDSLParser.T__1)
            self.state = 88
            self.match(deepDSLParser.T__7)
            self.state = 89
            self.match(deepDSLParser.T__8)
            self.state = 90
            self.match(deepDSLParser.T__9)
            self.state = 91
            self.match(deepDSLParser.INT)
            self.state = 92
            self.match(deepDSLParser.T__10)
            self.state = 93
            self.match(deepDSLParser.INT)
            self.state = 94
            self.match(deepDSLParser.T__11)
            self.state = 95
            self.match(deepDSLParser.T__12)
            self.state = 96
            self.match(deepDSLParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EvaluateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def METRICS(self, i:int=None):
            if i is None:
                return self.getTokens(deepDSLParser.METRICS)
            else:
                return self.getToken(deepDSLParser.METRICS, i)

        def getRuleIndex(self):
            return deepDSLParser.RULE_evaluate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvaluate" ):
                listener.enterEvaluate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvaluate" ):
                listener.exitEvaluate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEvaluate" ):
                return visitor.visitEvaluate(self)
            else:
                return visitor.visitChildren(self)




    def evaluate(self):

        localctx = deepDSLParser.EvaluateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_evaluate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(deepDSLParser.T__13)
            self.state = 99
            self.match(deepDSLParser.T__1)
            self.state = 100
            self.match(deepDSLParser.T__14)
            self.state = 101
            self.match(deepDSLParser.T__8)
            self.state = 102
            self.match(deepDSLParser.T__9)
            self.state = 103
            self.match(deepDSLParser.METRICS)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 104
                self.match(deepDSLParser.T__10)
                self.state = 105
                self.match(deepDSLParser.METRICS)
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 111
            self.match(deepDSLParser.T__11)
            self.state = 112
            self.match(deepDSLParser.T__12)
            self.state = 113
            self.match(deepDSLParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptimizerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPTIMIZER(self):
            return self.getToken(deepDSLParser.OPTIMIZER, 0)

        def getRuleIndex(self):
            return deepDSLParser.RULE_optimizer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptimizer" ):
                listener.enterOptimizer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptimizer" ):
                listener.exitOptimizer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptimizer" ):
                return visitor.visitOptimizer(self)
            else:
                return visitor.visitChildren(self)




    def optimizer(self):

        localctx = deepDSLParser.OptimizerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_optimizer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(deepDSLParser.T__15)
            self.state = 116
            self.match(deepDSLParser.T__8)
            self.state = 117
            self.match(deepDSLParser.OPTIMIZER)
            self.state = 118
            self.match(deepDSLParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LossContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOSS_FN(self):
            return self.getToken(deepDSLParser.LOSS_FN, 0)

        def getRuleIndex(self):
            return deepDSLParser.RULE_loss

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoss" ):
                listener.enterLoss(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoss" ):
                listener.exitLoss(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoss" ):
                return visitor.visitLoss(self)
            else:
                return visitor.visitChildren(self)




    def loss(self):

        localctx = deepDSLParser.LossContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_loss)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(deepDSLParser.T__16)
            self.state = 121
            self.match(deepDSLParser.T__8)
            self.state = 122
            self.match(deepDSLParser.LOSS_FN)
            self.state = 123
            self.match(deepDSLParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Metric_choiceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def METRICS(self, i:int=None):
            if i is None:
                return self.getTokens(deepDSLParser.METRICS)
            else:
                return self.getToken(deepDSLParser.METRICS, i)

        def getRuleIndex(self):
            return deepDSLParser.RULE_metric_choice

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMetric_choice" ):
                listener.enterMetric_choice(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMetric_choice" ):
                listener.exitMetric_choice(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMetric_choice" ):
                return visitor.visitMetric_choice(self)
            else:
                return visitor.visitChildren(self)




    def metric_choice(self):

        localctx = deepDSLParser.Metric_choiceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_metric_choice)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(deepDSLParser.T__14)
            self.state = 126
            self.match(deepDSLParser.T__8)
            self.state = 127
            self.match(deepDSLParser.T__9)
            self.state = 128
            self.match(deepDSLParser.METRICS)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 129
                self.match(deepDSLParser.T__10)
                self.state = 130
                self.match(deepDSLParser.METRICS)
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 136
            self.match(deepDSLParser.T__11)
            self.state = 137
            self.match(deepDSLParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EpochsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(deepDSLParser.INT, 0)

        def getRuleIndex(self):
            return deepDSLParser.RULE_epochs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEpochs" ):
                listener.enterEpochs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEpochs" ):
                listener.exitEpochs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEpochs" ):
                return visitor.visitEpochs(self)
            else:
                return visitor.visitChildren(self)




    def epochs(self):

        localctx = deepDSLParser.EpochsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_epochs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(deepDSLParser.T__17)
            self.state = 140
            self.match(deepDSLParser.T__8)
            self.state = 141
            self.match(deepDSLParser.INT)
            self.state = 142
            self.match(deepDSLParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Batch_sizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(deepDSLParser.INT, 0)

        def getRuleIndex(self):
            return deepDSLParser.RULE_batch_size

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBatch_size" ):
                listener.enterBatch_size(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBatch_size" ):
                listener.exitBatch_size(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBatch_size" ):
                return visitor.visitBatch_size(self)
            else:
                return visitor.visitChildren(self)




    def batch_size(self):

        localctx = deepDSLParser.Batch_sizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_batch_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(deepDSLParser.T__18)
            self.state = 145
            self.match(deepDSLParser.T__8)
            self.state = 146
            self.match(deepDSLParser.INT)
            self.state = 147
            self.match(deepDSLParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Validation_splitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(deepDSLParser.FLOAT, 0)

        def getRuleIndex(self):
            return deepDSLParser.RULE_validation_split

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValidation_split" ):
                listener.enterValidation_split(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValidation_split" ):
                listener.exitValidation_split(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValidation_split" ):
                return visitor.visitValidation_split(self)
            else:
                return visitor.visitChildren(self)




    def validation_split(self):

        localctx = deepDSLParser.Validation_splitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_validation_split)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(deepDSLParser.T__19)
            self.state = 150
            self.match(deepDSLParser.T__8)
            self.state = 151
            self.match(deepDSLParser.FLOAT)
            self.state = 152
            self.match(deepDSLParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SourceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(deepDSLParser.STRING, 0)

        def getRuleIndex(self):
            return deepDSLParser.RULE_source

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSource" ):
                listener.enterSource(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSource" ):
                listener.exitSource(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSource" ):
                return visitor.visitSource(self)
            else:
                return visitor.visitChildren(self)




    def source(self):

        localctx = deepDSLParser.SourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_source)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(deepDSLParser.T__20)
            self.state = 155
            self.match(deepDSLParser.T__8)
            self.state = 156
            self.match(deepDSLParser.STRING)
            self.state = 157
            self.match(deepDSLParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreprocessingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREPROCESSING_FN(self):
            return self.getToken(deepDSLParser.PREPROCESSING_FN, 0)

        def getRuleIndex(self):
            return deepDSLParser.RULE_preprocessing

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreprocessing" ):
                listener.enterPreprocessing(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreprocessing" ):
                listener.exitPreprocessing(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreprocessing" ):
                return visitor.visitPreprocessing(self)
            else:
                return visitor.visitChildren(self)




    def preprocessing(self):

        localctx = deepDSLParser.PreprocessingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_preprocessing)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(deepDSLParser.T__21)
            self.state = 160
            self.match(deepDSLParser.T__8)
            self.state = 161
            self.match(deepDSLParser.PREPROCESSING_FN)
            self.state = 162
            self.match(deepDSLParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LAYER_TYPE(self):
            return self.getToken(deepDSLParser.LAYER_TYPE, 0)

        def getRuleIndex(self):
            return deepDSLParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = deepDSLParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(deepDSLParser.T__22)
            self.state = 165
            self.match(deepDSLParser.T__8)
            self.state = 166
            self.match(deepDSLParser.LAYER_TYPE)
            self.state = 167
            self.match(deepDSLParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnitsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(deepDSLParser.INT, 0)

        def getRuleIndex(self):
            return deepDSLParser.RULE_units

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnits" ):
                listener.enterUnits(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnits" ):
                listener.exitUnits(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnits" ):
                return visitor.visitUnits(self)
            else:
                return visitor.visitChildren(self)




    def units(self):

        localctx = deepDSLParser.UnitsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_units)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(deepDSLParser.T__23)
            self.state = 170
            self.match(deepDSLParser.T__8)
            self.state = 171
            self.match(deepDSLParser.INT)
            self.state = 172
            self.match(deepDSLParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActivationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACTIVATION_FN(self):
            return self.getToken(deepDSLParser.ACTIVATION_FN, 0)

        def getRuleIndex(self):
            return deepDSLParser.RULE_activation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActivation" ):
                listener.enterActivation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActivation" ):
                listener.exitActivation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActivation" ):
                return visitor.visitActivation(self)
            else:
                return visitor.visitChildren(self)




    def activation(self):

        localctx = deepDSLParser.ActivationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_activation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(deepDSLParser.T__24)
            self.state = 175
            self.match(deepDSLParser.T__8)
            self.state = 176
            self.match(deepDSLParser.ACTIVATION_FN)
            self.state = 177
            self.match(deepDSLParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Input_shapeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(deepDSLParser.INT)
            else:
                return self.getToken(deepDSLParser.INT, i)

        def getRuleIndex(self):
            return deepDSLParser.RULE_input_shape

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput_shape" ):
                listener.enterInput_shape(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput_shape" ):
                listener.exitInput_shape(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInput_shape" ):
                return visitor.visitInput_shape(self)
            else:
                return visitor.visitChildren(self)




    def input_shape(self):

        localctx = deepDSLParser.Input_shapeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_input_shape)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(deepDSLParser.T__25)
            self.state = 180
            self.match(deepDSLParser.T__8)
            self.state = 181
            self.match(deepDSLParser.T__9)
            self.state = 182
            self.match(deepDSLParser.INT)
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 183
                self.match(deepDSLParser.T__10)
                self.state = 184
                self.match(deepDSLParser.INT)
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 190
            self.match(deepDSLParser.T__11)
            self.state = 191
            self.match(deepDSLParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





