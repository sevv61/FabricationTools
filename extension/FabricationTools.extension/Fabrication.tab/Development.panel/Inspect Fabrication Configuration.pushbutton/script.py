# -*- coding: utf-8 -*-

from pyrevit import revit
from pyrevit import forms
import Autodesk.Revit.DB as DB


def main():

    doc = revit.doc

    # Attempt to retrieve the fabrication configuration
    config = DB.FabricationConfiguration.GetFabricationConfiguration(doc)

    if config is None:
        forms.alert(
            "No Fabrication Configuration is loaded.",
            title="Fabrication Configuration"
        )
        return

    lines = []

    lines.append("Fabrication Configuration")
    lines.append("")

    # Keep this first version minimal and robust.
    # We'll add more properties after confirming which ones
    # are available in your Revit 2023 build.

    lines.append("Configuration object loaded successfully.")
    lines.append("")
    lines.append("Type:")
    lines.append(str(type(config)))

    forms.alert(
        "\n".join(lines),
        title="Fabrication Configuration"
    )


if __name__ == "__main__":
    main()