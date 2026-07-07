# -*- coding: utf-8 -*-
"""
parts.py

Wrapper around Autodesk Revit FabricationPart.

This class provides a safe, Pythonic interface to FabricationPart
properties and isolates the rest of the project from direct Revit API
calls.

Author: Sam Vanvalkenbugh
Target: Autodesk Revit 2023
"""



class FabricationPartInfo(object):
    """Wrapper for Autodesk.Revit.DB.Fabrication.FabricationPart."""

    def __init__(self, part):
        self._part = part

    @property
    def element(self):
        """Return the underlying Revit element."""
        return self._part

    @property
    def id(self):
        """Element Id as an integer."""
        try:
            return self._part.Id.IntegerValue
        except Exception:
            return None

    @property
    def unique_id(self):
        """Revit UniqueId."""
        try:
            return self._part.UniqueId
        except Exception:
            return ""

    @property
    def name(self):
        """Element name."""
        try:
            return self._part.Name
        except Exception:
            return "<Unavailable>"

    @property
    def category(self):
        """Category name."""
        try:
            return self._part.Category.Name
        except Exception:
            return "<None>"

    @property
    def category_id(self):
        """BuiltInCategory integer value."""
        try:
            return self._part.Category.Id.IntegerValue
        except Exception:
            return None

    @property
    def service(self):
        """
        Fabrication Service Name.

        Some FabricationPart objects may not expose this property,
        so return '<Unavailable>' instead of raising an exception.
        """
        try:
            return self._part.ServiceName
        except Exception:
            return "<Unavailable>"

    @property
    def item_number(self):
        """Fabrication item number."""
        try:
            return self._part.ItemNumber
        except Exception:
            return "<Unavailable>"

    @property
    def is_valid(self):
        """True if the Revit element is still valid."""
        try:
            return self._part.IsValidObject
        except Exception:
            return False

    @property
    def is_fabrication_part(self):
        """Always True for wrapped objects."""
        return True

    def as_dict(self):
        """
        Return commonly used information as a dictionary.

        Useful for reporting, debugging, and exporting.
        """
        return {
            "id": self.id,
            "unique_id": self.unique_id,
            "name": self.name,
            "category": self.category,
            "service": self.service,
            "item_number": self.item_number,
            "is_valid": self.is_valid,
        }

    def __str__(self):
        return "{} ({})".format(self.name, self.id)

    def __repr__(self):
        return "<FabricationPartInfo {}>".format(self.id)