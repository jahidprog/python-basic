from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
csv_path = Path("sample_movie_revenue.csv")
if not csv_path.exists():
    pd.DataFrame({
        "year": [2020, 2021, 2022, 2023, 2024],
        "oscar_revenue": [620, 750, 710, 820, 790],
        "non_oscar_revenue": [1100, 1450, 1380, 1600, 1520],
    }).to_csv(csv_path, index=False)
    print(f"Created sample CSV: {csv_path.resolve()}")
df = pd.read_csv(csv_path)
plt.plot(df["year"], df["oscar_revenue"], marker="o", label="Oscar movies")
plt.plot(df["year"], df["non_oscar_revenue"], marker="s", label="Non-Oscar movies")
plt.title("Revenue Loaded from CSV")
plt.xlabel("Year")
plt.ylabel("Revenue (millions USD)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
