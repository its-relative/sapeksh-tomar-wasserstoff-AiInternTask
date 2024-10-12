# # def extract_keywords(text, num_keywords=5):
# #     """
# #     Extract keywords from the given text.

# #     Args:
# #         text (str): The text to extract keywords from.
# #         num_keywords (int, optional): The number of keywords to extract. Defaults to 5.

# #     Returns:
# #         list: A list of extracted keywords.
# #     """
# #     # Dummy logic
# #     words = text.split()
# #     return words[:num_keywords]


# # def extract_keywords_tfidf(text, num_keywords=5):
# #     """
# #     Extract keywords from the given text using TF-IDF.

# #     Args:
# #         text (str): The text to extract keywords from.
# #         num_keywords (int, optional): The number of keywords to extract. Defaults to 5.

# #     Returns:
# #         list: A list of extracted keywords.
# #     """
# #     # Dummy logic
# #     from sklearn.feature_extraction.text import TfidfVectorizer
# #     vectorizer = TfidfVectorizer()
# #     tfidf = vectorizer.fit_transform([text])
# #     feature_names = vectorizer.get_feature_names_out()
# #     keywords = [feature_names[index] for index in tfidf.toarray().argsort()[0][-num_keywords:]]
# #     return keywords


# # def extract_keywords_yake(text, num_keywords=5):
# #     """
# #     Extract keywords from the given text using YAKE.

# #     Args:
# #         text (str): The text to extract keywords from.
# #         num_keywords (int, optional): The number of keywords to extract. Defaults to 5.

# #     Returns:
# #         list: A list of extracted keywords.
# #     """
# #     # Dummy logic
# #     from yake.keywordextractor import KeywordExtractor
# #     kw_extractor = KeywordExtractor()
# #     keywords = kw_extractor.extract_keywords(text)
# #     return [keyword[0] for keyword in sorted(keywords, key=lambda x: x[1], reverse=True)[:num_keywords]]



# from sklearn.feature_extraction.text import TfidfVectorizer

# def extract_keywords(text, num_keywords=5):
#     """
#     Extract top 'num_keywords' keywords from the text using basic split.
    
#     Args:
#         text (str): The text to extract keywords from.
#         num_keywords (int, optional): The number of keywords to extract. Defaults to 5.

#     Returns:
#         list: A list of extracted keywords.
#     """
#     words = text.split()
#     return words[:num_keywords]

# def extract_keywords_tfidf(text, num_keywords=5):
#     """
#     Extract keywords from the given text using TF-IDF.

#     Args:
#         text (str): The text to extract keywords from.
#         num_keywords (int, optional): The number of keywords to extract. Defaults to 5.

#     Returns:
#         list: A list of extracted keywords.
#     """
#     vectorizer = TfidfVectorizer(max_df=0.8, max_features=10000)
#     tfidf_matrix = vectorizer.fit_transform([text])
#     feature_names = vectorizer.get_feature_names_out()
#     tfidf_scores = tfidf_matrix.toarray()[0]
    
#     # Get indices of the top keywords
#     sorted_indices = tfidf_scores.argsort()[::-1][:num_keywords]
#     top_keywords = [feature_names[i] for i in sorted_indices]
    
#     return top_keywords

# def extract_keywords_yake(text, num_keywords=5):
#     """
#     Extract keywords using YAKE (Yet Another Keyword Extractor).

#     Args:
#         text (str): The text to extract keywords from.
#         num_keywords (int, optional): The number of keywords to extract. Defaults to 5.

#     Returns:
#         list: A list of extracted keywords.
#     """
#     from yake import KeywordExtractor
#     kw_extractor = KeywordExtractor()
#     keywords = kw_extractor.extract_keywords(text)
    
#     # Sort keywords by relevance score and select top 'num_keywords'
#     return [keyword[0] for keyword in sorted(keywords, key=lambda x: x[1])[:num_keywords]]


from sklearn.feature_extraction.text import TfidfVectorizer
import re

class KeywordExtractor:
    def __init__(self, max_keywords=10):
        # Initialize parameters for keyword extraction
        self.max_keywords = max_keywords
        self.vectorizer = TfidfVectorizer(stop_words='english', max_df=0.85)

    def clean_text(self, text):
        # Clean the text by removing special characters and numbers
        text = re.sub(r'\d+', '', text)  # remove numbers
        text = re.sub(r'\W+', ' ', text)  # remove special characters
        return text

    def extract_keywords(self, text):
        # Clean the input text
        cleaned_text = self.clean_text(text)
        
        # Fit and transform the text using TF-IDF
        tfidf_matrix = self.vectorizer.fit_transform([cleaned_text])
        feature_names = self.vectorizer.get_feature_names_out()
        
        # Sort TF-IDF scores for keywords
        scores = tfidf_matrix.toarray()[0]
        keyword_indices = scores.argsort()[-self.max_keywords:][::-1]
        keywords = [feature_names[index] for index in keyword_indices]
        
        return keywords

def extract_keywords_from_pdf_text(text):
    extractor = KeywordExtractor(max_keywords=10)
    return extractor.extract_keywords(text)
