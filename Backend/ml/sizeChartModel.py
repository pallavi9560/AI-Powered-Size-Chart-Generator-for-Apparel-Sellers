import sys
import json
import numpy as np
from sklearn.cluster import KMeans
import pymongo

def load_user_data():
    user_data = json.loads(sys.argv[1])
    return user_data

def cluster_data(user_data):
    features = np.array([user['measurements'] for user in user_data])
    kmeans = KMeans(n_clusters=4).fit(features)
    return kmeans

def generate_size_chart(user_data, model):
    clusters = model.predict([user['measurements'] for user in user_data])
    size_chart = {"S": {}, "M": {}, "L": {}, "XL": {}}
    for i, user in enumerate(user_data):
        size = determine_size(clusters[i])
        size_chart[size].append(user['measurements'])
    return size_chart

def determine_size(cluster_label):
    size_mapping = {0: "S", 1: "M", 2: "L", 3: "XL"}
    return size_mapping[cluster_label]

def main():
    user_data = load_user_data()
    model = cluster_data(user_data)
    size_chart = generate_size_chart(user_data, model)
    
    # Include confidence scores
    for size in size_chart:
        size_chart[size] = {
            'measurements': np.mean(size_chart[size], axis=0).tolist(),
            'confidenceScores': np.std(size_chart[size], axis=0).tolist()
        }

    print(json.dumps(size_chart))

if __name__ == "__main__":
    main()

