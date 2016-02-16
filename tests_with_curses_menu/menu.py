from cursesmenu import CursesMenu
from cursesmenu.items import FunctionItem

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


menu = NewCursesMenu('This is a menu', 'It has a subtitle too!')
news = [
    'New',
    'New',
    'New',
    'New',
    'New',
    'New',
    'New',
    'New',
    'New',
    'New',
    'New',
    'New',
    'New',
    'New',
    'New',
    'New',
    'New',
    'New',
    'New',
    'New',
    'New',
    'New',
    'New',
    'New',
    'New',
    'New',
    'New',
    'New',
    'New',
    'New',
    'New',
    'New',
]


def print_new():
    print('This is a new')

for new in news:
    menu.append_item(FunctionItem(new, print_new))


menu.show()
