#!./bin/python
"""The Main entry point"""
from tkinter import Tk
from app import ToDoListApp


def main():
    """The main function"""
    root = Tk()
    ToDoListApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
