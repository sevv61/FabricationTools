# -*- coding: utf-8 -*-
"""
spacing.py

Calculates hanger insertion points for Fabrication Parts.

Target:
    Autodesk Revit 2023
"""

from hangers.hanger_point import HangerPoint
import Autodesk.Revit.DB as DB


class HangerSpacingEngine(object):
    """
    Calculates hanger insertion locations along a fabrication part.
    """

    def __init__(self, config):
        """
        Parameters
        ----------
        config : HangerConfiguration
        """
        self.config = config

    def calculate(self, geometry):
        """
        Calculate hanger insertion points.

        Parameters
        ----------
        geometry : GeometryInfo

        Returns
        -------
        list[HangerPoint]
        """

        points = []

        if geometry is None:
            return points

        if geometry.curve is None:
            return points

        length = geometry.length

        if length < self.config.minimum_length:
            return points

        direction = geometry.direction

        if direction is None:
            return points

        start = self.config.start_offset
        end = self.config.end_offset
        spacing = self.config.spacing

        usable_length = length - start - end

        if usable_length <= 0:
            return points

        current_distance = start

        while current_distance <= (length - end + 0.0001):

            location = geometry.start_point + direction.Multiply(current_distance)

            hanger = HangerPoint(
                location=location,
                station=current_distance
            )

            points.append(hanger)

            current_distance += spacing

        return points

    def count(self, geometry):
        """
        Return the number of calculated hanger locations.
        """

        return len(self.calculate(geometry))

    def first(self, geometry):
        """
        Return the first hanger point.
        """

        points = self.calculate(geometry)

        if points:
            return points[0]

        return None

    def last(self, geometry):
        """
        Return the last hanger point.
        """

        points = self.calculate(geometry)

        if points:
            return points[-1]

        return None