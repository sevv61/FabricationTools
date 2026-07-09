# -*- coding: utf-8 -*-


class HangerRuleResult:


    def __init__(self):

        self.requires_hanger = False

        self.spacing = None

        self.hanger_type = None

        self.reason = []


    def add_reason(self, text):

        self.reason.append(text)



    def to_dict(self):

        return {

            "requires_hanger":
                self.requires_hanger,

            "spacing":
                self.spacing,

            "hanger_type":
                self.hanger_type,

            "reason":
                self.reason
        }