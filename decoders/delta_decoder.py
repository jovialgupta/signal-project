import numpy as np


def delta_decode(bitstream, step_size=0.1, initial_value=0.0):
    current = initial_value
    staircase = [current]