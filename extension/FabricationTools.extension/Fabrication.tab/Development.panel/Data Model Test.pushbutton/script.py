# -*- coding: utf-8 -*-

from pyrevit import revit

from Autodesk.Revit.UI.Selection import ObjectType
from Autodesk.Revit.DB import FabricationPart

from fabrication_extractor import extract_fabrication_part



uidoc = revit.uidoc
doc = revit.doc



ref = uidoc.Selection.PickObject(
    ObjectType.Element,
    "Select Fabrication Part"
)


part = doc.GetElement(ref)



if isinstance(part, FabricationPart):


    data = extract_fabrication_part(
        part
    )


    print(
        data.to_dict()
    )