from normalizer import normalize_text
from tokenizer import tokenize
from intent_detector import IntentDetector
from entity_extractor import extract_entities

intent_detector = IntentDetector()

def process(text: str) -> dict:
    normalized = normalize_text(text)
    tokens = tokenize(normalized)

    intent, confidence = intent_detector.detect(normalized)
    entities = extract_entities(tokens)

    return {
        "text": normalized,
        "tokens": tokens,
        "intent": intent,
        "confidence": round(float(confidence), 3),
        "entities": entities
    }
