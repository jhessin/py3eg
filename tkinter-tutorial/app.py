""" The App class contains all app logic """
from tkinter import (
    Label,
    StringVar,
    Tk,
    Entry,
)


class App:
    """The App class holds all global app variables"""
    root: Tk
    label: Label
    entry: Entry
    entry_text: StringVar

    def __init__(self, root) -> None:
        # start by saving the root
        self.root = root

        self.label = Label(
            root,
            text="Some label text",
        )
        self.label.pack()

        self.entry_text = StringVar()
        self.entry = Entry(root, textvariable=self.entry_text)
        self.entry.pack()

        # end by calling the initializer
        self.initialize_window()

    def initialize_window(self):
        """ Initializes the app """

        # Two ways to set widget properties
        # self.label['text'] = "New label text"
        # self.label['font'] = ["Courier", 40]
        self.label.configure(text="New label text", font=['Courier', 30])
        self.label.configure(textvariable=self.entry_text)

        self.root.title("My app")
        # sets the initial size (doesn't work in grid layouts)
        # root.geometry("500x400")

        # sets the maximum size of the window (Does work in grid layouts)
        # root.maxsize(500, 400)

    def run(self) -> None:
        """ run the mainloop """
        self.root.mainloop()
