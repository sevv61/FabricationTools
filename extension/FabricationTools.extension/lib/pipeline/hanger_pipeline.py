# -*- coding: utf-8 -*-

from collector import collect_parts
from extractor import extract_parts
from evaluator import evaluate_parts
from generator import generate_points
from validator import validate_points


class HangerPipeline(object):

    def __init__(self, doc):

        self.doc = doc


    def execute(self):

        parts = collect_parts(self.doc)

        models = extract_parts(parts)

        rules = evaluate_parts(models)

        points = generate_points(models, rules)

        valid_points = validate_points(points)

        return valid_points