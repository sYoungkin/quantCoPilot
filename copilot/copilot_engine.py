from models.xgboost import run_xgboost
from models.feature_engineering import generate_features

def run_models(df):

    print("[🔧 Starting CoPilot Engine]")

    # === Feature Engineering ===
    print("[🔧 Generating Features]")
    df = generate_features(df)

#------ df copies

    # === Run XGBoost ===
    print("[🔧 Running XGBoost]")
    print("[🔍 Columns in DataFrame]:", df.columns.tolist())
    df = run_xgboost(df)

    # === Run Regression ===


    # === Run KNN ===


    # === Run Random Forest ===


    # === Run SVM ===

    return df