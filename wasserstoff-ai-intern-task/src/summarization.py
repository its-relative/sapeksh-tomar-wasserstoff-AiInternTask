def summarize_text(text, method="textrank"):
    """
    Summarize the given text using the specified method.

    Args:
        text (str): The text to summarize.
        method (str, optional): The summarization method. Defaults to "textrank".

    Returns:
        str: The summarized text.
    """
    # Dummy logic
    if method == "textrank":
        return text[:100] + "..."
    else:
        return text[:50] + "..."

