from sentence_transformers import SentenceTransformer
from config import MODEL_NAME

model = SentenceTransformer(MODEL_NAME)

def get_embeddings(text_list):
    return model.encode(text_list)

def get_query_embedding(query):
    return model.encode([query])