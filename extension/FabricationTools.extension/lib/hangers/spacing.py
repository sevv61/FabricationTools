# -*- coding: utf-8 -*-
"""
spacing.py

Calculates hanger insertion points for a Fabrication Part.

Target:
    Autodesk Revit 2023
"""

from hangers.hanger_point import HangerPoint
from hangers.hanger_run import HangerRun


class HangerSpacingEngine(object):
    """
    Calculates hanger insertion locations along a Fabrication Part.
    """

    def __init__(self, config):

        self.config = config

    def calculate(self, part):
        """
        Calculate hanger insertion locations.

        Parameters
        ----------
        part : FabricationPartInfo

        Returns
        -------
        HangerRun
        """

        run = HangerRun()

        # Store references
        run.part = part
        run.geometry = part.geometry
        run.config = self.config

        geometry = part.geometry

        # Validate geometry
        if geometry is None:
            run.add_warning("Part has no geometry.")
            return run

        if geometry.curve is None:
            run.add_warning("Part has no LocationCurve.")
            return run

        length = geometry.length

        run.total_length = length

        if length < self.config.minimum_length:
            run.add_warning(
                "Part shorter than minimum hanger length."
            )
            return run

        start = self.config.start_offset
        end = self.config.end_offset
        spacing = self.config.spacing

        run.spacing = spacing

        usable = length - start - end

        run.usable_length = usable

        if usable <= 0:
            run.add_warning("No usable length.")
            return run

        direction = geometry.direction

        if direction is None:
            run.add_warning("Unable to determine direction.")
            return run

        current = start

        while current <= (length - end + 0.0001):

            location = (
                geometry.start_point +
                direction.Multiply(current)
            )

            hanger = HangerPoint(
                location=location,
                station=current
            )

            # Populate metadata
            hanger.direction = direction
            hanger.host = part.element
            hanger.part_name = part.name

            run.add_point(hanger)

            current += spacing

        return run