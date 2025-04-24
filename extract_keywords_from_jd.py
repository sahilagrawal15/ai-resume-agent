def extract_keywords_from_jd(jd_text, top_n=50):
    from skills_list import SKILLS
    from keybert import KeyBERT

    kw_model = KeyBERT(model="all-MiniLM-L6-v2")
    jd_lower = jd_text.lower()

    # Step 1: Use KeyBERT
    raw_keywords = kw_model.extract_keywords(
        jd_text,
        keyphrase_ngram_range=(1, 3),
        stop_words='english',
        top_n=top_n
    )
    bert_phrases = {phrase.lower().strip() for phrase, _ in raw_keywords}

    # Step 2: Fallback scan (search skills directly in JD)
    direct_matches = {skill for skill in SKILLS if skill in jd_lower}

    # Combine both sources
    matched_skills = (bert_phrases | direct_matches) & SKILLS
    return list(matched_skills)
