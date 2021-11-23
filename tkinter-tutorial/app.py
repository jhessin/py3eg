""" The App class contains all app logic """
from tkinter import (
    Tk,
    Variable,
    Listbox,
    Entry,
    Button,
    Label,
    font,
)
from typing import List


class App:
    """The App class holds all global app variables"""
    root: Tk
    label_text: Variable
    entry_text: Variable
    list_item_strings: List[str]

    def __init__(self, root) -> None:
        # start by saving the root
        self.root = root
        self.root.title("My app")
        # sets the initial size (doesn't work in grid layouts)
        # root.geometry("500x400")
        # sets the maximum size of the window (Does work in grid layouts)
        # root.maxsize(500, 400)

        self.entry_text = Variable()
        self.label_text = Variable(value='New label text')

        # A label is a simple text object
        label = Label(
            root,
            text="Some label text",
        )
        # Two ways to set widget properties
        # label['text'] = "New label text"
        # label['font'] = ["Courier", 40]
        label.configure(
            text="New label text",
            font=['Courier', 30],
            textvariable=self.label_text,
        )
        # self.label.configure(textvariable=self.entry_text)
        entry = Entry(
            root,
            textvariable=self.entry_text,
        )

        button = Button(root, text="Submit", command=self.press_button)
        button.configure(width=10, height=2, font=('Courier', 40))

        self.list_item_strings = ['Hey', 'Hi', 'Hello', 'Howdy', 'Greetings']
        list_items = Variable(value=self.list_item_strings)
        listbox = Listbox(root, listvariable=list_items)
        listbox["height"] = 3
        listbox.bind('<<ListboxSelect>>',
                     lambda _: self.select_item(listbox.curselection()[0]))

        ### Location Location Location!

        # pack locates the widget in the default orientation tk.TOP
        # label.pack(side=tk.TOP)
        # listbox.pack(side=tk.LEFT, padx=20, pady=40)
        # button.pack(side=tk.LEFT)
        # entry.pack(side=tk.LEFT)

        # place allows us to locate widgets at specific coordinates
        # entry.place(x=50, y=50)
        # label.place(x=50, y=10)

        # label.grid(column=1, row=1)
        # entry.grid(column=3, row=1)
        # button.grid(column=1, row=2, sticky='SEW')
        # listbox.grid(column=2, row=2)

        button.place(x=0, y=0)

    def press_button(self):
        """Handle pressing the button"""
        self.label_text.set(self.entry_text.get())

    def select_item(self, index: int):
        """Get Selected Item"""
        selected_item = self.list_item_strings[index]
        self.entry_text.set(selected_item)

    def run(self) -> None:
        """ run the mainloop """
        self.root.mainloop()
