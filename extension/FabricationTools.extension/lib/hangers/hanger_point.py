# -*- coding: utf-8 -*-

"""
hanger_point.py

Represents a calculated hanger location.
"""

import Autodesk.Revit.DB as DB


class HangerPoint(object):
    """
    Represents one hanger insertion point.
    """

    def __init__(self,
                 location,
                 station):

        if not isinstance(location, DB.XYZ):
            raise TypeError("location must be DB.XYZ")

        self.location = location

        # Distance along the duct centerline (feet)
        self.station = float(station)

        # Placement flags
        self.is_start_hanger = False
        self.is_end_hanger = False

        # Validation
        self.is_valid = True
        self.skip = False

        # Filled in later
        self.host = None
        self.service = ""
        self.hanger_type = ""

        # Diagnostics
        self.notes = []

    @property
    def x(self):
        return self.location.X

    @property
    def y(self):
        return self.location.Y

    @property
    def z(self):
        return self.location.Z

    def add_note(self, note):
        self.notes.append(str(note))

    def __repr__(self):

        return (
            "HangerPoint("
            "station={:.2f}, "
            "XYZ=({:.3f}, {:.3f}, {:.3f}))"
        ).format(
            self.station,
            self.x,
            self.y,
            self.z
        )