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
# Imports from lib
# ---------------------------------------------------------

from fabrication_extractor import (
    extract_fabrication_part
)

from rules.rule_engine import (
    evaluate_part
)



# ---------------------------------------------------------
# Revit objects
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


part = doc.GetElement(ref)



# ---------------------------------------------------------
# Validate Selection
# ---------------------------------------------------------

if not isinstance(part, FabricationPart):

    forms.alert(
        "Selected element is not a FabricationPart",
        exitscript=True
    )



# ---------------------------------------------------------
# Extract Data Model
# ---------------------------------------------------------

data = extract_fabrication_part(
    part
)



# ---------------------------------------------------------
# Evaluate Rules
# ---------------------------------------------------------

result = evaluate_part(
    data
)



# ---------------------------------------------------------
# Output
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
        "No rule available for this part type"
    )