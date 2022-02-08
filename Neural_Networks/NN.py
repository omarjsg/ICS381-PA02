import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


def train(train_x, train_y, units, lr):
    classifier = MLPClassifier(learning_rate_init=float(lr), hidden_layer_sizes=(int(units),), max_iter=200)
    start = time.time()
    model = classifier.fit(train_x, np.ravel(train_y))
    end = time.time()
    plt.plot(classifier.loss_curve_)
    print(classifier.get_params())
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.xticks()
    plt.savefig('assets/loss_vs_epoch.png')
    return f'{end - start:.2f}s', model


def test(test_x, test_y, model):
    classifier = model
    score = classifier.score(test_x, test_y)
    predicted_y = classifier.predict(test_x)
    cm = confusion_matrix(test_y, predicted_y)
    cmd = ConfusionMatrixDisplay(cm, display_labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    cmd.plot()
    cmd.ax_.set(
        title='Confusion Matrix',
        xlabel='Predicted Data',
        ylabel='Actual Data')
    plt.savefig('assets/Confusion_Matrix.png')
    plt.show()
    return f'{score * 100}%'
