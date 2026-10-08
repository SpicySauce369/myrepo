import pandas as pd
chart = pd.read_csv("scores.csv")
chart["score"] = pd.to_numeric(chart["score"], errors="coerce")
result = chart.groupby("category")["score"].mean().round(2)
print(result)