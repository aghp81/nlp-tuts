from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class SimilarityEngine:
    def __init__(self, patterns: list[str]):
        self.vectorizer = TfidfVectorizer()
        self.matrix = self.vectorizer.fit_transform(patterns)

    def best_match(self, text: str):
        vec = self.vectorizer.transform([text])
        scores = cosine_similarity(vec, self.matrix)[0]
        idx = np.argmax(scores)
        return idx, scores[idx]
