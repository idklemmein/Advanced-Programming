from tkinter import *
from functools import partial    # to prevent unwanted windows


class Converter:
    """
    Temperature conversion tool (C* to F* or F* to C*)
    """

    def __init__(self):

        """
        Temperature converter GUI
        """

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.to_history_button = Button(self.temp_frame,
                                        text="History / Export",
                                        bg="#CC6600",
                                        fg="#FFFFFF",
                                        font)