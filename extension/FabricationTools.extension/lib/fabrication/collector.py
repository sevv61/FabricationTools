# -*- coding: utf-8 -*-
"""
collector.py

Collect FabricationPart elements from the active Revit document.

Target:
    Autodesk Revit 2023
"""

from Autodesk.Revit.DB import FilteredElementCollector
from Autodesk.Revit.DB.Fabrication import FabricationPart


class FabricationCollector(object):
    """Collects FabricationPart objects."""

    def __init__(self, doc):
        self.doc = doc

    def get_all_parts(self):
        return list(
            FilteredElementCollector(self.doc)
            .OfClass(FabricationPart)
            .WhereElementIsNotElementType()
        )

    def count(self):
        return len(self.get_all_parts())

    def first(self):
        parts = self.get_all_parts()
        return parts[0] if parts else None

    def sample(self, size=10):
        return self.get_all_parts()[:size]

    def by_service(self, service_name):
        results = []

        for part in self.get_all_parts():
            try:
                if part.ServiceName == service_name:
                    results.append(part)
            except Exception:
                pass

        return results