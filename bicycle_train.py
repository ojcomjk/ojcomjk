from google.colab import files
uploaded = files.upload()

import pandas as pd
train = pd.read_csv("train.csv")
train.head()
