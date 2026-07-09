# -*- coding: utf-8 -*-

from base_rules import HangerRuleResult



def evaluate_duct(data):


    result = HangerRuleResult()



    result.requires_hanger = True

    result.hanger_type = (
        "DUCT_HANGER"
    )


    #
    # Initial spacing rules
    #
    # These will later be replaced
    # with SMACNA / project standards
    #


    if data.width:

        if data.width >= 48:

            result.spacing = 96

            result.add_reason(
                "Large duct width"
            )


        else:

            result.spacing = 120

            result.add_reason(
                "Standard duct spacing"
            )


    else:

        result.spacing = 120

        result.add_reason(
            "Default duct spacing"
        )



    return result