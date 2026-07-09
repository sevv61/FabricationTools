# -*- coding: utf-8 -*-
"""
hanger_point.py

Represents a calculated hanger location for a Fabrication Part.

Target:
    Autodesk Revit 2023
"""

import Autodesk.Revit.DB as DB


class HangerPoint(object):
    """
    Represents one calculated hanger insertion point.
    """

    STATUS_VALID = "Valid"
    STATUS_WARNING = "Warning"
    STATUS_INVALID = "Invalid"

    def __init__(self,
                 location,
                 station):

        if not isinstance(location, DB.XYZ):
            raise TypeError(
                "location must be Autodesk.Revit.DB.XYZ"
            )

        # ------------------------------------------------------------------
        # Geometry
        # ------------------------------------------------------------------

        self.location = location

        # Distance from start of duct (feet)
        self.station = float(station)

        # Filled in by the spacing engine
        self.direction = None

        # ------------------------------------------------------------------
        # Host Information
        # ------------------------------------------------------------------

        self.host = None

        self.service = ""

        self.part_name = ""

        self.part_id = None

        # ------------------------------------------------------------------
        # Placement
        # ------------------------------------------------------------------

        self.is_start_hanger = False

        self.is_end_hanger = False

        self.is_trapeze = False

        self.is_single_rod = True

        # ------------------------------------------------------------------
        # Validation
        # ------------------------------------------------------------------

        self.status = self.STATUS_VALID

        self.skip = False

        self.skip_reason = ""

        # ------------------------------------------------------------------
        # Future Placement Data
        # ------------------------------------------------------------------

        self.hanger_family = ""

        self.rod_length = None

        self.rod_diameter = None

        self.structure = None

        # ------------------------------------------------------------------
        # Diagnostics
        # ------------------------------------------------------------------

        self.notes = []

    # ==========================================================
    # Coordinate Helpers
    # ==========================================================

    @property
    def x(self):
        return self.location.X

    @property
    def y(self):
        return self.location.Y

    @property
    def z(self):
        return self.location.Z

    # ==========================================================
    # Status Helpers
    # ==========================================================

    @property
    def is_valid(self):
        return self.status == self.STATUS_VALID

    @property
    def has_warning(self):
        return self.status == self.STATUS_WARNING

    @property
    def is_invalid(self):
        return self.status == self.STATUS_INVALID

    # ==========================================================
    # Diagnostics
    # ==========================================================

    def add_note(self, note):

        self.notes.append(str(note))

    def warning(self, note):

        self.status = self.STATUS_WARNING

        self.add_note(note)

    def invalidate(self, note):

        self.status = self.STATUS_INVALID

        self.skip = True

        self.skip_reason = str(note)

        self.add_note(note)

    # ==========================================================
    # Display
    # ==========================================================

    def to_string(self):

        return (
            "Station: {:.2f} ft\n"
            "XYZ: ({:.3f}, {:.3f}, {:.3f})\n"
            "Status: {}\n"
        ).format(
            self.station,
            self.x,
            self.y,
            self.z,
            self.status
        )

    def __repr__(self):

        return (
            "HangerPoint("
            "station={:.2f}, "
            "status={}, "
            "XYZ=({:.3f}, {:.3f}, {:.3f}))"
        ).format(
            self.station,
            self.status,
            self.x,
            self.y,
            self.z
        )