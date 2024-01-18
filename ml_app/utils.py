import fitz
from user.models import Department
from .constants import UnnecessaryKeywords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
from collections import Counter

def ParseResume(resume):
    doc = fitz.open(resume)
    text = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    doc.close()
    return text

def GetKeywords(resume):
    parsed_keywords = ParseResume(resume)
    unnecessary_keywords = UnnecessaryKeywords
    keywords = re.findall(r'\b\w+\b', parsed_keywords.lower())
    filtered_keywords = {keyword for keyword in keywords if keyword not in unnecessary_keywords}
    keyword_frequency = Counter(filtered_keywords)
    return keyword_frequency

def normalize_weights(weights):
    total_weight = sum(weights.values())

    normalized_weights = {category: weight / total_weight * 100 for category, weight in weights.items()}

    return normalized_weights


def calculate_weighted_average(scores, weights):
    weighted_sum = sum(score * weight for score, weight in zip(scores, weights))
    total_weight = sum(weights)
    return (weighted_sum / total_weight)*10 if total_weight != 0 else 0


def DepartmentWiseAlignment(resume):
    filtered_keywords = GetKeywords(resume)
    department_weightage = {}
    departments = Department.objects.all()

    for department_object in departments:
        all_skillset_keywords = []
        department = department_object.name
        keywords = department_object.requirements
        all_skillset_keywords.append(' '.join(keywords))
        filtered_keywords_str = ' '.join(filtered_keywords)
        department_weights = [1] * len(all_skillset_keywords)
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([filtered_keywords_str] + all_skillset_keywords)
        similarity_scores = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1:])
        weighted_averages = [calculate_weighted_average(scores, department_weights) for scores in similarity_scores]
        department_weightage[department] = round(weighted_averages[0] * 100, 2)

    return department_weightage
