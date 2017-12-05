import datetime
import importlib
import os
import shutil
import sys

import requests
from termcolor import cprint


def get_year_day():
    now = datetime.datetime.now()
    return now.year, now.day


YEAR, DAY = get_year_day()


def main():
    exercise = sys.argv[1]

    if not os.path.exists(get_relative_path()):
        cprint("FIRST RUN", 'red')
        setup_test_dir()
        get_day_input(sys.argv[2])

    if exercise == '1':
        importlib.import_module('.solution', package='day%02d' % DAY).part_one()
    elif exercise == '2':
        importlib.import_module('.solution', package='day%02d' % DAY).part_two()


def get_relative_path():
    """
    Returns the relative path of the current day
    """
    decorator_dir = os.path.dirname(__file__)
    rel_path = 'day%02d/' % DAY
    return os.path.join(decorator_dir, rel_path)


def setup_test_dir():
    """
    Create a new Folder based on the day and populate it with a template python
    solution module
    """
    template_path = os.path.dirname(__file__) + '/template/'
    dest_path = get_relative_path()

    if os.path.exists(dest_path):
        return

    os.makedirs(dest_path)

    shutil.copy('{path}{file_name}'.format(path=template_path, file_name='__init__.py'),
                '{path}{file_name}'.format(path=dest_path, file_name='__init__.py'))

    shutil.copy('{path}{file_name}'.format(path=template_path, file_name='solution.py'),
                '{path}{file_name}'.format(path=dest_path, file_name='solution.py'))


def get_day_input(session):
    """
    Pulls down the input based on the current year/day. Requires the user session.
    """
    r = requests.get(
        'http://adventofcode.com/{year}/day/{day}/input'.format(year=YEAR, day=DAY),
        cookies=dict(session=session))

    input_text = r.text

    with open('{directory}{filename}'.format(directory=get_relative_path(),
                                             filename='input.txt'), 'w') as input_file:
        input_file.write(input_text)


if __name__ == '__main__':
    main()
