import requests
import shutil
import pandas as pd

csv_path = "./website/images_men.csv"
df = pd.read_csv(csv_path)
for ind in df.index:
    #print(df.loc[ind])
    row = df.loc[ind].dropna()
    for url in row:
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open("./website/data/" + url.replace("/", "_").replace("?", "-").replace(".", "-").replace(":", "-"), 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)