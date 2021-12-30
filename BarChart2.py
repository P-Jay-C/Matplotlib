import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt


data = pd.read_csv("data.csv")
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(sep=';'))

languages = []
popularity =  []

for item in language_counter.most_common(n=15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages,popularity)

plt.title("Most popular languages")
plt.xlabel("Number of users")



print(languages)
print(popularity)


