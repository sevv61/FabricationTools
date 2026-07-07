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