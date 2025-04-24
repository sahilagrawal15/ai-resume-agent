from skill_weights import SKILL_WEIGHTS

def generate_suggestions(missing_keywords, top_n=5):
    """
    Generate clean, template-based resume improvement suggestions.
    """
    sorted_missing = sorted(
        missing_keywords,
        key=lambda k: SKILL_WEIGHTS.get(k.lower(), 1.0),
        reverse=True
    )

    suggestions = []

    templates = [
        "Your resume currently lacks mention of '{}'. Consider showing where you've used it in a project or achievement.",
        "Highlight how you applied '{}' in a technical context with measurable impact.",
        "If you've worked with '{}', add a bullet that shows your contribution and outcomes.",
        "Employers often value '{}'. Include it if it's part of your actual experience.",
        "Add a project or responsibility where '{}' played a key role."
    ]

    for i, keyword in enumerate(sorted_missing[:top_n]):
        template = templates[i % len(templates)]
        suggestions.append(template.format(keyword))

    return suggestions
