def difficulty_match(content_level, user_level):
    return 1 if content_level == user_level else 0

def keyword_overlap(text, query):
    return len(set(text.lower().split()) & set(query.lower().split()))