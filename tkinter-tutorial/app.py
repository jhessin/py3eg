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
    name: Variable
    description: Variable

    def __init__(self, root: Tk) -> None:
        # set the root title
        root.title('To Do List')

        # Create the root frame
        frame = Frame(root, borderwidth=2, relief='sunken')
        frame.grid(column=1, row=1, sticky='NESW')
        root.columnconfigure(1, weight=1)
        root.rowconfigure(1, weight=1)

        # Initialize Variables
        self.to_do_names = Variable(
            value=list(map(lambda x: x.name, self.to_do_items)))
        self.selected_description = Variable()
        self.name = Variable()
        self.description = Variable()

        # Create the items_list
        items_list = Listbox(frame, listvariable=self.to_do_names)
        items_list.bind(
            '<<ListboxSelect>>',
            lambda _: self.select_item(items_list.curselection()[0]))
        items_list.grid(column=1, row=2, sticky='WE')

        # Create the list_label
        list_label = Label(frame, text='To Do Items')
        list_label.grid(column=1, row=1, sticky='SW')

        # Create the selected_description_label
        selected_description_label = Label(
            frame,
            textvariable=self.selected_description,
            wraplength=150,
        )
        selected_description_label.grid(column=1, row=3, sticky='EW')

        # New Item frame
        new_item_frame = Frame(frame, borderwidth=2, relief='sunken')
        new_item_frame.grid(column=2, row=2, sticky='NESW')

        new_item_label = Label(new_item_frame, text='New Item')
        new_item_label.grid(column=1, row=1, sticky='SEW')

        name_label = Label(new_item_frame, text='Item name')
        name_label.grid(column=1, row=2, sticky='SW')

        name_entry = Entry(new_item_frame, textvariable=self.name)
        name_entry.grid(column=1, row=3, sticky='NEW')

        description_label = Label(
            new_item_frame,
            text='Item description',
        )
        description_label.grid(column=1, row=4, sticky='SW')

        description_entry = Entry(new_item_frame,
                                  textvariable=self.description)
        description_entry.grid(column=1, row=5, sticky='NEW')

        save_button = Button(new_item_frame,
                             text='Save',
                             command=self.save_item)
        save_button.grid(column=1, row=6, sticky='E')

        for child in frame.winfo_children():
            child.grid_configure(padx=10, pady=5)
        for child in new_item_frame.winfo_children():
            child.grid_configure(padx=10, pady=5)

    def select_item(self, index: int):
        """ Called when an item is selecte in the todolist """
        selected = self.to_do_items[index]
        self.selected_description.set(selected.description)

    def save_item(self):
        """ Save a new item """
        self.to_do_items.append(
            ToDoItem(self.name.get(), self.description.get()))
        self.to_do_names.set(
            value=list(map(lambda x: x.name, self.to_do_items)))
        self.description.set('')
        self.name.set('')
