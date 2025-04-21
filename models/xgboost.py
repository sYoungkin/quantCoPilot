# models/xgboost_model.py
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from feature_engineering import generate_features
from sklearn.model_selection import GridSearchCV, train_test_split

def run_xgboost(df):
    df = generate_features(df)
    df['target'] = (df['close'].shift(-3) > df['close']).astype(int)
    df = df.dropna()

    features = ['return_1', 'return_3', 'macd', 'rsi', 'boll_upper', 'boll_lower']
    X = df[features]
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False)

    # === Define Parameter Grid ===
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [3, 5, 7],
        'learning_rate': [0.01, 0.1, 0.2],
        'subsample': [0.7, 1.0],
        'colsample_bytree': [0.7, 1.0],
        'gamma': [0, 1, 5]
    }

    # === Run Grid Search ===
    model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    grid = GridSearchCV(model, param_grid, cv=3, scoring='f1', verbose=1)
    grid.fit(X_train, y_train)

    # === Print Results ===
    print("\n[Best Parameters]")
    print(grid.best_params_)

    preds = model.predict(X_test)
    print("\n[🔍 XGBoost Results]")
    print(classification_report(y_test, preds))

    print("\n[Evaluation on Test Set]")
    y_pred = grid.best_estimator_.predict(X_test)
    print(classification_report(y_test, y_pred))

    # Optional: save best model
    grid.best_estimator_.save_model("models/xgboost_best.json")

    return df