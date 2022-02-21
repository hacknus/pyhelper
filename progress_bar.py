import time
import sys


class Bar:

    def __init__(self, max, width=50):
        self.max = max
        self.width = width

    def update(self, i):
        time.sleep(0.1)  # do real work here
        # update the bar
        j = int(i / self.max * self.width)
        bar = "#" * j + " " * (self.width - j) + f" {i + 1}/{self.max}\r"
        sys.stdout.write(bar)
        sys.stdout.flush()
        if i == self.max - 1:
            sys.stdout.write("\n")
            sys.stdout.flush()


if __name__ == "__main__":
    # setup progress bar
    max = 10
    progress_bar = Bar(max)
    # run progress bar
    for i in range(max):
        progress_bar.update(i)
