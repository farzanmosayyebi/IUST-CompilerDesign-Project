# Generated from D:/University/Compiler Design/DeepDSL/Grammar/deepDSL.g4 by ANTLR 4.13.2
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
        4,1,30,89,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,4,0,11,8,0,11,
        0,12,0,12,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,3,1,33,8,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,41,8,1,
        10,1,12,1,44,9,1,1,1,1,1,3,1,48,8,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,68,8,2,10,2,12,2,
        71,9,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,0,0,3,0,2,4,0,0,90,0,6,1,0,0,0,2,17,1,0,0,0,4,51,1,0,0,
        0,6,7,5,1,0,0,7,8,5,21,0,0,8,10,5,2,0,0,9,11,3,2,1,0,10,9,1,0,0,
        0,11,12,1,0,0,0,12,10,1,0,0,0,12,13,1,0,0,0,13,14,1,0,0,0,14,15,
        3,4,2,0,15,16,5,3,0,0,16,1,1,0,0,0,17,18,5,4,0,0,18,19,5,21,0,0,
        19,20,5,2,0,0,20,21,5,5,0,0,21,22,5,6,0,0,22,23,5,22,0,0,23,24,5,
        7,0,0,24,25,5,8,0,0,25,26,5,6,0,0,26,27,5,27,0,0,27,32,5,7,0,0,28,
        29,5,9,0,0,29,30,5,6,0,0,30,31,5,23,0,0,31,33,5,7,0,0,32,28,1,0,
        0,0,32,33,1,0,0,0,33,47,1,0,0,0,34,35,5,10,0,0,35,36,5,6,0,0,36,
        37,5,11,0,0,37,42,5,27,0,0,38,39,5,12,0,0,39,41,5,27,0,0,40,38,1,
        0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,45,1,0,0,0,44,
        42,1,0,0,0,45,46,5,13,0,0,46,48,5,7,0,0,47,34,1,0,0,0,47,48,1,0,
        0,0,48,49,1,0,0,0,49,50,5,3,0,0,50,3,1,0,0,0,51,52,5,14,0,0,52,53,
        5,2,0,0,53,54,5,15,0,0,54,55,5,6,0,0,55,56,5,24,0,0,56,57,5,7,0,
        0,57,58,5,16,0,0,58,59,5,6,0,0,59,60,5,25,0,0,60,61,5,7,0,0,61,62,
        5,17,0,0,62,63,5,6,0,0,63,64,5,11,0,0,64,69,5,26,0,0,65,66,5,12,
        0,0,66,68,5,26,0,0,67,65,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,
        70,1,0,0,0,70,72,1,0,0,0,71,69,1,0,0,0,72,73,5,13,0,0,73,74,5,7,
        0,0,74,75,5,18,0,0,75,76,5,6,0,0,76,77,5,27,0,0,77,78,5,7,0,0,78,
        79,5,19,0,0,79,80,5,6,0,0,80,81,5,27,0,0,81,82,5,7,0,0,82,83,5,20,
        0,0,83,84,5,6,0,0,84,85,5,28,0,0,85,86,5,7,0,0,86,87,5,3,0,0,87,
        5,1,0,0,0,5,12,32,42,47,69
    ]

class deepDSLParser ( Parser ):

    grammarFileName = "deepDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'network'", "'{'", "'}'", "'layer'", 
                     "'type'", "':'", "';'", "'units'", "'activation'", 
                     "'input_shape'", "'['", "','", "']'", "'training'", 
                     "'optimizer'", "'loss'", "'metrics'", "'epochs'", "'batch_size'", 
                     "'validation_split'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "LAYER_TYPE", "ACTIVATION_FN", 
                      "OPTIMIZER", "LOSS_FN", "METRICS", "INT", "FLOAT", 
                      "WS", "COMMENT" ]

    RULE_network = 0
    RULE_layer = 1
    RULE_training = 2

    ruleNames =  [ "network", "layer", "training" ]

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
    ID=21
    LAYER_TYPE=22
    ACTIVATION_FN=23
    OPTIMIZER=24
    LOSS_FN=25
    METRICS=26
    INT=27
    FLOAT=28
    WS=29
    COMMENT=30

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
            self.state = 6
            self.match(deepDSLParser.T__0)
            self.state = 7
            self.match(deepDSLParser.ID)
            self.state = 8
            self.match(deepDSLParser.T__1)
            self.state = 10 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 9
                self.layer()
                self.state = 12 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==4):
                    break

            self.state = 14
            self.training()
            self.state = 15
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

        def LAYER_TYPE(self):
            return self.getToken(deepDSLParser.LAYER_TYPE, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(deepDSLParser.INT)
            else:
                return self.getToken(deepDSLParser.INT, i)

        def ACTIVATION_FN(self):
            return self.getToken(deepDSLParser.ACTIVATION_FN, 0)

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
            self.state = 17
            self.match(deepDSLParser.T__3)
            self.state = 18
            self.match(deepDSLParser.ID)
            self.state = 19
            self.match(deepDSLParser.T__1)
            self.state = 20
            self.match(deepDSLParser.T__4)
            self.state = 21
            self.match(deepDSLParser.T__5)
            self.state = 22
            self.match(deepDSLParser.LAYER_TYPE)
            self.state = 23
            self.match(deepDSLParser.T__6)
            self.state = 24
            self.match(deepDSLParser.T__7)
            self.state = 25
            self.match(deepDSLParser.T__5)
            self.state = 26
            self.match(deepDSLParser.INT)
            self.state = 27
            self.match(deepDSLParser.T__6)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 28
                self.match(deepDSLParser.T__8)
                self.state = 29
                self.match(deepDSLParser.T__5)
                self.state = 30
                self.match(deepDSLParser.ACTIVATION_FN)
                self.state = 31
                self.match(deepDSLParser.T__6)


            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 34
                self.match(deepDSLParser.T__9)
                self.state = 35
                self.match(deepDSLParser.T__5)
                self.state = 36
                self.match(deepDSLParser.T__10)
                self.state = 37
                self.match(deepDSLParser.INT)
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==12:
                    self.state = 38
                    self.match(deepDSLParser.T__11)
                    self.state = 39
                    self.match(deepDSLParser.INT)
                    self.state = 44
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 45
                self.match(deepDSLParser.T__12)
                self.state = 46
                self.match(deepDSLParser.T__6)


            self.state = 49
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

        def OPTIMIZER(self):
            return self.getToken(deepDSLParser.OPTIMIZER, 0)

        def LOSS_FN(self):
            return self.getToken(deepDSLParser.LOSS_FN, 0)

        def METRICS(self, i:int=None):
            if i is None:
                return self.getTokens(deepDSLParser.METRICS)
            else:
                return self.getToken(deepDSLParser.METRICS, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(deepDSLParser.INT)
            else:
                return self.getToken(deepDSLParser.INT, i)

        def FLOAT(self):
            return self.getToken(deepDSLParser.FLOAT, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(deepDSLParser.T__13)
            self.state = 52
            self.match(deepDSLParser.T__1)
            self.state = 53
            self.match(deepDSLParser.T__14)
            self.state = 54
            self.match(deepDSLParser.T__5)
            self.state = 55
            self.match(deepDSLParser.OPTIMIZER)
            self.state = 56
            self.match(deepDSLParser.T__6)
            self.state = 57
            self.match(deepDSLParser.T__15)
            self.state = 58
            self.match(deepDSLParser.T__5)
            self.state = 59
            self.match(deepDSLParser.LOSS_FN)
            self.state = 60
            self.match(deepDSLParser.T__6)
            self.state = 61
            self.match(deepDSLParser.T__16)
            self.state = 62
            self.match(deepDSLParser.T__5)
            self.state = 63
            self.match(deepDSLParser.T__10)
            self.state = 64
            self.match(deepDSLParser.METRICS)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 65
                self.match(deepDSLParser.T__11)
                self.state = 66
                self.match(deepDSLParser.METRICS)
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.match(deepDSLParser.T__12)
            self.state = 73
            self.match(deepDSLParser.T__6)
            self.state = 74
            self.match(deepDSLParser.T__17)
            self.state = 75
            self.match(deepDSLParser.T__5)
            self.state = 76
            self.match(deepDSLParser.INT)
            self.state = 77
            self.match(deepDSLParser.T__6)
            self.state = 78
            self.match(deepDSLParser.T__18)
            self.state = 79
            self.match(deepDSLParser.T__5)
            self.state = 80
            self.match(deepDSLParser.INT)
            self.state = 81
            self.match(deepDSLParser.T__6)
            self.state = 82
            self.match(deepDSLParser.T__19)
            self.state = 83
            self.match(deepDSLParser.T__5)
            self.state = 84
            self.match(deepDSLParser.FLOAT)
            self.state = 85
            self.match(deepDSLParser.T__6)
            self.state = 86
            self.match(deepDSLParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





