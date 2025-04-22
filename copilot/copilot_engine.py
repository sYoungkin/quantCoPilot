from models.feature_engineering import generate_features
from models.xgboost import train_xgboost

def run_models(df):

    print("[🔧 Starting CoPilot Engine]")

    # === Feature Engineering ===
    print("[🔧 Generating Features]")
    df = generate_features(df)

    # === Run XGBoost ===
    print("[🔧 Running XGBoost]")
   

    #df = train_xgboost(df)

    # === Run Regression ===


    # === Run KNN ===


    # === Run Random Forest ===


    # === Run SVM ===

    return df



def train_models(df):

    print("[🔧 Starting CoPilot Engine: Training Model]")

    # === Feature Engineering ===
    print("[🔧 Generating Features]")
    df = generate_features(df)

    # === Run XGBoost ===
    print("[🔧 Training XGBoost]")
    #df = apply_xgboost_model(df)

    df = train_xgboost(df)

    # === Run Regression ===


    # === Run KNN ===


    # === Run Random Forest ===


    # === Run SVM ===

    return df