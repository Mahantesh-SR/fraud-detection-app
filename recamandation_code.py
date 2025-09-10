import joblib
import numpy as np

# Load the 10-feature model
knn_from_joblib = joblib.load('xg_boost_recomondation.pkl')

def recondation_fn(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
    # Convert inputs to floats
    features_list = [float(p1), float(p2), float(p3), float(p4),
                     float(p5), float(p6), float(p7), float(p8),
                     float(p9), float(p10)]

    # Reshape for prediction
    int_features = np.array(features_list).reshape(1, -1)

    # Get prediction (0 = Not Fraud, 1 = Fraud)
    prediction = knn_from_joblib.predict(int_features)
    # Get probabilities [Not Fraud %, Fraud %]
    prob = knn_from_joblib.predict_proba(int_features)[0]

    return int(prediction[0]), prob
