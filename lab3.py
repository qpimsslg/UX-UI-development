import curses
import time

def string(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    stdscr.timeout(100)

    text = "Бегущая строка... бежит! "
    text_length = len(text)
    start_x = curses.COLS

    while True:
        stdscr.clear()

        visible_text = ""
        for i in range(curses.COLS):
            char_index = (start_x + i) % text_length
            visible_text += text[char_index]

        try:
            stdscr.addstr(0, 0, visible_text, curses.color_pair(1))
        except curses.error:
            pass

        stdscr.refresh()
        start_x -= 1

        if start_x < 0:
            start_x += text_length

        time.sleep(0.1)

        key = stdscr.getch()
        if key != -1:
            break

if __name__ == "__main__":
    curses.wrapper(string)