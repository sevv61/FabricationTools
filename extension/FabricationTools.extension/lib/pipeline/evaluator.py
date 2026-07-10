from rules.fabrication_rules import evaluate_fabrication_part


def evaluate_parts(models):

    results = []

    for model in models:

        results.append(
            evaluate_fabrication_part(model)
        )

    return results