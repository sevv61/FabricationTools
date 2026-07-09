# -*- coding: utf-8 -*-

import sys
import os


from pyrevit import revit, forms

from Autodesk.Revit.UI.Selection import ObjectType
from Autodesk.Revit.DB import FabricationPart



# ---------------------------------------------------------
# Add extension lib folder to Python path
# ---------------------------------------------------------

extension_path = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                __file__
            )
        )
    )
)


lib_path = os.path.join(
    extension_path,
    "lib"
)


if lib_path not in sys.path:

    sys.path.append(lib_path)



# ---------------------------------------------------------
# Import project modules
# ---------------------------------------------------------

from fabrication_extractor import (
    extract_fabrication_part
)


from rules.fabrication_rules import (
    evaluate_fabrication_part
)



# ---------------------------------------------------------
# Revit document
# ---------------------------------------------------------

uidoc = revit.uidoc
doc = revit.doc



# ---------------------------------------------------------
# Select Fabrication Part
# ---------------------------------------------------------

ref = uidoc.Selection.PickObject(
    ObjectType.Element,
    "Select Fabrication Part"
)



part = doc.GetElement(
    ref
)



# ---------------------------------------------------------
# Validate Selection
# ---------------------------------------------------------

if not isinstance(
    part,
    FabricationPart
):

    forms.alert(
        "Selected element is not a FabricationPart",
        exitscript=True
    )



# ---------------------------------------------------------
# Create Fabrication Data Model
# ---------------------------------------------------------

data = extract_fabrication_part(
    part
)



# ---------------------------------------------------------
# Evaluate Fabrication Rules
# ---------------------------------------------------------

result = evaluate_fabrication_part(
    data
)



# ---------------------------------------------------------
# Output Results
# ---------------------------------------------------------

print("==============================")
print("FABRICATION DATA")
print("==============================")


print(
    data.to_dict()
)



print("")
print("==============================")
print("HANGER RULE RESULT")
print("==============================")


if result:

    print(
        result.to_dict()
    )


else:

    print(
        "No Fabrication rule available"
    )