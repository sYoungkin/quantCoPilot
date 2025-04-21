# models/xgboost_model.py
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt


def train_xgboost(df):
    df['target'] = (df['close'].shift(-3) > df['close']).astype(int)

    # 🔧 Drop rows where the target is NaN (typically at the end)
    df = df.dropna(subset=['target'])

    features = ['return_1', 'return_3', 'macd', 'rsi', 'boll_upper', 'boll_lower']
    X = df[features]
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False)

    # === Run Grid Search ===
    model = XGBClassifier(eval_metric='logloss')
    param_grid = {
        'n_estimators': [50, 100, 200],         
        'max_depth': [3, 5, 7],                 
        'learning_rate': [0.01, 0.1, 0.2],      
        'subsample': [0.7, 1.0],                
        'colsample_bytree': [0.7, 1.0],         
        'gamma': [0, 1, 5]                      
    }
    grid = GridSearchCV(model, param_grid, cv=3, scoring='f1', verbose=1, n_jobs=2)
    grid.fit(X_train, y_train)

    # === Evaluation ===
    print("\n[Best Parameters]")
    print(grid.best_params_)

    y_pred = grid.best_estimator_.predict(X_test)
    print("\n[🔍 XGBoost Results]")
    print(classification_report(y_test, y_pred))


    # Save model
    grid.best_estimator_.save_model("models/xgboost_best.json")

     # === Feature Importances ===
    best_model = grid.best_estimator_
    importances = best_model.feature_importances_

    # Print importances
    print("\n[📊 Feature Importances]")
    for feat, score in zip(X.columns, importances):
        print(f"{feat:<15}: {score:.4f}")

    # Optional: Plot them
    # plt.figure(figsize=(8, 5))
    # plt.bar(X.columns, importances)
    # plt.title("XGBoost Feature Importances")
    # plt.xticks(rotation=45)
    # plt.tight_layout()
    # plt.show()

    return df

