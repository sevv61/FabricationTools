# -*- coding: utf-8 -*-

from pyrevit import revit, forms, script
from Autodesk.Revit.DB.Fabrication import FabricationPart

doc = revit.doc
uidoc = revit.uidoc

selection = uidoc.Selection.GetElementIds()

if len(selection) != 1:
    forms.alert("Select exactly ONE Fabrication Part.")
    script.exit()

element = doc.GetElement(list(selection)[0])

if not isinstance(element, FabricationPart):
    forms.alert("Selected element is not a Fabrication Part.")
    script.exit()

message = ""

message += "ID: {}\n".format(element.Id.IntegerValue)
message += "Name: {}\n".format(element.Name)
message += "Category: {}\n".format(element.Category.Name)

forms.alert(message)