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


    from rules.rule_engine import evaluate_part


    result = evaluate_part(
        data
    )


    print(
        data.to_dict()
    )


    print(
        result.to_dict()
    )