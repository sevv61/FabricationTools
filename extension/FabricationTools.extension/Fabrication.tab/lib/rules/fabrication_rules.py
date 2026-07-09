# -*- coding: utf-8 -*-

from .duct_rules import evaluate_duct
from .pipe_rules import evaluate_pipe


def evaluate_fabrication_part(data):

    if data.part_type == "DUCT":
        return evaluate_duct(data)

    elif data.part_type == "PIPE":
        return evaluate_pipe(data)

    return None


def evaluate_fabrication_part(data):


    print("FABRICATION RULES LOADED")


    result = {}


    result["part_type"] = (
        data.part_type
    )


    result["requires_hanger"] = True


    result["spacing"] = 120


    result["hanger_type"] = (
        "TEST_HANGER"
    )


    return result