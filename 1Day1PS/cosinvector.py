from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 형태소 분석기 인스턴스 생성
okt = Okt()

# 문장들
sentence = "유저아이디를 확인하는 메소드 명"

# 형태소 분석을 수행하여 문장들을 형태소의 리스트로 변환
# morphs = [' '.join(okt.morphs(sentence)) for sentence in sentences]
morphs = okt.morphs(sentence)
# TF-IDF 벡터를 계산
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(morphs)

# TF-IDF 벡터를 추출
tfidf_vector_1 = tfidf_matrix[0].toarray()
# tfidf_vector_2 = tfidf_matrix[1].toarray()

# 벡터 출력
print("첫 번째 문장의 TF-IDF 벡터: ", tfidf_vector_1)
# print("두 번째 문장의 TF-IDF 벡터: ", tfidf_vector_2)

# 첫 번째 문장과 두 번째 문장의 코사인 유사도를 계산
# cosine_sim = cosine_similarity(tfidf_vector_1, tfidf_vector_2)

# print(cosine_sim[0][0])
