# -*- coding: utf-8 -*-

from rules.minimum_length import MinimumLengthRule
from rules.end_offset import EndOffsetRule


class RuleEngine(object):

    def __init__(self):

        self.rules = []

        self.register(MinimumLengthRule())
        self.register(EndOffsetRule())

    def register(self, rule):
        self.rules.append(rule)

    def validate(self, run):

        for rule in self.rules:

            if rule.enabled:
                run = rule.validate(run)

        return run