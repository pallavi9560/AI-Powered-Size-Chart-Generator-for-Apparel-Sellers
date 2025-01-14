import numpy as np
from sklearn.cluster import KMeans
from pymongo import MongoClient
import json

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['size-chart-generator']
users_collection = db['users']

# Load user data from MongoDB
def load_user_data():
    user_data = []
    for user in users_collection.find():
        user_data.append(user['measurements'])
    return np.array(user_data)

# Train KMeans model
def train_model():
    user_data = load_user_data()
    kmeans = KMeans(n_clusters=4, random_state=42)
    kmeans.fit(user_data)
    return kmeans

# Save model
def save_model(model, model_path='kmeans_model.json'):
    model_data = {
        'cluster_centers': model.cluster_centers_.tolist(),
        'labels': model.labels_.tolist()
    }
    with open(model_path, 'w') as file:
        json.dump(model_data, file)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    model = train_model()
    save_model(model)

