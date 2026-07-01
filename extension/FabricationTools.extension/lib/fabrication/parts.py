FabricationPartWrapper
# -*- coding: utf-8 -*-
"""
parts.py

Wrapper for Autodesk Revit FabricationPart objects.
Target: Revit 2023
"""

from Autodesk.Revit.DB import LocationCurve


class FabricationPartWrapper(object):
    """Wraps a Revit FabricationPart with convenient properties."""

    def __init__(self, part):
        self.part = part

    @property
    def id(self):
        return self.part.Id.IntegerValue

    @property
    def unique_id(self):
        return self.part.UniqueId

    @property
    def name(self):
        return self.part.Name

    @property
    def category(self):
        if self.part.Category:
            return self.part.Category.Name
        return "Unknown"

    @property
    def location_curve(self):
        loc = self.part.Location
        if isinstance(loc, LocationCurve):
            return loc.Curve
        return None

    @property
    def length(self):
        curve = self.location_curve
        if curve:
            return curve.Length
        return 0.0

    @property
    def connector_count(self):
        try:
            return self.part.ConnectorManager.Connectors.Size
        except:
            return 0

    def __repr__(self):
        return "<FabricationPartWrapper {} ({})>".format(
            self.id,
            self.name
        )