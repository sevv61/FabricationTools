# -*- coding: utf-8 -*-
"""
geometry.py

Geometry helper functions for Fabrication Parts.

Target:
    Autodesk Revit 2023
"""

from Autodesk.Revit.DB import LocationCurve


class GeometryInfo(object):
    """Geometry helper for Fabrication Parts."""

    def __init__(self, part):
        self.part = part

    @property
    def direction(self):
        """
        Unit direction vector from start to end.
        """
        if self.curve:
            return (self.end_point - self.start_point).Normalize()

        return None

    @property
    def direction(self):
        """
        Unit direction vector from start to end.
        """
        if self.curve:
            return (self.end_point - self.start_point).Normalize()

        return None
    
    @property
    def midpoint(self):
        """
        Midpoint of the fabrication part.
        """
        if self.curve:
            return self.curve.Evaluate(0.5, True)

        return None
    

    @property
    def is_horizontal(self):
        """
        True if essentially horizontal.
        """
        if not self.direction:
         return False

        return abs(self.direction.Z) < 0.001


    @property
    def is_vertical(self):
        """
        True if essentially vertical.
        """
        if not self.direction:
            return False

        return abs(self.direction.Z) > 0.999


    @property
    def is_sloped(self):
        """
        True if neither horizontal nor vertical.
        """
        return not self.is_horizontal and not self.is_vertical

    @property
    def location_curve(self):
        """Return the element's LocationCurve."""
        location = self.part.Location

        if isinstance(location, LocationCurve):
            return location

        return None

    @property
    def curve(self):
        """Return the underlying Revit curve."""
        if self.location_curve:
            return self.location_curve.Curve

        return None

    @property
    def start_point(self):
        """Curve start point."""
        if self.curve:
            return self.curve.GetEndPoint(0)

        return None

    @property
    def end_point(self):
        """Curve end point."""
        if self.curve:
            return self.curve.GetEndPoint(1)

        return None

    @property
    def length(self):
        """Curve length (Revit internal units = feet)."""
        if self.curve:
            return self.curve.Length

        return 0.0