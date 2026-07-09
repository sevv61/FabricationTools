# -*- coding: utf-8 -*-
"""
Preview Hanger Locations

Development tool for calculating hanger locations.
"""

from pyrevit import revit
from pyrevit import forms

import fabrication.parts as parts

from config.hanger_config import HangerConfiguration
from pipeline.hanger_pipeline import HangerPipeline
from hangers.preview import HangerPreview


def main():

    # ---------------------------------------------------------
    # Get Selection
    # ---------------------------------------------------------

    selection = revit.get_selection()

    if len(selection) != 1:

        forms.alert(
            "Please select one Fabrication Part.",
            title="Preview Hangers"
        )

        return

    # ---------------------------------------------------------
    # Wrap selected fabrication part
    # ---------------------------------------------------------

    part = parts.FabricationPartInfo(selection[0])

    # ---------------------------------------------------------
    # Build configuration
    # ---------------------------------------------------------

    config = HangerConfiguration()

    #
    # Temporary development values
    #

    config.spacing = 8.0

    config.start_offset = 1.0

    config.end_offset = 1.0

    config.minimum_length = 3.0

    # ---------------------------------------------------------
    # Execute pipeline
    # ---------------------------------------------------------

    pipeline = HangerPipeline(config)

    run = pipeline.execute(part)

    # ---------------------------------------------------------
    # Preview Results
    # ---------------------------------------------------------

    preview = HangerPreview()

    report = preview.build_report(run)

    forms.alert(
        report,
        title="Hanger Preview"
    )


if __name__ == "__main__":

    main()