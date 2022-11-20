import pandas as pd
import requests
import os

save_path = './images'

df = pd.read_csv('./image-similarity-bc0atzhw1x-valentino_images.csv', sep=',', na_values="*")
df2 = df.fillna('')

for i in range(len(df)):

    filename = df.iloc[i, 0].split('/')[-1]
    full_path = os.path.join(save_path, filename)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/50.0.2661.102 Safari/537.36'}

    img_data = requests.get(df.iloc[i, 0], headers=headers).content

    with open(full_path, 'wb') as handler:
        handler.write(img_data)
