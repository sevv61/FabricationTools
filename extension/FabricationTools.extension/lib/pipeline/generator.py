from hangers.hanger_point import create_hanger_points


def generate_points(models, rules):

    points = []

    for model, rule in zip(models, rules):

        if rule is None:
            continue

        points.extend(
            create_hanger_points(
                model,
                rule
            )
        )

    return points