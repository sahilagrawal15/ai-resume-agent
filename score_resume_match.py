from difflib import SequenceMatcher
from skill_weights import SKILL_WEIGHTS
from role_multipliers import ROLE_MULTIPLIERS

def is_fuzzy_match(term, text, threshold=0.8):
    """Check if term approximately matches part of resume using ratio similarity."""
    term = term.lower()
    text = text.lower()
    words = text.split()
    for i in range(len(words)):
        window = " ".join(words[i:i+len(term.split()) + 2])
        ratio = SequenceMatcher(None, term, window).ratio()
        if ratio >= threshold:
            return True
    return False

def get_effective_weight(skill, role=None):
    """
    Combines base weight with role-based multiplier.
    """
    base = SKILL_WEIGHTS.get(skill, 1.0)
    multiplier = 1.0
    if role and role in ROLE_MULTIPLIERS:
        multiplier = ROLE_MULTIPLIERS[role].get(skill, 1.0)
    return base * multiplier

def score_resume_match(jd_keywords, resume_text, role=None):
    """
    Weighted, fuzzy-matched resume scoring based on skill importance and role context.
    """
    resume_text_lower = resume_text.lower()
    found = []
    missing = []

    total_weight = 0
    matched_weight = 0

    for keyword in jd_keywords:
        key = keyword.lower()
        weight = get_effective_weight(key, role)
        total_weight += weight

        if key in resume_text_lower or is_fuzzy_match(key, resume_text_lower):
            matched_weight += weight
            found.append(keyword)
        else:
            missing.append(keyword)

    if total_weight == 0:
        return 0, [], []

    score = round((matched_weight / total_weight) * 100)
    return score, found, missing
