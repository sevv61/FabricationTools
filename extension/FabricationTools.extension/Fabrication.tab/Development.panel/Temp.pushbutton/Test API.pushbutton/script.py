from pyrevit import forms
import Autodesk.Revit.DB as DB

names = sorted([n for n in dir(DB) if "Fabrication" in n])

if names:
    forms.alert("\n".join(names), title="Fabrication Classes")
else:
    forms.alert("No Fabrication classes found.", title="Fabrication Classes")