# -*- coding: utf-8 -*-

from rules.base_rule import ValidationRule


class EndOffsetRule(ValidationRule):

    name = "End Offset"

    def validate(self, run):

        for hanger in run.hanger_points:

            if hanger.station < run.config.start_offset:

                hanger.warning(
                    "Closer than start offset."
                )

        return run