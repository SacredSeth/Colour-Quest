from tkinter import *
from functools import partial


class StartGame:
    """
    Initial Game Interface (asks user how many rounds they
    would like to play)
    """

    def __init__(self):
        """
        Gets number of rounds from user
        """

        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # create play button
        self.play_button = Button(self.start_frame, font = ("Arial", "16", "bold"),
                                  fg = "#FFFFFF", bg="#0057D8", text="Play", width=30,
                                  command=self.check_rounds)
        self.play_button.grid(row=0, column=1, padx=20, pady=20)

    def check_rounds(self):
        """
        Checks users have entered 1 or more rounds
        :return:
        """

        # retrieve rounds wanted
        rounds_wanted = 5
        self.to_play(rounds_wanted)

    def to_play(self, num_rounds):
        """
        Invokes Game GUI and takes across number of rounds to be played
        :param num_rounds:
        :return:
        """
        Play(num_rounds)
        # hide root window
        root.withdraw()


class Play:
    """
    Interface for playing the Colour Quest Game
    """

    def __init__(self, how_many):
        self.play_box = Toplevel()

        self.game_frame = Frame(self.play_box)
        self.game_frame.grid(padx=10, pady=10)

        self.heading_label = Label(self.game_frame, text="Colour Quest",
                                   font=("Arial", "16", "bold"), padx=5, pady=5)
        self.heading_label.grid(row=0)

        self.hints_button = Button(self.game_frame, font=("Arial", "14", "bold"),
                                   text="Hints", width=15, fg="#FFFFFF",
                                   bg="#FF8000", padx=10, pady=10, command=self.to_hints)
        self.hints_button.grid(row=1)


    def to_hints(self):
        """
        Displays hints for playing game
        :return:
        """
        DisplayHints(self)


    def close_play(self):
        """reshows"""


class DisplayHints:

    def __init__(self, partner):

        # setup dialogue box
        self.hint_box = Toplevel()

        # disable help button
        partner.hints_button.config(state=DISABLED)

        # if users press cross at top, closes help and
        # releases help button
        self.hint_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_hints, partner))

        bg_colour = "#FFE6CC"
        self.hint_frame = Frame(self.hint_box, width=300, height=200, bg=bg_colour)
        self.hint_frame.grid()

        self.hint_heading = Label(self.hint_frame,
                                  text="Help / Information",
                                  font=("Arial", "14", "bold"),
                                  bg=bg_colour)
        self.hint_heading.grid(row=0)

        hint_instructions = ("To use the program, simply enter the temperature "
                             "you wish to convert and then choose to convert to "
                             "either degrees Celsius (centigrade) or Fahrenheit."
                             "\n\n"
                             "Note that -273 degrees C (-459 F) is absolute zero "
                             "(the coldest possible temperature). If you try to "
                             "convert a temperature that is less than -273 degrees "
                             "C, you will get an error message. \n\n"
                             "To see your "
                             "calculation history and export it to a text file, please "
                             "click the 'History / Export' button.")
        self.hint_text = Label(self.hint_frame,
                               text=hint_instructions,
                               wraplength=350,
                               justify="left",
                               bg=bg_colour)
        self.hint_text.grid(row=1, padx=10)

        self.close_button = Button(self.hint_frame, text="Close",
                                   bg="#CC6600", fg="#FFFFFF",
                                   font=("Arial", "12", "bold"),
                                   command=partial(self.close_hints, partner))
        self.close_button.grid(row=2, padx=10, pady=10)



    def close_hints(self, partner):
        """closes help box and re-enables help button"""
        # Put help button back to normal
        partner.hints_button.config(state=NORMAL)
        self.hint_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    StartGame()
    root.mainloop()