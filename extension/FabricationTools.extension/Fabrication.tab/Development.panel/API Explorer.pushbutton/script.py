# -*- coding: utf-8 -*-

from pyrevit import revit, forms

from Autodesk.Revit.DB import FabricationPart
from Autodesk.Revit.UI.Selection import ObjectType

from api_explorer import explore_fabrication_part


uidoc = revit.uidoc
doc = revit.doc


ref = uidoc.Selection.PickObject(
    ObjectType.Element,
    "Select Fabrication Part"
)


element = doc.GetElement(ref)


if not isinstance(element, FabricationPart):

    forms.alert(
        "Selected element is not a FabricationPart",
        exitscript=True
    )


results = explore_fabrication_part(element)


forms.alert(
    "Fabrication API Explorer Complete\n\n"
    "Data written to explorer_results.json"
)