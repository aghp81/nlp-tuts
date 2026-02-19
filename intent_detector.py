from similarity import SimilarityEngine
from intents import INTENTS

class IntentDetector:
    def __init__(self):
        self.patterns = []
        self.intent_map = []

        for intent, phrases in INTENTS.items():
            for p in phrases:
                self.patterns.append(p)
                self.intent_map.append(intent)

        self.engine = SimilarityEngine(self.patterns)

    def detect(self, text: str, threshold=0.4):
        idx, score = self.engine.best_match(text)
        if score < threshold:
            return None, score

        return self.intent_map[idx], score
