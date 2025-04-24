from difflib import SequenceMatcher
from skill_weights import SKILL_WEIGHTS

# Define low-importance skills that should not heavily penalize the score
LOW_IMPORTANCE_SKILLS = set([
    "innovator", "innovation", "innovative solutions", "engineering opportunities", "skills experience",
    "development experience", "interview onboarding", "sprints", "scrum", "standups", "apply", "support",
    "onboarding", "hiring process", "team collaboration", "collaborate", "inclusive culture",
    "world changer", "fun doing", "evangelize", "delight", "soft skills", "passion", "motivated",
    "curious", "self starter", "fast paced", "impactful", "ownership", "responsibilities", "qualifications",
    "equal opportunity", "employer", "recruiting", "application process", "job application", "culture",
    "background", "experience required", "preferred qualifications", "communication", "results driven",
    "creative", "detailed oriented", "team player", "willingness", "positive attitude", "growth mindset"
])

def is_fuzzy_match(term, text, threshold=0.8):
    term = term.lower()
    text = text.lower()
    words = text.split()
    for i in range(len(words)):
        window = " ".join(words[i:i+len(term.split()) + 2])
        ratio = SequenceMatcher(None, term, window).ratio()
        if ratio >= threshold:
            return True
    return False

def score_resume_match(jd_keywords, resume_text, role=None):
    resume_text_lower = resume_text.lower()
    found = []
    missing = []

    total_weight = 0
    matched_weight = 0

    for keyword in jd_keywords:
        key = keyword.lower()

        # Down-weight low-importance skills
        if key in LOW_IMPORTANCE_SKILLS:
            weight = 0.1
        else:
            weight = SKILL_WEIGHTS.get(key, 1.0)

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
