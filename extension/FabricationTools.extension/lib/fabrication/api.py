# -*- coding: utf-8 -*-
"""
api.py

High-level API for interacting with Revit Fabrication Parts.
Target: Revit 2023
"""

from lib.fabrication.collector import FabricationCollector


class FabricationAPI(object):
    """High-level access to Fabrication data."""

    def __init__(self, doc):
        self.doc = doc
        self.collector = FabricationCollector(doc)

    def get_all_parts(self):
        """Return all Fabrication Parts."""
        return self.collector.get_all_parts()

    def get_part_count(self):
        """Return total number of Fabrication Parts."""
        return self.collector.get_count()

    def get_straight_parts(self):
        """
        Placeholder for straight duct filtering.
        """
        return self.collector.get_straight_parts()

    def get_services(self):
        """
        Placeholder.

        Future version:
            Return unique fabrication services.
        """
        return []

    def get_fittings(self):
        """
        Placeholder.

        Future version:
            Return only fabrication fittings.
        """
        return []

    def get_accessories(self):
        """
        Placeholder.

        Future version:
            Return accessories.
        """
        return []

    def summary(self):
        """Return basic model statistics."""
        return {
            "parts": self.get_part_count(),
            "straight_parts": len(self.get_straight_parts()),
            "services": len(self.get_services()),
            "fittings": len(self.get_fittings()),
            "accessories": len(self.get_accessories()),
        }