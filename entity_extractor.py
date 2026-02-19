def extract_entities(tokens: list[str]) -> dict:
    entities = {}

    for token in tokens:
        if token.isdigit():
            entities.setdefault("number", []).append(token)

        if token in ["تهران", "اصفهان", "مشهد"]:
            entities["city"] = token

    return entities
