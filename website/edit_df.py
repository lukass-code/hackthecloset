import pandas as pd

df = pd.read_csv("./website/holy_grail.csv")
df = df.drop(columns=["set_id","year","season","product_type","category"])

df.to_csv('./website/holy_grail_pro.csv', index=False)