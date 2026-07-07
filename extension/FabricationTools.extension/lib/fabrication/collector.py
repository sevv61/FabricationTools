# -*- coding: utf-8 -*-
"""
collector.py

Collects Autodesk Revit Fabrication Parts from the active document.

Target:
    Autodesk Revit 2023
"""

from Autodesk.Revit.DB import (
    BuiltInCategory,
    FilteredElementCollector
)


class FabricationCollector(object):
    """Collects Fabrication Parts from the active Revit document."""

    def __init__(self, doc):
        self.doc = doc
        self._parts = None

    def get_all_parts(self):
        """Return all Fabrication Parts in the document."""
        if self._parts is None:
            self._parts = list(
                FilteredElementCollector(self.doc)
                .OfCategory(BuiltInCategory.OST_FabricationDuctwork)
                .WhereElementIsNotElementType()
            )

        return self._parts

    def count(self):
        """Return the number of Fabrication Parts."""
        return len(self.get_all_parts())

    def first(self):
        """Return the first Fabrication Part, or None."""
        parts = self.get_all_parts()
        return parts[0] if parts else None

    def sample(self, size=10):
        """Return the first 'size' Fabrication Parts."""
        return self.get_all_parts()[:size]

    def refresh(self):
        """Clear the cache and recollect Fabrication Parts."""
        self._parts = None
        return self.get_all_parts()
    