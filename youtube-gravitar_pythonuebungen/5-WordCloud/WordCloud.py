import os  # MS-Struktur laden
# Wechsle ins Unterverzeichniss
os.chdir("youtube-gravitar_pythonuebungen\\5-WordCloud")

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

with open("Teil_05_Alice_in_wonderland.txt") as f:
    text = f.read()

wordcloud = WordCloud(width=1920, height=1200)

STOPWORDS.add('said')
STOPWORDS.add('illustration')

wordcloud.generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.show()