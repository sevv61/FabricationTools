# -*- coding: utf-8 -*-

"""
Preview Hanger Locations

Calculates hanger insertion locations for the selected
Fabrication Part and displays the results.
"""

from pyrevit import revit
from pyrevit import forms

import fabrication.parts as parts

from config.hanger_config import HangerConfiguration
from spacing.spacing import HangerSpacingEngine


def main():

    selection = revit.get_selection()

    if len(selection) != 1:
        forms.alert(
            "Please select one Fabrication Part.",
            title="Preview Hangers"
        )
        return

    # Get selected fabrication part
    part = parts.FabricationPartInfo(selection[0])

    # Create configuration
    config = HangerConfiguration()

    # Create spacing engine
    engine = HangerSpacingEngine(config)

    # Calculate hanger points
    hanger_points = engine.calculate(part.geometry)

    if not hanger_points:

        forms.alert(
            "No hanger locations were calculated.",
            title="Preview Hangers"
        )

        return

    # Build report

    msg = []

    msg.append("Hanger Preview")
    msg.append("")
    msg.append("Part")
    msg.append(str(part.name))
    msg.append("")
    msg.append("Length")
    msg.append("{:.2f} ft".format(part.geometry.length))
    msg.append("")
    msg.append("Total Hangers")
    msg.append(str(len(hanger_points)))
    msg.append("")
    msg.append("---------------------------------------")
    msg.append("")

    for i, hanger in enumerate(hanger_points):

        msg.append(
            "Hanger {}".format(i + 1)
        )

        msg.append(
            "  Station : {:.2f} ft".format(
                hanger.station
            )
        )

        msg.append(
            "  X : {:.3f}".format(
                hanger.x
            )
        )

        msg.append(
            "  Y : {:.3f}".format(
                hanger.y
            )
        )

        msg.append(
            "  Z : {:.3f}".format(
                hanger.z
            )
        )

        if hanger.notes:

            msg.append("  Notes")

            for note in hanger.notes:

                msg.append(
                    "     - {}".format(note)
                )

        msg.append("")

    forms.alert(
        "\n".join(msg),
        title="Preview Hangers"
    )


if __name__ == "__main__":
    main()