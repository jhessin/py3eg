""" The App class contains all app logic """
from tkinter import Button, Entry, Frame, Label, Listbox, Tk, Variable
from typing import List

from todo import ToDoItem


class ToDoListApp:
    """The App class holds all global app variables"""
    to_do_items: List[ToDoItem] = [
        ToDoItem('Workout', 'Push ups, pull ups, squats'),
        ToDoItem('House work', 'Clean kitchen, sweep floors, do laundry'),
        ToDoItem('Groceries', 'Buy bread, milk, eggs')
    ]
    to_do_names: Variable
    selected_description: Variable

    def __init__(self, root: Tk) -> None:
        # start by saving the root
        root.title('To Do List')

        frame = Frame(root, borderwidth=2, relief='sunken')
        frame.grid(column=1, row=1, sticky='NESW')
        root.columnconfigure(1, weight=1)
        root.rowconfigure(1, weight=1)

        self.to_do_names = Variable(
            value=list(map(lambda x: x.name, self.to_do_items)))

        items_list = Listbox(frame, listvariable=self.to_do_names)
        items_list.bind(
            '<<ListboxSelect>>',
            lambda _: self.select_item(items_list.curselection()[0]))
        items_list.grid(column=1, row=2, sticky='WE')

        list_label = Label(frame, text='To Do Items')
        list_label.grid(column=1, row=1, sticky='SW')

        self.selected_description = Variable()
        selected_description_label = Label(
            frame, textvariable=self.selected_description)
        selected_description_label.grid(column=1, row=3, sticky='EW')

    def select_item(self, index: int):
        selected = self.to_do_items[index]
        self.selected_description.set(selected.description)
