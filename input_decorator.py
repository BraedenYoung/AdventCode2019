import datetime
import os
import time

from termcolor import cprint


def has_input(part):
    def wrapper():
        """
        Surrounds the call with a timer and reads in the input file for the
        challenge
        """

        day = datetime.datetime.now().day

        decorator_dir = os.path.dirname(__file__)
        rel_path = 'day%02d/input.txt' % day

        with open(os.path.join(decorator_dir, rel_path), 'r') as input_file:
            input_text = input_file.read()

        cprint("Part %s for day %s" % (01, day), 'magenta')
        print ' '

        start = time.time()
        part(input_text)

        cprint("Process time: %s" % (time.time() - start), 'yellow')

    return wrapper
