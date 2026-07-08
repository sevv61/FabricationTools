from pyrevit import revit, forms

import fabrication.parts as parts


def main():

    selection = revit.get_selection()

    if len(selection) != 1:
        forms.alert(
            "Please select one Fabrication Part.",
            title="Inspect Geometry"
        )
        return

    element = list(selection)[0]

    fab = parts.FabricationPartInfo(element)

    geo = fab.geometry

    if geo.curve is None:
        forms.alert(
            "Selected element has no LocationCurve.",
            title="Inspect Geometry"
        )
        return

    msg = []

    msg.append("Geometry Information")
    msg.append("")
    msg.append("Length : {:.3f} ft".format(geo.length))
    msg.append("")
    msg.append("Start Point")
    msg.append(str(geo.start_point))
    msg.append("")
    msg.append("End Point")
    msg.append(str(geo.end_point))
    msg.append("")
    msg.append("Mid Point")
    msg.append(str(geo.midpoint))

    msg.append("")
    msg.append("Direction")
    msg.append(str(geo.direction))

    msg.append("")
    msg.append("Horizontal : {}".format(geo.is_horizontal))
    msg.append("Vertical   : {}".format(geo.is_vertical))
    msg.append("Sloped     : {}".format(geo.is_sloped))

    forms.alert("\n".join(msg), title="Geometry")


if __name__ == "__main__":
    main()