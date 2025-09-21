import curses
import random
import time

from effect import matrix_effect

def main():
    stdscr = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    try:
        matrix_effect(stdscr)
    finally:
        curses.endwin()


if __name__ == "__main__":
    main()