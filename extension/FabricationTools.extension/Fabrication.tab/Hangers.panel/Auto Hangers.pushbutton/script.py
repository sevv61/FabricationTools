# -*- coding: utf-8 -*-
"""
Auto Hangers

Main entry point for the Fabrication Tools hanger engine.

Version: 0.1.0
Target: Autodesk Revit 2023
"""

from pyrevit import revit, forms

from fabrication.collector import FabricationCollector
from fabrication.parts import FabricationPartInfo


def main():
    """Main entry point."""

    doc = revit.doc

    collector = FabricationCollector(doc)

    parts = collector.get_all_parts()

    if not parts:
        forms.alert(
            "No Fabrication Parts were found in the active model.",
            title="Auto Hangers"
        )
        return

    valid_parts = []

    for part in parts:
        fab = FabricationPartInfo(part)

        if fab.is_valid:
            valid_parts.append(fab)

    sample = valid_parts[:10]

    message = []

    message.append("Fabrication Tools")
    message.append("")
    message.append("Auto Hanger Engine")
    message.append("")
    message.append("Total Fabrication Parts : {}".format(len(parts)))
    message.append("Valid Fabrication Parts : {}".format(len(valid_parts)))
    message.append("")
    message.append("Sample Parts")
    message.append("----------------------------------------")

    for fab in sample:

        message.append("ID       : {}".format(fab.id))
        message.append("Name     : {}".format(fab.name))
        message.append("Category : {}".format(fab.category))
        message.append("Service  : {}".format(fab.service))
        message.append("")

    forms.alert(
        "\n".join(message),
        title="Auto Hangers"
    )


if __name__ == "__main__":
    main()