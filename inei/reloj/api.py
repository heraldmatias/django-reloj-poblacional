# -*- coding -*-
from datetime import datetime

__author__ = 'holivares'

from constants import *


def intWith(character, x):
    if type(x) not in [type(0), type(0L)]:
        raise TypeError("Parameter must be an integer.")
    if x < 0:
        return '-' + intWith(character, -x)
    result = ''
    while x >= 1000:
        x, r = divmod(x, 1000)
        result = "%s%03d%s" % (character, r, result)
    return "%d%s" % (x, result)


class Api(object):

    def __init__(self, year):
        self.year = year

    def get_estimated_population(self):
        if self.year == YEAR:
            end_date = datetime.today()
            duration = (end_date - START_DATE)
            seconds = (duration.microseconds + (duration.seconds + duration.days * 24 * 3600) * 10**6) / 10**6
            population = int(POPULATION + round((seconds/COUNTER), 1))
            return population
        return POPULATION

    def get_elapsed_time(self):
        if self.year == YEAR:
            end_date = datetime.today()
            duration = (end_date - START_DATE)
            seconds = (duration.microseconds + (duration.seconds + duration.days * 24 * 3600) * 10**6) / 10**6
            initial_seconds = seconds
            population = seconds/COUNTER
            next_population = population + 1
            while population != next_population:
                seconds += 1
                population = seconds/COUNTER
            return seconds - initial_seconds