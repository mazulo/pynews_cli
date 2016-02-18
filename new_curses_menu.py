from cursesmenu import CursesMenu

import curses


class NewCursesMenu(CursesMenu):

    def process_user_input(self):
        user_input = self.get_input()

        if user_input == curses.KEY_DOWN:
            self.go_down()
        elif user_input == curses.KEY_UP:
            self.go_up()
        elif user_input == ord("\n"):
            self.select()
