# INF601 - Advanced Programming in Python
# Janelyn Nichols
# Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt

books = pd.read_csv("books_data.csv", index_col=0, parse_dates=True)
print(books.head())
