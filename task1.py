import numpy as np
import pandas as pd
from scipy import stats

scores_data = [72, 65, 88, np.nan, 54, 91, 76, np.nan, 83, 69]

scores = pd.Series(scores_data, name="Exam_Scores")

print("=== Descriptive Statistics (.describe()) ===")
print(scores.describe())

clean_scores = scores.dropna()
skewness = stats.skew(clean_scores)
kurtosis = stats.kurtosis(clean_scores)

print(f"\nSkewness: {skewness:.4f}")
print(f"Kurtosis: {kurtosis:.4f}")

missing_count = scores.isnull().sum()
print(f"\nMissing values: {missing_count}")

mean_val = scores.mean()
filled_scores = scores.fillna(mean_val)

print("\nFilled scores:")
print(filled_scores)