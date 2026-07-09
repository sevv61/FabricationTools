class HangerValidator(object):

    def __init__(self):

        from rules.rule_engine import RuleEngine

        self.engine = RuleEngine()

    def validate(self, run):

        return self.engine.validate(run)