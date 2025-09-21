import curses
import random
import time

def matrix_effect(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(10)

    # Отримати розміри екрану
    height, width = stdscr.getmaxyx()

    columns = [0] * width
    symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$%#@!*&^()"

    try:
        while True:
            if stdscr.getch() == ord('q'):
                break

            stdscr.clear()

            for i in range(width):
                if columns[i] > 0:
                    char = random.choice(symbols)

                    if random.random() < 0.1:
                        stdscr.addstr(columns[i] - 1, i, char, curses.color_pair(1))
                    else:
                        stdscr.addstr(columns[i] - 1, i, char, curses.color_pair(2))

                if columns[i] < height - 1 and random.random() < 0.8:
                    columns[i] += 1
                else:
                    if random.random() < 0.05:
                        columns[i] = 0

            stdscr.refresh()
            time.sleep(0.05)

    except KeyboardInterrupt:
        pass