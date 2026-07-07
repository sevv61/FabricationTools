from pyrevit import revit, forms

from lib.fabrication.parts import FabricationPartInfo


def main():

    selection = revit.get_selection()

    if len(selection) != 1:
        forms.alert(
            "Please select one Fabrication Part.",
            title="Inspect Geometry"
        )
        return

    fab = FabricationPartInfo(selection.first)

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

    forms.alert("\n".join(msg), title="Geometry")


if __name__ == "__main__":
    main()