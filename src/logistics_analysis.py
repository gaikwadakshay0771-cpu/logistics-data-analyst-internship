"""Week 1 baseline logistics analysis."""

from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "DataCoSupplyChainDataset.csv"


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found at {path}. Download the DataCo dataset and place it in data/."
        )
    return pd.read_csv(path)


def profile(df: pd.DataFrame) -> None:
    print("Shape:", df.shape)
    print("Duplicate rows:", df.duplicated().sum())
    print("\nTop missing-value counts:")
    print(df.isna().sum().sort_values(ascending=False).head(15))


def delivery_kpis(df: pd.DataFrame) -> None:
    if "Late_delivery_risk" in df.columns:
        rate = (df["Late_delivery_risk"] == 1).mean() * 100
        print(f"Late delivery rate: {rate:.2f}%")
    else:
        print("Late_delivery_risk column not found; verify the dataset.")

    if "Days for shipping (real)" in df.columns:
        print(f"Average shipping duration: {df['Days for shipping (real)'].mean():.2f} days")
    else:
        print("Days for shipping (real) column not found; verify the dataset.")


def classification_example(df: pd.DataFrame) -> None:
    from sklearn.compose import ColumnTransformer
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.impute import SimpleImputer
    from sklearn.metrics import classification_report, roc_auc_score
    from sklearn.model_selection import train_test_split
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import OneHotEncoder

    features = [
        "Shipping Mode", "Market", "Order Region",
        "Category Name", "Order Item Quantity"
    ]
    target = "Late_delivery_risk"

    missing = [c for c in features + [target] if c not in df.columns]
    if missing:
        print("Skipping classification; missing columns:", missing)
        return

    X, y = df[features], df[target]
    preprocess = ColumnTransformer([(
        "cat",
        Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore"))
        ]),
        features
    )])

    model = Pipeline([
        ("prep", preprocess),
        ("rf", RandomForestClassifier(
            n_estimators=200, random_state=42, class_weight="balanced"
        ))
    ])

    Xtr, Xte, ytr, yte = train_test_split(
        X, y, test_size=0.20, stratify=y, random_state=42
    )
    model.fit(Xtr, ytr)
    pred = model.predict(Xte)
    prob = model.predict_proba(Xte)[:, 1]

    print(classification_report(yte, pred))
    print("ROC-AUC:", round(roc_auc_score(yte, prob), 4))


def clustering_example(df: pd.DataFrame) -> None:
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import StandardScaler

    cols = ["Order Item Quantity", "Sales per customer", "Benefit per order"]
    missing = [c for c in cols if c not in df.columns]
    if missing:
        print("Skipping clustering; missing columns:", missing)
        return

    segment = df[cols].dropna().copy()
    if len(segment) < 20:
        print("Not enough complete rows for clustering.")
        return

    scaled = StandardScaler().fit_transform(segment)
    segment["cluster"] = KMeans(n_clusters=4, random_state=42, n_init=10).fit_predict(scaled)
    print(segment.groupby("cluster")[cols].mean().round(2))


def main() -> None:
    df = load_data()
    profile(df)
    delivery_kpis(df)
    classification_example(df)
    clustering_example(df)


if __name__ == "__main__":
    main()
