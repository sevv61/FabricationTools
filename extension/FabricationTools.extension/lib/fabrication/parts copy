# -*- coding: utf-8 -*-
"""
parts.py

Wrapper around Autodesk Revit FabricationPart objects.

Provides a safe, Pythonic interface for accessing fabrication
properties and geometry information.

Target:
    Autodesk Revit 2023
"""

from geometry.geometry import GeometryInfo


class FabricationPartInfo(object):
    """
    Wrapper around Autodesk.Revit.DB.Fabrication.FabricationPart.
    """

    def __init__(self, part):
        self._part = part

    # ----------------------------------------------------------
    # Core Element Access
    # ----------------------------------------------------------

    @property
    def element(self):
        """
        Return underlying Revit element.
        """
        return self._part

    @property
    def id(self):
        """
        Element Id as integer.
        """
        try:
            return self._part.Id.IntegerValue
        except Exception:
            return None

    @property
    def unique_id(self):
        """
        Revit UniqueId.
        """
        try:
            return self._part.UniqueId
        except Exception:
            return ""

    @property
    def is_valid(self):
        """
        True if Revit element is still valid.
        """
        try:
            return self._part.IsValidObject
        except Exception:
            return False

    # ----------------------------------------------------------
    # Classification
    # ----------------------------------------------------------

    @property
    def name(self):
        """
        Fabrication part name.
        """
        try:
            return self._part.Name
        except Exception:
            return "<Unavailable>"

    @property
    def category(self):
        """
        Revit category name.
        """
        try:
            return self._part.Category.Name
        except Exception:
            return "<None>"

    @property
    def service(self):
        """
        Fabrication service name.
        """
        try:
            return self._part.ServiceName
        except Exception:
            return "<Unavailable>"

    @property
    def item_number(self):
        """
        Fabrication item number.
        """
        try:
            return self._part.ItemNumber
        except Exception:
            return "<Unavailable>"

    # ----------------------------------------------------------
    # Geometry
    # ----------------------------------------------------------

    @property
    def geometry(self):
        """
        Return GeometryInfo wrapper.
        """
        return GeometryInfo(self._part)

    @property
    def length(self):
        """
        Convenience access to geometry length.
        """
        return self.geometry.length

    @property
    def start_point(self):
        """
        Convenience access to start point.
        """
        return self.geometry.start_point

    @property
    def end_point(self):
        """
        Convenience access to end point.
        """
        return self.geometry.end_point

    # ----------------------------------------------------------
    # Reporting
    # ----------------------------------------------------------

    def as_dict(self):
        """
        Convert commonly used values to dictionary.
        Useful for reports and debugging.
        """
        return {
            "id": self.id,
            "unique_id": self.unique_id,
            "name": self.name,
            "category": self.category,
            "service": self.service,
            "item_number": self.item_number,
            "length": self.length,
            "is_valid": self.is_valid,
        }

    def __str__(self):
        return "{} ({})".format(self.name, self.id)

    def __repr__(self):
        return "<FabricationPartInfo {}>".format(self.id)