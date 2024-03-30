import numpy as np
from store.vector import VectorStore

vector_store = VectorStore()

sentences = [
    "I eat an apple",
    "apple is my favorite fruit",
    "both apple and orange are fruit",
    "fruit is good for health",
]


vocab = set([word for sentence in sentences for word in sentence.lower().split()])

word_to_index = {word: i for i, word in enumerate(vocab)}

# create embeddings
sentence_vectors = {}
for sentence in sentences:
    tokens = sentence.lower().split()
    vector = np.zeros(len(vocab))
    for token in tokens:
        vector[word_to_index[token]] += 1
    sentence_vectors[sentence] = vector
    
print(sentence_vectors)

for sentence, vector in sentence_vectors.items():
    vector_store.add_vector(sentence, vector)
    
query_sentence = "apple is best for health"
query_vector = np.zeros(len(vocab))
for token in query_sentence.lower().split():
    if token in word_to_index:
        query_vector[word_to_index[token]] += 1
        
print(query_vector)       
similar_sentences = vector_store.get_similarities(query_vector, 3)


print("Query:", query_sentence)
print("Similar sentences:")
for sentence, similarity in similar_sentences:
    print(f"\t{sentence}: Similarity: {similarity:.4f}")