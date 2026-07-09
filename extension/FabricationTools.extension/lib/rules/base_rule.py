# -*- coding: utf-8 -*-
"""
Base class for all validation rules.
"""


class ValidationRule(object):

    name = "Unnamed Rule"

    enabled = True

    def validate(self, run):
        """
        Validate a HangerRun.

        Returns the modified run.
        """
        return run