grammar deepDSL;

// Parser Rules

start: network EOF;

network: 'network' ID '{'
            layer+
            training
            (dataset)?
            (visualize)?
            (evaluate)?
         '}';

layer: 'layer' ID '{'
          types
          units
          (activation)?
          (input_shape)?
       '}';

training: 'training' '{'
               optimizer
               loss
               metric_choice
               epochs
               batch_size
               validation_split
          '}';

dataset: 'dataset' ID '{'
                source
                preprocessing
           '}';

visualize: 'visualize' '{'
                'grid' ':' '[' size ',' size ']' ';'
           '}';

evaluate: 'evaluate' '{'
                metric_choice
           '}';

optimizer: 'optimizer' ':' optimizer_func ';';

optimizer_func: ('adam' | 'sgd' | 'rmsprop');

loss: 'loss' ':' loss_func ';';
loss_func: ('SparseCategoricalCrossentropy' | 'MeanSquearedError');

metric_choice: 'metric' ':' '[' metrics (',' metrics)* ']' ';';

metrics: ('accuracy' | 'loss');

epochs: 'epochs' ':' size ';';

batch_size: 'batch_size' ':' size ';';

validation_split: 'validation_split' ':' size ';';

source: 'source' ':' path ';';

preprocessing: 'preprocessing' ':' preprocessing_func ';';

preprocessing_func: 'normalize' size;

types: 'type' ':' ('Dense' | 'Flatten') ';';

units: 'units' ':' size ';';

activation: 'activation' ':' activation_func ';';
activation_func: ('Relu' | 'Sigmoid' | 'Softmax' | 'Tanh' | 'Linear');

input_shape: 'input_shape' ':' '[' size (',' size)* ']' ';';

size : INT | FLOAT;

path: STRING;

// Lexer Rules
ID: [a-zA-Z_][a-zA-Z_0-9]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' .*? '"';
WS: [ \t\r\n]+ -> skip;
COMMENT: '#' ~[\r\n]* -> skip;
