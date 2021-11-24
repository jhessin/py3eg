from enum import Enum
import tkinter as tk
import tkinter.colorchooser
from PIL import ImageGrab
from datetime import datetime


class Tool(Enum):
    PEN = 1
    ERASE = 2


class PixelApp:
    tool: Tool = Tool.PEN

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title('Pixel Art')

        cell_length = 50
        grid_width = 20
        grid_height = 10

        self.color_chooser = tkinter.colorchooser.Chooser(self.root)
        self.chosen_color = 'white'

        self.drawing_grid = tk.Canvas(self.root)
        self.drawing_grid.grid(column=0, row=0, sticky='NESW')

        self.cells = []
        for x in range(grid_width):
            for y in range(grid_height):
                cell = tk.Frame(
                    self.drawing_grid,
                    width=cell_length,
                    height=cell_length,
                    bg='white',
                    highlightbackground='black',
                    highlightcolor='black',
                    highlightthickness=1,
                )
                cell.bind('<Button-1>', self.tap_cell)
                cell.grid(column=x, row=y)
                self.cells.append(cell)

        control_frame = tk.Frame(
            self.root,
            height=cell_length,
        )
        control_frame.grid(column=0, row=1, sticky='NESW')

        new_button = tk.Button(
            control_frame,
            text='New',
            command=self.press_new,
        )
        new_button.grid(
            column=0,
            row=0,
            columnspan=2,
            sticky='NESW',
            padx=5,
            pady=5,
        )

        save_button = tk.Button(
            control_frame,
            text='Save',
            command=self.press_save,
        )
        save_button.grid(
            column=2,
            row=0,
            columnspan=2,
            sticky='NESW',
            padx=5,
            pady=5,
        )

        self.pencil_image = tk.PhotoImage(file='assets/pencil.png').subsample(
            2, 3)
        pen_button = tk.Button(
            control_frame,
            image=self.pencil_image,
            text='Pen',
            command=self.press_pen,
        )
        pen_button.grid(
            column=8,
            row=0,
            columnspan=2,
            sticky='NESW',
            padx=5,
            pady=5,
        )

        self.erase_image = tk.PhotoImage(file='assets/eraser.png').subsample(
            2, 3)
        erase_button = tk.Button(
            control_frame,
            image=self.erase_image,
            text='Erase',
            command=self.press_clear,
        )
        erase_button.grid(
            column=10,
            row=0,
            columnspan=2,
            sticky='NESW',
            padx=5,
            pady=5,
        )

        self.selected_color_box = tk.Frame(
            control_frame,
            borderwidth=2,
            relief='raised',
            bg=self.chosen_color,
        )
        self.selected_color_box.grid(
            column=15,
            row=0,
            sticky='NESW',
            padx=5,
            pady=8,
        )

        pick_color_button = tk.Button(
            control_frame,
            text='Pick Color',
            command=self.pick_color,
        )
        pick_color_button.grid(
            column=17,
            row=0,
            columnspan=3,
            sticky='NESW',
            padx=5,
            pady=5,
        )

        cols, _ = control_frame.grid_size()

        for col in range(cols):
            control_frame.columnconfigure(col, minsize=cell_length)
        control_frame.rowconfigure(0, minsize=cell_length)

    def tap_cell(self, event: tk.Event):
        widget = event.widget
        match self.tool:
            case Tool.ERASE:
                widget['bg'] = 'white'
            case Tool.PEN:
                widget['bg'] = self.chosen_color

    def press_new(self):
        for cell in self.cells:
            cell['bg'] = 'white'
        self.chosen_color = 'white'
        self.tool = Tool.PEN
        self.selected_color_box['bg'] = 'white'

    def press_save(self):
        x = self.root.winfo_rootx() + self.drawing_grid.winfo_x()
        y = self.root.winfo_rooty() + self.drawing_grid.winfo_y()
        width = x + 1000
        height = y + 500

        image_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.png'

        ImageGrab.grab(bbox=(x, y, width, height)).save(image_name)

    def press_pen(self):
        self.tool = Tool.PEN

    def press_clear(self):
        self.tool = Tool.ERASE

    def pick_color(self):
        color_info = self.color_chooser.show()
        self.chosen_color = color_info[1] or self.chosen_color
        self.selected_color_box.configure(bg=self.chosen_color)

    def mainloop(self):
        self.root.mainloop()
