# -*- coding: utf-8 -*-

from rules.base_rule import ValidationRule


class MinimumLengthRule(ValidationRule):

    name = "Minimum Length"

    def validate(self, run):

        if run.total_length < run.config.minimum_length:

            run.add_warning(
                "Part shorter than minimum length."
            )

            for hanger in run.hanger_points:

                hanger.invalidate(
                    "Host part too short."
                )

        return run