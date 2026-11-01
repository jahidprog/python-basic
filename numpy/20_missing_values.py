"""Find and handle missing numeric values with NumPy."""

import numpy as np


scores = np.array([82.0, np.nan, 91.0, 76.0, np.nan])
missing = np.isnan(scores)

print("Scores:", scores)
print("Missing-value mask:", missing)
print("Number missing:", np.count_nonzero(missing))
print("Mean ignoring missing values:", np.nanmean(scores))

# Replace missing scores with the mean of the available scores.
filled_scores = np.where(missing, np.nanmean(scores), scores)
print("Scores with missing values filled:", filled_scores)
