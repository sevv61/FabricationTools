# -*- coding: utf-8 -*-
"""
collector.py

Collects Autodesk Revit FabricationPart elements from the active document.

Author: Sam Vanvalkenbugh
Target: Autodesk Revit 2023
"""

from Autodesk.Revit.DB import FilteredElementCollector
from Autodesk.Revit.DB.Fabrication import FabricationPart


class FabricationCollector(object):
    """Collects FabricationPart elements from a Revit document."""

    def __init__(self, doc):
        """
        Initialize the collector.

        Args:
            doc (Autodesk.Revit.DB.Document):
                The active Revit document.
        """
        self.doc = doc
        self._parts = None

    def get_all_parts(self):
        """
        Return all FabricationPart elements in the document.

        The results are cached so Revit is only queried once during
        the lifetime of this collector instance.
        """
        if self._parts is None:
            self._parts = list(
                FilteredElementCollector(self.doc)
                .OfClass(FabricationPart)
                .WhereElementIsNotElementType()
            )

        return self._parts

    def count(self):
        """
        Return the total number of Fabrication Parts.
        """
        return len(self.get_all_parts())

    def first(self):
        """
        Return the first Fabrication Part, or None if no parts exist.
        """
        parts = self.get_all_parts()

        if parts:
            return parts[0]

        return None

    def sample(self, size=10):
        """
        Return the first 'size' Fabrication Parts.

        Args:
            size (int):
                Number of sample parts to return.
        """
        return self.get_all_parts()[:size]

    def by_service(self, service_name):
        """
        Return all Fabrication Parts belonging to a service.

        Args:
            service_name (str):
                Fabrication service name.

        Returns:
            list[FabricationPart]
        """
        matches = []

        for part in self.get_all_parts():
            try:
                if part.ServiceName == service_name:
                    matches.append(part)
            except Exception:
                # Ignore parts that don't expose ServiceName
                pass

        return matches

    def refresh(self):
        """
        Clear the cache and reload Fabrication Parts.
        """
        self._parts = None
        return self.get_all_parts()