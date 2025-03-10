
import Levenshtein
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def jaccard_similarity(vec1, vec2):
    intersection = sum([min(a, b) for a, b in zip(vec1, vec2)])
    union = sum([max(a, b) for a, b in zip(vec1, vec2)])
    return intersection / union if union != 0 else 0

def compare(str1="", str2="", method="content", replace_list=[["NPO", "NP0"]], ignore_len=3):
    if len(replace_list) > 0:
        for replace_item in replace_list:
            str1 = str1.replace(replace_item[0], replace_item[1])
            str2 = str2.replace(replace_item[0], replace_item[1])
    similarity = 0
    match method:
        case 'Levenshtein':
            distance = Levenshtein.distance(str1, str2)
            similarity = 1 - Levenshtein.distance(str1, str2) / max(len(str1), len(str2))
        case 'Jacquard':
            vectorizer = CountVectorizer().fit_transform([str1, str2])
            vectors = vectorizer.toarray()
            similarity = jaccard_similarity(vectors[0], vectors[1])
        case 'content':
            if len(str2) < ignore_len:
                return 0
            if str1.find('-') == 1:
                str1_ = str1[1:].replace('-','')
                if (str1_ in str2) or (str2 in str1):
                    similarity = 1
            if (str1 in str2) or (str2 in str1):
                similarity = 1
    return similarity

def nmax(nums):
    maxx = max(nums)
    for i in range(0, len(nums) + 1):
        if nums[i] == maxx:
            return maxx, i

def find_all_occurrences(text, substring):
    start = 0
    indices = []
    while True:
        index = text.find(substring, start)
        if index == -1:  
            break
        indices.append(index)
        start = index + 1
    return indices

def isRLC(part_number):
    elements = ['R', 'C', 'L']
    packages = ['0603', '0402', '0201', '0805', '1206', '1210']
    if part_number[0] in elements:
        pos_ = find_all_occurrences(part_number, '-')
        if len(pos_) > 1:
            if part_number[pos_[0]+1:pos_[1]] in packages:
                return [True, part_number[pos_[0]+1:pos_[1]]]
    return [False, ""]