import requests
import shutil
import pandas as pd

csv_path = "./website/processed_dataset.csv"
df = pd.read_csv(csv_path)
for ind in df.index:
    #print(df.loc[ind])
    row = df.loc[ind].dropna()
    for i in range(1, 4):
        url = row["IMAGE_VERSION_"+ str(i)]
        if len(url) > 1:
            print(url)
            r = requests.get(url, stream=True)
            if r.status_code == 200:
                with open("./website/data2/" + url.replace("/", "_").replace("?", "-").replace(".", "-").replace(":", "-"), 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)
            else:
                print("FAAAIL")