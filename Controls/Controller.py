from tkinter import filedialog
import Controls.FileReading as fr
import Neural_Networks.NN as nn


class Controller(object):
    def __init__(self):
        self.train_x = None
        self.train_y = None
        self.test_x = None
        self.test_y = None
        self.model = None

    def open_directory(self):
        path = filedialog.askopenfilename()
        return path

    def load_training_files(self, train_x_path, train_y_path):
        self.train_x = fr.read(train_x_path)
        self.train_y = fr.read(train_y_path)
        return

    def load_testing_files(self, test_x_path, test_y_path):
        self.test_x = fr.read(test_x_path)
        self.test_y = fr.read(test_y_path)
        return

    def train(self, units, lr):
        time, model = nn.train(self.train_x, self.train_y, units, lr)
        self.model = model
        return time

    def test(self):
        accuracy = nn.test(self.test_x, self.test_y, self.model)
        return accuracy


