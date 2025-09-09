import joblib
import xgboost as xgb

old_model = joblib.load("xg_boost_recomondation.pkl")
print("Model loaded with old XGBoost version")

old_model.save_model("xg_boost_recomondation.json")
