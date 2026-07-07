# -*- coding: utf-8 -*-

from pyrevit import revit, forms

from fabrication.collector import FabricationCollector


def main():
    doc = revit.doc

    collector = FabricationCollector(doc)

    parts = collector.get_all_parts()

    if not parts:
        forms.alert(
            "No Fabrication Parts found.",
            title="Inspect Fabrication"
        )
        return

    message = []

    message.append(
        "Fabrication Parts Found: {}\n".format(len(parts))
    )

    sample = parts[:10]

   for part in sample:

    message.append("--------------------------------")

    message.append(
        "ID: {}".format(part.Id.IntegerValue)
    )

    try:
        message.append(
            "Name: {}".format(part.Name)
        )
    except Exception:
        message.append(
            "Name: <Unavailable>"
        )

    forms.alert(
        "\n".join(message),
        title="Inspect Fabrication"
    )


if __name__ == "__main__":
    main()