# -*- coding: utf-8 -*-

from .base_rules import HangerRuleResult



def evaluate_pipe(data):

    result = HangerRuleResult()


    result.requires_hanger = True

    result.hanger_type = (
        "PIPE_HANGER"
    )


    result.spacing = 120


    result.add_reason(
        "Standard pipe spacing"
    )


    return result