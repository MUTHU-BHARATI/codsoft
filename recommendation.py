import numpy as np

# Sample movie ratings (rows: users, columns: movies)
ratings = np.array([
    [5, 4, 0, 0, 1],
    [0, 5, 4, 0, 2],
    [2, 0, 5, 4, 0],
    [0, 0, 0, 5, 4]
])

def collaborative_filtering_recommendation(user_id, ratings):
    similarity = np.dot(ratings, ratings[user_id]) / (np.linalg.norm(ratings, axis=1) * np.linalg.norm(ratings[user_id]))
    similarity[user_id] = 0

    similar_user_id = np.argmax(similarity)

    recommendations = [i for i in range(len(ratings[user_id])) if ratings[user_id][i] == 0 and ratings[similar_user_id][i] > 3]

    return recommendations

# Example usage
target_user_id = 0
recommendations = collaborative_filtering_recommendation(target_user_id, ratings)

print(f"Recommendations for user {target_user_id}: {recommendations}")
