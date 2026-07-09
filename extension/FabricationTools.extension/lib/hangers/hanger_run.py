# -*- coding: utf-8 -*-
"""
hanger_run.py

Represents one hanger calculation for a Fabrication Part.
"""


class HangerRun(object):

    def __init__(self):

        self.part = None

        self.geometry = None

        self.config = None

        self.hanger_points = []

        self.total_length = 0.0

        self.usable_length = 0.0

        self.spacing = 0.0

        self.notes = []

        self.warnings = []

    @property
    def hanger_count(self):

        return len(self.hanger_points)

    def add_point(self, hanger):

        self.hanger_points.append(hanger)

    def add_note(self, text):

        self.notes.append(str(text))

    def add_warning(self, text):

        self.warnings.append(str(text))