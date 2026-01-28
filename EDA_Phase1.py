import pandas as pd
import numpy as np
df = pd.read_csv("/Users/ashishsharma/CSUEB/volunteer_mvp/data/clean/dataset_cleaned_merged.csv")

df.shape
df.head()
df.info()
missing = (
    df.isna()
      .sum()
      .sort_values(ascending=False)
)

missing
(missing / len(df) * 100).round(1)
df[["REVENUE_AMT", "ASSET_AMT", "INCOME_AMT"]].describe()
df[["REVENUE_AMT", "ASSET_AMT", "INCOME_AMT"]].median()
df["STATE"].value_counts().head(10)
df["NTEE_CD"].value_counts().head(10)
df["SUBSECTION"].value_counts()
df.groupby("STATE")["EIN"].count().sort_values(ascending=False).head(10)
df.groupby("STATE")["REVENUE_AMT"].sum().sort_values(ascending=False).head(10)
df.groupby("NTEE_CD")["REVENUE_AMT"].median().sort_values(ascending=False).head(10)

