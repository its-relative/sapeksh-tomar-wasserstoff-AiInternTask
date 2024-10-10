def extract_keywords(text, num_keywords=5):
    """
    Extract keywords from the given text.

    Args:
        text (str): The text to extract keywords from.
        num_keywords (int, optional): The number of keywords to extract. Defaults to 5.

    Returns:
        list: A list of extracted keywords.
    """
    # Dummy logic
    words = text.split()
    return words[:num_keywords]


def extract_keywords_tfidf(text, num_keywords=5):
    """
    Extract keywords from the given text using TF-IDF.

    Args:
        text (str): The text to extract keywords from.
        num_keywords (int, optional): The number of keywords to extract. Defaults to 5.

    Returns:
        list: A list of extracted keywords.
    """
    # Dummy logic
    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([text])
    feature_names = vectorizer.get_feature_names_out()
    keywords = [feature_names[index] for index in tfidf.toarray().argsort()[0][-num_keywords:]]
    return keywords


def extract_keywords_yake(text, num_keywords=5):
    """
    Extract keywords from the given text using YAKE.

    Args:
        text (str): The text to extract keywords from.
        num_keywords (int, optional): The number of keywords to extract. Defaults to 5.

    Returns:
        list: A list of extracted keywords.
    """
    # Dummy logic
    from yake.keywordextractor import KeywordExtractor
    kw_extractor = KeywordExtractor()
    keywords = kw_extractor.extract_keywords(text)
    return [keyword[0] for keyword in sorted(keywords, key=lambda x: x[1], reverse=True)[:num_keywords]]