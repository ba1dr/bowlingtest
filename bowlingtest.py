# -*- coding: utf-8 -*-

"""
    Script file: bowlingtest
"""

__author__ = "Alexey Kolyanov"
__email__ = "alexey.kolyanov@gmail.com"

from collections import defaultdict

# input
SCORES = [10, 3, 7, 6, 1, 10, 10, 10, 2, 8, 9, 0, 7, 3, 10, 10, 10]  # 193


def bowling10(scores):
    """
        Calculate scores for the 10 pin bowling.
        Inputs: list of integers (hits for the pins)
        returns: integer as total score
    """
    LASTFRAME = 9
    frame = 0  # current frame
    frames = defaultdict(list)
    pins = 10  # current state of the pins
    addframes = []  # list of frames to add additional scores

    for hit in scores:
        if pins == 0:
            pins = 10
            frame += 1 * (frame < LASTFRAME)
        pins -= hit
        frames[frame] += [hit]
        for af in addframes:  # add extra scores to previous frames
            frames[af.pop()] += [hit]  # pop() modifies the element!
        addframes = [af for af in addframes if af]  # shrink
        if frame < LASTFRAME:
            if pins == 0:
                if len(frames[frame]) == 1:  # strike!
                    addframes += [[frame, frame]]
                else:  # spare!
                    addframes += [[frame], ]
            elif len(frames[frame]) > 1:  # more than one hit made in the current frame
                pins = 0
    total = sum(sum(frames[fh]) for fh in frames)
    # output
    for f in sorted(frames.keys()):
        print("Frame %s: %s" % (f + 1, frames[f]))
    print("Total: %s" % total)
    return total


if __name__ == "__main__":
    bowling10(SCORES)
