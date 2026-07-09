# -*- coding: utf-8 -*-
"""
hanger_pipeline.py

Coordinates the hanger calculation workflow.

Target:
    Autodesk Revit 2023
"""

from spacing.spacing import HangerSpacingEngine
from hangers.validator import HangerValidator


class HangerPipeline(object):
    """
    Coordinates hanger calculation and validation.
    """

    def __init__(self, config):

        self.config = config

        self.spacing_engine = HangerSpacingEngine(config)

        self.validator = HangerValidator()

    def execute(self, part):
        """
        Execute the complete hanger pipeline.

        Parameters
        ----------
        part : FabricationPartInfo

        Returns
        -------
        HangerRun
        """

        # ---------------------------------------
        # Calculate hanger locations
        # ---------------------------------------

        run = self.spacing_engine.calculate(part)

        # ---------------------------------------
        # Validate using Rule Engine
        # ---------------------------------------

        run = self.validator.validate(run)

        # ---------------------------------------
        # Return validated run
        # ---------------------------------------

        return run