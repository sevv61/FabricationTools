# -*- coding: utf-8 -*-
"""
collector.py

Collects Autodesk Revit Fabrication Parts from the active document.

Target:
    Autodesk Revit 2023
"""

from Autodesk.Revit.DB import FilteredElementCollector
import Autodesk.Revit.DB as DB


class FabricationCollector(object):

    def __init__(self, doc):
        self.doc = doc

    def get_all_parts(self):
        return list(
            DB.FilteredElementCollector(self.doc)
              .OfClass(DB.FabricationPart)
              .WhereElementIsNotElementType()
        )
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
    