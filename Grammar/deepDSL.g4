grammar deepDSL;

// Parser Rules
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
                'grid' ':' '[' INT ',' INT ']' ';'
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

epochs: 'epochs' ':' INT ';';

batch_size: 'batch_size' ':' INT ';';

validation_split: 'validation_split' ':' FLOAT ';';

source: 'source' ':' STRING ';';

preprocessing: 'preprocessing' ':' preprocessing_func ';';

preprocessing_func: 'normalize' INT;

types: 'type' ':' ('Dense' | 'Flatten') ';';

units: 'units' ':' INT ';';

activation: 'activation' ':' activation_func ';';
activation_func: ('Relu' | 'Sigmoid' | 'Softmax' | 'Tanh' | 'Linear');

input_shape: 'input_shape' ':' '[' INT (',' INT)* ']' ';';

// Lexer Rules
ID: [a-zA-Z_][a-zA-Z_0-9]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' .*? '"';
WS: [ \t\r\n]+ -> skip;
COMMENT: '#' ~[\r\n]* -> skip;
