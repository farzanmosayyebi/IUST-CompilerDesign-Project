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
        4,1,46,216,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,1,0,1,
        0,1,1,1,1,1,1,1,1,4,1,60,8,1,11,1,12,1,61,1,1,1,1,3,1,66,8,1,1,1,
        3,1,69,8,1,1,1,3,1,72,8,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,82,
        8,2,1,2,3,2,85,8,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,
        9,1,9,1,9,1,9,1,9,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,5,11,143,
        8,11,10,11,12,11,146,9,11,1,11,1,11,1,11,1,12,1,12,1,13,1,13,1,13,
        1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,16,
        1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,19,
        1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,
        1,21,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,5,23,204,8,23,10,23,
        12,23,207,9,23,1,23,1,23,1,23,1,24,1,24,1,25,1,25,1,25,0,0,26,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,
        48,50,0,6,1,0,16,18,1,0,20,21,2,0,19,19,23,23,1,0,31,32,1,0,35,39,
        1,0,42,43,197,0,52,1,0,0,0,2,55,1,0,0,0,4,75,1,0,0,0,6,88,1,0,0,
        0,8,98,1,0,0,0,10,105,1,0,0,0,12,117,1,0,0,0,14,122,1,0,0,0,16,127,
        1,0,0,0,18,129,1,0,0,0,20,134,1,0,0,0,22,136,1,0,0,0,24,150,1,0,
        0,0,26,152,1,0,0,0,28,157,1,0,0,0,30,162,1,0,0,0,32,167,1,0,0,0,
        34,172,1,0,0,0,36,177,1,0,0,0,38,180,1,0,0,0,40,185,1,0,0,0,42,190,
        1,0,0,0,44,195,1,0,0,0,46,197,1,0,0,0,48,211,1,0,0,0,50,213,1,0,
        0,0,52,53,3,2,1,0,53,54,5,0,0,1,54,1,1,0,0,0,55,56,5,1,0,0,56,57,
        5,41,0,0,57,59,5,2,0,0,58,60,3,4,2,0,59,58,1,0,0,0,60,61,1,0,0,0,
        61,59,1,0,0,0,61,62,1,0,0,0,62,63,1,0,0,0,63,65,3,6,3,0,64,66,3,
        8,4,0,65,64,1,0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,67,69,3,10,5,0,68,
        67,1,0,0,0,68,69,1,0,0,0,69,71,1,0,0,0,70,72,3,12,6,0,71,70,1,0,
        0,0,71,72,1,0,0,0,72,73,1,0,0,0,73,74,5,3,0,0,74,3,1,0,0,0,75,76,
        5,4,0,0,76,77,5,41,0,0,77,78,5,2,0,0,78,79,3,38,19,0,79,81,3,40,
        20,0,80,82,3,42,21,0,81,80,1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,
        85,3,46,23,0,84,83,1,0,0,0,84,85,1,0,0,0,85,86,1,0,0,0,86,87,5,3,
        0,0,87,5,1,0,0,0,88,89,5,5,0,0,89,90,5,2,0,0,90,91,3,14,7,0,91,92,
        3,18,9,0,92,93,3,22,11,0,93,94,3,26,13,0,94,95,3,28,14,0,95,96,3,
        30,15,0,96,97,5,3,0,0,97,7,1,0,0,0,98,99,5,6,0,0,99,100,5,41,0,0,
        100,101,5,2,0,0,101,102,3,32,16,0,102,103,3,34,17,0,103,104,5,3,
        0,0,104,9,1,0,0,0,105,106,5,7,0,0,106,107,5,2,0,0,107,108,5,8,0,
        0,108,109,5,9,0,0,109,110,5,10,0,0,110,111,3,48,24,0,111,112,5,11,
        0,0,112,113,3,48,24,0,113,114,5,12,0,0,114,115,5,13,0,0,115,116,
        5,3,0,0,116,11,1,0,0,0,117,118,5,14,0,0,118,119,5,2,0,0,119,120,
        3,22,11,0,120,121,5,3,0,0,121,13,1,0,0,0,122,123,5,15,0,0,123,124,
        5,9,0,0,124,125,3,16,8,0,125,126,5,13,0,0,126,15,1,0,0,0,127,128,
        7,0,0,0,128,17,1,0,0,0,129,130,5,19,0,0,130,131,5,9,0,0,131,132,
        3,20,10,0,132,133,5,13,0,0,133,19,1,0,0,0,134,135,7,1,0,0,135,21,
        1,0,0,0,136,137,5,22,0,0,137,138,5,9,0,0,138,139,5,10,0,0,139,144,
        3,24,12,0,140,141,5,11,0,0,141,143,3,24,12,0,142,140,1,0,0,0,143,
        146,1,0,0,0,144,142,1,0,0,0,144,145,1,0,0,0,145,147,1,0,0,0,146,
        144,1,0,0,0,147,148,5,12,0,0,148,149,5,13,0,0,149,23,1,0,0,0,150,
        151,7,2,0,0,151,25,1,0,0,0,152,153,5,24,0,0,153,154,5,9,0,0,154,
        155,3,48,24,0,155,156,5,13,0,0,156,27,1,0,0,0,157,158,5,25,0,0,158,
        159,5,9,0,0,159,160,3,48,24,0,160,161,5,13,0,0,161,29,1,0,0,0,162,
        163,5,26,0,0,163,164,5,9,0,0,164,165,3,48,24,0,165,166,5,13,0,0,
        166,31,1,0,0,0,167,168,5,27,0,0,168,169,5,9,0,0,169,170,3,50,25,
        0,170,171,5,13,0,0,171,33,1,0,0,0,172,173,5,28,0,0,173,174,5,9,0,
        0,174,175,3,36,18,0,175,176,5,13,0,0,176,35,1,0,0,0,177,178,5,29,
        0,0,178,179,3,48,24,0,179,37,1,0,0,0,180,181,5,30,0,0,181,182,5,
        9,0,0,182,183,7,3,0,0,183,184,5,13,0,0,184,39,1,0,0,0,185,186,5,
        33,0,0,186,187,5,9,0,0,187,188,3,48,24,0,188,189,5,13,0,0,189,41,
        1,0,0,0,190,191,5,34,0,0,191,192,5,9,0,0,192,193,3,44,22,0,193,194,
        5,13,0,0,194,43,1,0,0,0,195,196,7,4,0,0,196,45,1,0,0,0,197,198,5,
        40,0,0,198,199,5,9,0,0,199,200,5,10,0,0,200,205,3,48,24,0,201,202,
        5,11,0,0,202,204,3,48,24,0,203,201,1,0,0,0,204,207,1,0,0,0,205,203,
        1,0,0,0,205,206,1,0,0,0,206,208,1,0,0,0,207,205,1,0,0,0,208,209,
        5,12,0,0,209,210,5,13,0,0,210,47,1,0,0,0,211,212,7,5,0,0,212,49,
        1,0,0,0,213,214,5,44,0,0,214,51,1,0,0,0,8,61,65,68,71,81,84,144,
        205
    ]

class deepDSLParser ( Parser ):

    grammarFileName = "deepDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'network'", "'{'", "'}'", "'layer'", 
                     "'training'", "'dataset'", "'visualize'", "'grid'", 
                     "':'", "'['", "','", "']'", "';'", "'evaluate'", "'optimizer'", 
                     "'adam'", "'sgd'", "'rmsprop'", "'loss'", "'SparseCategoricalCrossentropy'", 
                     "'MeanSquearedError'", "'metric'", "'accuracy'", "'epochs'", 
                     "'batch_size'", "'validation_split'", "'source'", "'preprocessing'", 
                     "'normalize'", "'type'", "'Dense'", "'Flatten'", "'units'", 
                     "'activation'", "'Relu'", "'Sigmoid'", "'Softmax'", 
                     "'Tanh'", "'Linear'", "'input_shape'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "INT", "FLOAT", "STRING", "WS", 
                      "COMMENT" ]

    RULE_start = 0
    RULE_network = 1
    RULE_layer = 2
    RULE_training = 3
    RULE_dataset = 4
    RULE_visualize = 5
    RULE_evaluate = 6
    RULE_optimizer = 7
    RULE_optimizer_func = 8
    RULE_loss = 9
    RULE_loss_func = 10
    RULE_metric_choice = 11
    RULE_metrics = 12
    RULE_epochs = 13
    RULE_batch_size = 14
    RULE_validation_split = 15
    RULE_source = 16
    RULE_preprocessing = 17
    RULE_preprocessing_func = 18
    RULE_types = 19
    RULE_units = 20
    RULE_activation = 21
    RULE_activation_func = 22
    RULE_input_shape = 23
    RULE_value = 24
    RULE_path = 25

    ruleNames =  [ "start", "network", "layer", "training", "dataset", "visualize", 
                   "evaluate", "optimizer", "optimizer_func", "loss", "loss_func", 
                   "metric_choice", "metrics", "epochs", "batch_size", "validation_split", 
                   "source", "preprocessing", "preprocessing_func", "types", 
                   "units", "activation", "activation_func", "input_shape", 
                   "value", "path" ]

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
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    ID=41
    INT=42
    FLOAT=43
    STRING=44
    WS=45
    COMMENT=46

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def network(self):
            return self.getTypedRuleContext(deepDSLParser.NetworkContext,0)


        def EOF(self):
            return self.getToken(deepDSLParser.EOF, 0)

        def getRuleIndex(self):
            return deepDSLParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = deepDSLParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.network()
            self.state = 53
            self.match(deepDSLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


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
        self.enterRule(localctx, 2, self.RULE_network)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(deepDSLParser.T__0)
            self.state = 56
            self.match(deepDSLParser.ID)
            self.state = 57
            self.match(deepDSLParser.T__1)
            self.state = 59 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 58
                self.layer()
                self.state = 61 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==4):
                    break

            self.state = 63
            self.training()
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 64
                self.dataset()


            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 67
                self.visualize()


            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 70
                self.evaluate()


            self.state = 73
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

        def types(self):
            return self.getTypedRuleContext(deepDSLParser.TypesContext,0)


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
        self.enterRule(localctx, 4, self.RULE_layer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(deepDSLParser.T__3)
            self.state = 76
            self.match(deepDSLParser.ID)
            self.state = 77
            self.match(deepDSLParser.T__1)
            self.state = 78
            self.types()
            self.state = 79
            self.units()
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 80
                self.activation()


            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 83
                self.input_shape()


            self.state = 86
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
        self.enterRule(localctx, 6, self.RULE_training)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(deepDSLParser.T__4)
            self.state = 89
            self.match(deepDSLParser.T__1)
            self.state = 90
            self.optimizer()
            self.state = 91
            self.loss()
            self.state = 92
            self.metric_choice()
            self.state = 93
            self.epochs()
            self.state = 94
            self.batch_size()
            self.state = 95
            self.validation_split()
            self.state = 96
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
        self.enterRule(localctx, 8, self.RULE_dataset)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(deepDSLParser.T__5)
            self.state = 99
            self.match(deepDSLParser.ID)
            self.state = 100
            self.match(deepDSLParser.T__1)
            self.state = 101
            self.source()
            self.state = 102
            self.preprocessing()
            self.state = 103
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

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(deepDSLParser.ValueContext)
            else:
                return self.getTypedRuleContext(deepDSLParser.ValueContext,i)


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
        self.enterRule(localctx, 10, self.RULE_visualize)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(deepDSLParser.T__6)
            self.state = 106
            self.match(deepDSLParser.T__1)
            self.state = 107
            self.match(deepDSLParser.T__7)
            self.state = 108
            self.match(deepDSLParser.T__8)
            self.state = 109
            self.match(deepDSLParser.T__9)
            self.state = 110
            self.value()
            self.state = 111
            self.match(deepDSLParser.T__10)
            self.state = 112
            self.value()
            self.state = 113
            self.match(deepDSLParser.T__11)
            self.state = 114
            self.match(deepDSLParser.T__12)
            self.state = 115
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

        def metric_choice(self):
            return self.getTypedRuleContext(deepDSLParser.Metric_choiceContext,0)


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
        self.enterRule(localctx, 12, self.RULE_evaluate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(deepDSLParser.T__13)
            self.state = 118
            self.match(deepDSLParser.T__1)
            self.state = 119
            self.metric_choice()
            self.state = 120
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

        def optimizer_func(self):
            return self.getTypedRuleContext(deepDSLParser.Optimizer_funcContext,0)


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
        self.enterRule(localctx, 14, self.RULE_optimizer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(deepDSLParser.T__14)
            self.state = 123
            self.match(deepDSLParser.T__8)
            self.state = 124
            self.optimizer_func()
            self.state = 125
            self.match(deepDSLParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optimizer_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return deepDSLParser.RULE_optimizer_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptimizer_func" ):
                listener.enterOptimizer_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptimizer_func" ):
                listener.exitOptimizer_func(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptimizer_func" ):
                return visitor.visitOptimizer_func(self)
            else:
                return visitor.visitChildren(self)




    def optimizer_func(self):

        localctx = deepDSLParser.Optimizer_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_optimizer_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 458752) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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

        def loss_func(self):
            return self.getTypedRuleContext(deepDSLParser.Loss_funcContext,0)


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
        self.enterRule(localctx, 18, self.RULE_loss)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(deepDSLParser.T__18)
            self.state = 130
            self.match(deepDSLParser.T__8)
            self.state = 131
            self.loss_func()
            self.state = 132
            self.match(deepDSLParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loss_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return deepDSLParser.RULE_loss_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoss_func" ):
                listener.enterLoss_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoss_func" ):
                listener.exitLoss_func(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoss_func" ):
                return visitor.visitLoss_func(self)
            else:
                return visitor.visitChildren(self)




    def loss_func(self):

        localctx = deepDSLParser.Loss_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_loss_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            _la = self._input.LA(1)
            if not(_la==20 or _la==21):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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

        def metrics(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(deepDSLParser.MetricsContext)
            else:
                return self.getTypedRuleContext(deepDSLParser.MetricsContext,i)


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
        self.enterRule(localctx, 22, self.RULE_metric_choice)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(deepDSLParser.T__21)
            self.state = 137
            self.match(deepDSLParser.T__8)
            self.state = 138
            self.match(deepDSLParser.T__9)
            self.state = 139
            self.metrics()
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 140
                self.match(deepDSLParser.T__10)
                self.state = 141
                self.metrics()
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 147
            self.match(deepDSLParser.T__11)
            self.state = 148
            self.match(deepDSLParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MetricsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return deepDSLParser.RULE_metrics

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMetrics" ):
                listener.enterMetrics(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMetrics" ):
                listener.exitMetrics(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMetrics" ):
                return visitor.visitMetrics(self)
            else:
                return visitor.visitChildren(self)




    def metrics(self):

        localctx = deepDSLParser.MetricsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_metrics)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            _la = self._input.LA(1)
            if not(_la==19 or _la==23):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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

        def value(self):
            return self.getTypedRuleContext(deepDSLParser.ValueContext,0)


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
        self.enterRule(localctx, 26, self.RULE_epochs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(deepDSLParser.T__23)
            self.state = 153
            self.match(deepDSLParser.T__8)
            self.state = 154
            self.value()
            self.state = 155
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

        def value(self):
            return self.getTypedRuleContext(deepDSLParser.ValueContext,0)


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
        self.enterRule(localctx, 28, self.RULE_batch_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(deepDSLParser.T__24)
            self.state = 158
            self.match(deepDSLParser.T__8)
            self.state = 159
            self.value()
            self.state = 160
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

        def value(self):
            return self.getTypedRuleContext(deepDSLParser.ValueContext,0)


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
        self.enterRule(localctx, 30, self.RULE_validation_split)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(deepDSLParser.T__25)
            self.state = 163
            self.match(deepDSLParser.T__8)
            self.state = 164
            self.value()
            self.state = 165
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

        def path(self):
            return self.getTypedRuleContext(deepDSLParser.PathContext,0)


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
        self.enterRule(localctx, 32, self.RULE_source)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(deepDSLParser.T__26)
            self.state = 168
            self.match(deepDSLParser.T__8)
            self.state = 169
            self.path()
            self.state = 170
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

        def preprocessing_func(self):
            return self.getTypedRuleContext(deepDSLParser.Preprocessing_funcContext,0)


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
        self.enterRule(localctx, 34, self.RULE_preprocessing)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(deepDSLParser.T__27)
            self.state = 173
            self.match(deepDSLParser.T__8)
            self.state = 174
            self.preprocessing_func()
            self.state = 175
            self.match(deepDSLParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Preprocessing_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(deepDSLParser.ValueContext,0)


        def getRuleIndex(self):
            return deepDSLParser.RULE_preprocessing_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreprocessing_func" ):
                listener.enterPreprocessing_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreprocessing_func" ):
                listener.exitPreprocessing_func(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreprocessing_func" ):
                return visitor.visitPreprocessing_func(self)
            else:
                return visitor.visitChildren(self)




    def preprocessing_func(self):

        localctx = deepDSLParser.Preprocessing_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_preprocessing_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(deepDSLParser.T__28)
            self.state = 178
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return deepDSLParser.RULE_types

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypes" ):
                listener.enterTypes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypes" ):
                listener.exitTypes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypes" ):
                return visitor.visitTypes(self)
            else:
                return visitor.visitChildren(self)




    def types(self):

        localctx = deepDSLParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(deepDSLParser.T__29)
            self.state = 181
            self.match(deepDSLParser.T__8)
            self.state = 182
            _la = self._input.LA(1)
            if not(_la==31 or _la==32):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 183
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

        def value(self):
            return self.getTypedRuleContext(deepDSLParser.ValueContext,0)


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
        self.enterRule(localctx, 40, self.RULE_units)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(deepDSLParser.T__32)
            self.state = 186
            self.match(deepDSLParser.T__8)
            self.state = 187
            self.value()
            self.state = 188
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

        def activation_func(self):
            return self.getTypedRuleContext(deepDSLParser.Activation_funcContext,0)


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
        self.enterRule(localctx, 42, self.RULE_activation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(deepDSLParser.T__33)
            self.state = 191
            self.match(deepDSLParser.T__8)
            self.state = 192
            self.activation_func()
            self.state = 193
            self.match(deepDSLParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Activation_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return deepDSLParser.RULE_activation_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActivation_func" ):
                listener.enterActivation_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActivation_func" ):
                listener.exitActivation_func(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActivation_func" ):
                return visitor.visitActivation_func(self)
            else:
                return visitor.visitChildren(self)




    def activation_func(self):

        localctx = deepDSLParser.Activation_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_activation_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1065151889408) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(deepDSLParser.ValueContext)
            else:
                return self.getTypedRuleContext(deepDSLParser.ValueContext,i)


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
        self.enterRule(localctx, 46, self.RULE_input_shape)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(deepDSLParser.T__39)
            self.state = 198
            self.match(deepDSLParser.T__8)
            self.state = 199
            self.match(deepDSLParser.T__9)
            self.state = 200
            self.value()
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 201
                self.match(deepDSLParser.T__10)
                self.state = 202
                self.value()
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 208
            self.match(deepDSLParser.T__11)
            self.state = 209
            self.match(deepDSLParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(deepDSLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(deepDSLParser.FLOAT, 0)

        def getRuleIndex(self):
            return deepDSLParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = deepDSLParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            _la = self._input.LA(1)
            if not(_la==42 or _la==43):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(deepDSLParser.STRING, 0)

        def getRuleIndex(self):
            return deepDSLParser.RULE_path

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPath" ):
                listener.enterPath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPath" ):
                listener.exitPath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPath" ):
                return visitor.visitPath(self)
            else:
                return visitor.visitChildren(self)




    def path(self):

        localctx = deepDSLParser.PathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_path)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(deepDSLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





