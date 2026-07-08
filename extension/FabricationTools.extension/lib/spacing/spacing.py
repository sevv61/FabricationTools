# -*- coding: utf-8 -*-

"""
spacing.py

Calculates hanger locations along a fabrication part.
"""

import Autodesk.Revit.DB as DB


class HangerSpacingEngine(object):

    def __init__(self,
                 start_offset=1.0,
                 end_offset=1.0,
                 spacing=8.0):

        # feet (internal Revit units)
        self.start_offset = start_offset
        self.end_offset = end_offset
        self.spacing = spacing

    def calculate(self, geometry):
        """
        Returns a list of XYZ hanger insertion points.
        """

        points = []

        length = geometry.length

        usable = length - self.start_offset - self.end_offset

        if usable <= 0:
            return points

        direction = geometry.direction

        current = self.start_offset

        while current <= length - self.end_offset + 0.0001:

            point = geometry.start_point + direction.Multiply(current)

            points.append(point)

            current += self.spacing

        return points