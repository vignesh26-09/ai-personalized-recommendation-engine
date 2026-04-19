import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from models.embedding import get_embeddings, get_query_embedding
from utils.feature_engineering import difficulty_match, keyword_overlap
from models.ranking_model import train_model, predict_scores

def generate_recommendations(data, query, user_level):
    
    embeddings = get_embeddings(data['description'].tolist())
    query_embedding = get_query_embedding(query)

    similarity_scores = cosine_similarity(query_embedding, embeddings)[0]

    features = []
    for i in range(len(data)):
        f1 = similarity_scores[i]
        f2 = difficulty_match(data['difficulty'][i], user_level)
        f3 = keyword_overlap(data['description'][i], query)
        features.append([f1, f2, f3])

    X = np.array(features)

    y = np.array([1 if s > 0.5 else 0 for s in similarity_scores])

    model = train_model(X, y)
    scores = predict_scores(model, X)

    return scores