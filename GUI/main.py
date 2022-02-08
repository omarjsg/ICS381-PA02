import tkinter as tk
from Controls import Controller
from PIL import ImageTk, Image
from tkmacosx import Button
from tkinter import ttk


class MyApp():
    def __init__(self):
        self.cntrl = Controller.Controller()
        root = tk.Tk()
        root.geometry('1000x320')
        root.update()
        root.configure(bg="#25262B")
        root.title('USPS Digit Recognition')
        training_data_label = tk.Label(root, text="Training Data",
                                       font=("Great Vibes", 32, "bold"), foreground='#FFFFFF', background='#25262B')
        training_data_label.place(x=20, y=20)
        # load train_x section
        trx_load_label = tk.Label(root, text="Select the file of the x training set to load",
                                  font=("Great Vibes", 16, "bold"), foreground='#FFFFFF', background='#25262B')
        trx_load_label.place(x=20, y=90)
        trx_path_field = tk.Entry(root, width=73, font=("Great Vibes", 16), highlightbackground='#25262B',
                                  foreground='#8f98a6', background='#353943')
        trx_path_field.place(x=22, y=120)
        trx_path_field.insert(0, 'docs/tr_X.txt')
        trx_open_button = Button(root, text="Open", command=lambda: self.fill_text_field(trx_path_field),
                                 font=("Great Vibes", 16, "bold"), width=140, height=30, bg='#6D7784', fg='#FFFFFF',
                                 borderless=True, activeforeground='#FFFFFF', activebackground='#88929D',
                                 focusthickness=0)
        trx_open_button.place(x=800, y=120)
        # load train_y section
        try_load_label = tk.Label(root, text="Select the file of the y training set to load",
                                  font=("Great Vibes", 16, "bold"), foreground='#FFFFFF', background='#25262B')
        try_load_label.place(x=20, y=160)
        try_path_field = tk.Entry(root, width=73, font=("Great Vibes", 16), foreground='#8f98a6',
                                  background='#353943', highlightbackground='#25262B')
        try_path_field.place(x=22, y=190)
        try_path_field.insert(0, 'docs/tr_y.txt')
        try_open_button = Button(root, text="Open", command=lambda: self.fill_text_field(try_path_field),
                                 font=("Great Vibes", 16, "bold"), width=140, height=30, bg='#6D7784', fg='#FFFFFF',
                                 borderless=True, activeforeground='#FFFFFF', activebackground='#88929D',
                                 focusthickness=0)
        try_open_button.place(x=800, y=190)
        tr_load_button = Button(root, text="Load Training Files",
                                command=lambda: self.load_training(trx_path_field.get(), try_path_field.get(), root),
                                font=("Great Vibes", 16, "bold"), width=200, height=30, bg='#7AC578', fg='#FFFFFF',
                                borderless=True, activeforeground='#FFFFFF', activebackground='#AAD1A9',
                                focusthickness=0)
        tr_load_button.place(x=400, y=240)
        root.mainloop()

    def fill_text_field(self, tf):
        path = self.cntrl.open_directory()
        tf.delete(0, tk.END)
        tf.insert(0, path)
        return

    def load_training(self, trx_path, try_path, root):
        if len(trx_path) != 0 and len(try_path) != 0:
            self.cntrl.load_training_files(trx_path, try_path)
            root.geometry('1000x350')
            root.update()
            hidden_neurons_label = tk.Label(root, text="Hidden neurons number",
                                            font=("Great Vibes", 16, "bold"), foreground='#FFFFFF',
                                            background='#25262B')
            hidden_neurons_label.place(x=20, y=285)
            hidden_neurons_field = tk.Entry(root, width=15, font=("Great Vibes", 16), foreground='#8f98a6',
                                            background='#353943', highlightbackground='#25262B')
            hidden_neurons_label.place(x=20, y=285)
            hidden_neurons_field.place(x=230, y=285)
            hidden_neurons_field.insert(0,100)
            learning_rate_label = tk.Label(root, text="Learning rate",
                                           font=("Great Vibes", 16, "bold"), foreground='#FFFFFF',
                                           background='#25262B')
            learning_rate_label.place(x=465, y=285)
            learning_rate_field = tk.Entry(root, width=15, font=("Great Vibes", 16), foreground='#8f98a6',
                                           background='#353943', highlightbackground='#25262B')
            learning_rate_field.insert(0, 0.001)
            learning_rate_field.place(x=595, y=285)
            train_button = Button(root, text="Train", command=lambda: self.train(hidden_neurons_field.get(),
                                                                                 learning_rate_field.get(), root),
                                  font=("Great Vibes", 16, "bold"), width=140, height=30, bg='#7AC578', fg='#FFFFFF',
                                  borderless=True, activeforeground='#FFFFFF', activebackground='#AAD1A9',
                                  focusthickness=0)
            train_button.place(x=800, y=285)

    def train(self, hidden_neurons, learning_rate, root):
        if len(hidden_neurons) != 0 or len(learning_rate) != 0 or learning_rate == 0 or hidden_neurons == 0:
            time = self.cntrl.train(hidden_neurons, learning_rate)
            self.plot(root, time)
            self.test(root)

    def plot(self, root, time):
        loss_vs_epoch_label = tk.Label(root, text="Loss vs Epochs",
                                       font=("Great Vibes", 16, "bold"), foreground='#FFFFFF', background='#25262B')
        loss_vs_epoch_label.place(x=950, y=90)
        training_time_label = tk.Label(root, text="Training Time: " + time,
                                       font=("Great Vibes", 16, "bold"), foreground='#FFFFFF', background='#25262B')
        training_time_label.place(x=950, y=330)
        root.geometry("1370x900")
        root.update()
        image = Image.open("assets/loss_vs_epoch.png")
        resized = image.resize((350, 190))
        img = ImageTk.PhotoImage(resized)
        panel = tk.Label(root, image=img)
        panel.image = img
        panel.place(x=950, y=120)

    def test(self, root):
        testing_data_label = tk.Label(root, text="Testing Data",
                                      font=("Great Vibes", 32, "bold"), foreground='#FFFFFF', background='#25262B')
        testing_data_label.place(x=20, y=390)
        # load test_x section
        tex_load_label = tk.Label(root, text="Select the file of the x testing set to load",
                                  font=("Great Vibes", 16, "bold"), foreground='#FFFFFF', background='#25262B')
        tex_load_label.place(x=20, y=470)
        tex_path_field = tk.Entry(root, width=73, font=("Great Vibes", 16), highlightbackground='#25262B',
                                  foreground='#8f98a6', background='#353943')
        tex_path_field.place(x=22, y=500)
        tex_path_field.insert(0, 'docs/te_X.txt')
        tex_open_button = Button(root, text="Open", command=lambda: self.fill_text_field(tex_path_field),
                                 font=("Great Vibes", 16, "bold"), width=140, height=30, bg='#6D7784', fg='#FFFFFF',
                                 borderless=True, activeforeground='#FFFFFF', activebackground='#88929D',
                                 focusthickness=0)
        tex_open_button.place(x=800, y=500)
        # load test_y section
        tey_load_label = tk.Label(root, text="Select the file of the y training set to load",
                                  font=("Great Vibes", 16, "bold"), foreground='#FFFFFF', background='#25262B')
        tey_load_label.place(x=20, y=540)
        tey_path_field = tk.Entry(root, width=73, font=("Great Vibes", 16), foreground='#8f98a6',
                                  background='#353943', highlightbackground='#25262B')
        tey_path_field.place(x=22, y=570)
        tey_path_field.insert(0, 'docs/te_y.txt')
        tey_open_button = Button(root, text="Open", command=lambda: self.fill_text_field(tey_path_field),
                                 font=("Great Vibes", 16, "bold"), width=140, height=30, bg='#6D7784', fg='#FFFFFF',
                                 borderless=True, activeforeground='#FFFFFF', activebackground='#88929D',
                                 focusthickness=0)
        tey_open_button.place(x=800, y=570)
        te_load_button = Button(root, text="Test data",
                                command=lambda: self.load_testing(tex_path_field.get(), tey_path_field.get(), root),
                                font=("Great Vibes", 16, "bold"), width=200, height=30, bg='#7AC578', fg='#FFFFFF',
                                borderless=True, activeforeground='#FFFFFF', activebackground='#AAD1A9',
                                focusthickness=0)
        te_load_button.place(x=400, y=620)

    def load_testing(self, tex_path, tey_path, root):
        self.cntrl.load_testing_files(tex_path, tey_path)
        accuracy = self.cntrl.test()
        confusion_matrix_label = tk.Label(root, text="Confusion Matrix",
                                       font=("Great Vibes", 16, "bold"), foreground='#FFFFFF', background='#25262B')
        confusion_matrix_label.place(x=950, y=470)
        accuracy_label = tk.Label(root, text="Accuracy: " + accuracy,
                                       font=("Great Vibes", 16, "bold"), foreground='#FFFFFF', background='#25262B')
        accuracy_label.place(x=950, y=710)
        image = Image.open("assets/Confusion_Matrix.png")
        resized = image.resize((350, 190))
        img = ImageTk.PhotoImage(resized)
        panel = tk.Label(root, image=img)
        panel.image = img
        panel.place(x=950, y=500)
        tr_load_button = Button(root, text="Load Training Files",
                                command=lambda: self.reset(root),
                                font=("Great Vibes", 16, "bold"), width=200, height=30, bg='#7AC578', fg='#FFFFFF',
                                borderless=True, activeforeground='#FFFFFF', activebackground='#AAD1A9',
                                focusthickness=0)
        tr_load_button.place(x=400, y=240)
        train_button = Button(root, text="Train", command=lambda: self.reset(root),
                              font=("Great Vibes", 16, "bold"), width=140, height=30, bg='#7AC578', fg='#FFFFFF',
                              borderless=True, activeforeground='#FFFFFF', activebackground='#AAD1A9',
                              focusthickness=0)
        train_button.place(x=800, y=285)
        te_load_button = Button(root, text="Test data",
                                command=lambda: self.reset(root),
                                font=("Great Vibes", 16, "bold"), width=200, height=30, bg='#7AC578', fg='#FFFFFF',
                                borderless=True, activeforeground='#FFFFFF', activebackground='#AAD1A9',
                                focusthickness=0)
        te_load_button.place(x=400, y=620)

    def reset(self, root):
        root.destroy()
        MyApp()


if __name__ == '__main__':
    mp = MyApp()
