grammar deepDSL;

// Parser Rules
network: 'network' ID '{'
            layer+
            training
         '}';

layer: 'layer' ID '{'
          'type' ':' LAYER_TYPE ';'
          'units' ':' INT ';'
          ('activation' ':' ACTIVATION_FN ';')?
          ('input_shape' ':' '[' INT (',' INT)* ']' ';')?
       '}';

training: 'training' '{'
              'optimizer' ':' OPTIMIZER ';'
              'loss' ':' LOSS_FN ';'
              'metrics' ':' '[' METRICS (',' METRICS)* ']' ';'
              'epochs' ':' INT ';'
              'batch_size' ':' INT ';'
              'validation_split' ':' FLOAT ';'
          '}';

// Lexer Rules
ID: [a-zA-Z_][a-zA-Z_0-9]*;
LAYER_TYPE: 'Dense' | 'Flatten';
ACTIVATION_FN: 'relu' | 'sigmoid' | 'softmax' | 'tanh' | 'linear';
OPTIMIZER: 'adam' | 'sgd' | 'rmsprop';
LOSS_FN: 'sparse_categorical_crossentropy' | 'mean_squared_error';
METRICS: 'accuracy' | 'loss';
INT: [0-9]+;
FLOAT: [0-9]+'.'[0-9]+;
WS: [ \t\r\n]+ -> skip;
COMMENT: '#' ~[\r\n]* -> skip;
