from hazm import Normalizer

_normalizer = Normalizer(
    persian_numbers=True,
    remove_diacritics=True,
    # affix_spacing=True
    # token_based=True
)

def normalize_text(text: str) -> str:
    text = text.strip()
    text = _normalizer.normalize(text)
    return text
