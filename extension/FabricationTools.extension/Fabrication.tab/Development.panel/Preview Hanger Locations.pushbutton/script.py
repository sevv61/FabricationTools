from pyrevit import revit
from pyrevit import forms

import fabrication.parts as parts

from spacing.spacing import HangerSpacingEngine


selection = revit.get_selection()

if len(selection) != 1:
    forms.alert("Select one Fabrication Part.")
    raise SystemExit

part = parts.FabricationPartInfo(selection[0])

engine = HangerSpacingEngine(
    start_offset=1.0,
    end_offset=1.0,
    spacing=8.0
)

points = engine.calculate(part.geometry)

msg = []

msg.append("Hanger Locations")
msg.append("")

for i, p in enumerate(points):

    msg.append(
        "{} : ({:.3f}, {:.3f}, {:.3f})".format(
            i + 1,
            p.X,
            p.Y,
            p.Z
        )
    )

forms.alert("\n".join(msg))