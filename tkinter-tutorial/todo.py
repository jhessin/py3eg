""" The ToDoItem that can be referenced """


class ToDoItem:
    """ The ToDoItem holds the name and description """
    name: str
    description: str

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
