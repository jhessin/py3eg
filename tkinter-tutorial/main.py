#!/usr/bin/env python3
"""The Main entry point"""
from tkinter import Tk
from app import App


def main():
    """The main function"""
    root = Tk()
    app = App(root)

    app.run()


if __name__ == '__main__':
    main()
