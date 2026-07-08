# -*- coding: utf-8 -*-

class HangerConfiguration(object):
    """
    Configuration for automatic hanger placement.
    """

    def __init__(self):

        # Internal Revit units (feet)

        self.spacing = 8.0

        self.start_offset = 1.0

        self.end_offset = 1.0

        self.minimum_length = 3.0

        self.place_end_hangers = True

        self.use_database_rules = False

        self.attach_to_structure = True

        self.avoid_fittings = True

        self.skip_short_parts = True