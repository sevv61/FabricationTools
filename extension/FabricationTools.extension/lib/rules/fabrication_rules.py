# -*- coding: utf-8 -*-


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