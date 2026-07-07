# -*- coding: utf-8 -*-
"""
Fabrication package.

Provides access to Fabrication-related helper classes.
Target: Autodesk Revit 2023
"""

from .collector import FabricationCollector
from .parts import FabricationPartInfo

__all__ = [
    "FabricationCollector",
    "FabricationPartInfo",
]