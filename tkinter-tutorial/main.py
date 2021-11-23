#!/usr/bin/env python3
"""The Main entry point"""
from tkinter import Tk
from app import ToDoListApp


def main():
    """The main function"""
    root = Tk()
    app = ToDoListApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
