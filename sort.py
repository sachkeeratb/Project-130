import csv
import pandas as pd

df = pd.read_csv("total_stars.csv")

del df["Luminosity"]
del df["Unnamed: 0"]

df.to_csv('main.csv')