from fabrication.fabrication_extractor import extract_fabrication_part


def extract_parts(parts):

    models = []

    for part in parts:

        models.append(
            extract_fabrication_part(part)
        )

    return models