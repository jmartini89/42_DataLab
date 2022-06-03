import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/titles.csv")

def customPlot(title:str="", x:str="", y:str="") -> None:
    plt.title("netflix&chill: " + title)
    plt.xlabel(x) 
    plt.ylabel(y)

df["genres"] = df["genres"].apply(eval)

customPlot("movies per release year", "release year", "number of movies")
movies = df.loc[df["type"].str.contains("MOVIE")]
movies['release_year'].value_counts().sort_index().plot()
plt.show()

customPlot("shows vs movies")
df["type"].value_counts().plot(kind = "pie")
plt.show()

# tmdb_popularity instead ?
customPlot("most popular genres")
genres = df["genres"].explode()
genres.value_counts().plot(kind = "bar")
plt.show()