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
        self.rounds_won = IntVar()

        # random score test data
        self.all_scores_list = [0, 15, 16, 0, 16]
        self.all_high_score_list = [20, 19, 18, 20, 20]
        self.rounds_won.set(3)

        self.play_box = Toplevel()

        self.game_frame = Frame(self.play_box)
        self.game_frame.grid(padx=10, pady=10)

        self.heading_label = Label(self.game_frame, text="Colour Quest",
                                   font=("Arial", "16", "bold"), padx=5, pady=5)
        self.heading_label.grid(row=0)

        self.stats_button = Button(self.game_frame, font=("Arial", "14", "bold"),
                                   text="Stats", width=15, fg="#FFFFFF",
                                   bg="#FF8000", padx=10, pady=10, command=self.to_stats)
        self.stats_button.grid(row=1)

        self.close_button = Button(self.game_frame, font=("Arial", "14", "bold"),
                                   text="End", width=15, fg="#FFFFFF",
                                    bg="#FF8000", padx=10, pady=10, command=self.close_play)
        self.close_button.grid(row=2)


    def to_stats(self):
        """
        Retrieves everything we need to display the game / round stats
        :return:
        """
        # IMPORTANT: retrieve number of rounds
        # won as a number (rather than the 'self' container)
        rounds_won = self.rounds_won.get()
        stats_bundle = [rounds_won, self.all_scores_list,
                        self.all_high_score_list]
        DisplayStats(self, stats_bundle)


    def close_play(self):
        """reshows"""
        root.deiconify()
        self.play_box.destroy()


class DisplayStats:

    def __init__(self, partner, all_stats_info):

        # Extract information from master list
        rounds_won = all_stats_info[0]
        user_scores = all_stats_info[1]
        high_scores = all_stats_info[2]

        # sort user scores to find high score
        user_scores.sort()

        # setup dialogue box
        self.stats_box = Toplevel()

        # disable help button
        partner.stats_button.config(state=DISABLED)

        # if users press cross at top, closes help and
        # releases help button
        self.stats_box.protocol('WM_DELETE_WINDOW',
                                partial(self.close_stats, partner))

        bg_colour = "#FFE6CC"
        self.stats_frame = Frame(self.stats_box, width=300, height=200, bg=bg_colour)
        self.stats_frame.grid()

        # Math ti populate stats dialogue
        rounds_played = len(user_scores)

        success_rate = rounds_won / rounds_played * 100
        total_score = sum(user_scores)
        max_possible = sum(high_scores)

        best_score = user_scores[-1]
        average_score = total_score / rounds_played

        # strings for stats labels

        success_string = (f"Success Rate: {rounds_won} / {rounds_played} "
                          f"({success_rate:.0f}%)")
        total_score_string = f"Total Score: {total_score}"
        max_possible_string = f"Maximum Possible Score: {max_possible}"
        best_score_string = f"Best Score: {best_score}"

        # custom comment text and formatting
        if total_score == max_possible:
            comment_string = ("Amazing! You got the highest "
                              "possible score!")
            comment_colour = "#D5E8D4"

        elif total_score == 0:
            comment_string = ("Oops - You've lost every round! "
                              "You might want to look at the hints!")
            comment_colour = "#F8CECC"
            best_score_string = f"Best Score: n/a"

        else:
            comment_string = ""
            comment_colour = bg_colour

        average_score_string = f"Average Score: {average_score:.0f}\n"

        heading_font = ("Arial", "16", "bold")
        normal_font = ("Arial", "14")
        comment_font = ("Arial", "13")

        # Label list (text | font | 'sticky')
        all_stats_strings = [
            ["Statistics", heading_font,""],
            [success_string, normal_font, "W"],
            [total_score_string, normal_font, "W"],
            [max_possible_string, normal_font, "W"],
            [comment_string, comment_font, "W"],
            ["\nRound Stats", heading_font, ""],
            [best_score_string, normal_font, "W"],
            [average_score_string, normal_font, "W"]
        ]

        stats_label_ref_list = []
        for count, item in enumerate(all_stats_strings):
            self.stats_label = Label(self.stats_frame, text=item[0], font=item[1],
                                     anchor="w", justify="left",
                                     padx=30, pady=5, bg=bg_colour)
            self.stats_label.grid(row=count, sticky=item[2], padx=10)
            stats_label_ref_list.append(self.stats_label)

        # configure comment label background (for all won / all lost)
        stats_comment_label = stats_label_ref_list[4]
        stats_comment_label.config(bg=comment_colour)

        self.close_button = Button(self.stats_frame, text="Dismiss",
                                   bg="#333333", fg="#FFFFFF", width=20,
                                   font=("Arial", "12", "bold"),
                                   command=partial(self.close_stats, partner))
        self.close_button.grid(row=8, padx=10, pady=10)



    def close_stats(self, partner):
        """closes help box and re-enables help button"""
        # Put help button back to normal
        partner.stats_button.config(state=NORMAL)
        self.stats_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    StartGame()
    root.mainloop()