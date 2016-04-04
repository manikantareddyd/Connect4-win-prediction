### An oracle for predicting who wins at a game of Connect 4

We are provided with the configuration of the connect four game board after the 8th move of both the players. The configuration has 42 parameters with a variability of 3 modes.

Every position of board is either occupied by x or b or is empty. So we generate a vector of length 42x3 by substituting a mode of position by a vector [1/0,1/0,1/0]. This configuration finally resulted to either of win or draw or loss of a specific player.

We use Linear Support Vector classifiers to train a prediction model for this data. We can use Linear Support Vector Classifiers in either one-vs-one or one-vs-all configuration.

A priori Class Distribution: 44473 win(65.83%), 16635 loss(24.62%), 6449 draw(9.55%) It is worth noting that, in our predictions, the draw class appears to be negligible!

|            |            |           |   One-vs-One     |          |           |    One-vs-All    |          |
|------------|------------|-----------|--------|----------|-----------|--------|----------|
|            | labels     | precision | recall | f1-score | precision | recall | f1-score |
| Fold 1     | -1         | 0.67      | 0.43   | 0.52     | 0.68      | 0.39   | 0.5      |
|            | 0          | 0.8       | 0      | 0.01     | 0.2       | 0      | 0        |
|            | 1          | 0.79      | 0.95   | 0.86     | 0.78      | 0.95   | 0.86     |
| Fold 2     | -1         | 0.71      | 0.65   | 0.68     | 0.76      | 0.58   | 0.66     |
|            | 0          | 0         | 0      | 0        | 0         | 0      | 0        |
|            | 1          | 0.84      | 0.95   | 0.89     | 0.82      | 0.96   | 0.89     |
| Fold 3     | -1         | 0.62      | 0.71   | 0.66     | 0.66      | 0.64   | 0.65     |
|            | 0          | 0.15      | 0.01   | 0.02     | 0.17      | 0.01   | 0.02     |
|            | 1          | 0.76      | 0.83   | 0.8      | 0.74      | 0.87   | 0.8      |
| Fold 4     | -1         | 0.63      | 0.55   | 0.59     | 0.68      | 0.46   | 0.55     |
|            | 0          | 0.21      | 0      | 0.01     | 0.25      | 0      | 0        |
|            | 1          | 0.78      | 0.92   | 0.84     | 0.76      | 0.94   | 0.84     |
| Fold 5     | -1         | 0.66      | 0.54   | 0.6      | 0.72      | 0.45   | 0.56     |
|            | 0          | 0.27      | 0.01   | 0.02     | 0.5       | 0      | 0        |
|            | 1          | 0.71      | 0.92   | 0.8      | 0.68      | 0.95   | 0.79     |

The very low posteriori distribution of draw is because of the decision function chosen for ambiguous classification used in case of Ambiguous predictions of binary classifiers.

i,e, if a one-one classifiers say win-loss-draw at the same time we output win (owing to high distribution of win in training set)
