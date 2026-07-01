# -*- coding: utf-8 -*-
"""
collector.py

Fabrication element collection utilities.

Author: Sam Vanvalkenbugh
Project: Fabrication Tools
"""

from Autodesk.Revit.DB import FilteredElementCollector
from Autodesk.Revit.DB.Fabrication import FabricationPart


class FabricationCollector(object):
    """
    Collects FabricationPart elements from the active Revit document.
    """

    def __init__(self, doc):
        self.doc = doc

    def get_all_parts(self):
        """
        Returns a list of all FabricationPart objects.
        """
        return list(
            FilteredElementCollector(self.doc)
            .OfClass(FabricationPart)
            .WhereElementIsNotElementType()
        )

    def get_part_count(self):
        """
        Returns the total number of fabrication parts.
        """
        return len(self.get_all_parts())

    def get_sample(self, count=10):
        """
        Returns the first few fabrication parts.
        """
        return self.get_all_parts()[:count]