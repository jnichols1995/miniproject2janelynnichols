# INF601 - Advanced Programming in Python
# Janelyn Nichols
# Mini Project 2

# Mini Project 2 requirements
# (5/5 points) Initial comments with your name, class and project at the top of your .py file.
# (5/5 points) Proper import of packages used.
# (20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
# Think of some question you would like to solve such as:
# "How many homes in the US have access to 100Mbps Internet or more?"
# "How many movies that Ridley Scott directed is on Netflix?" - https://www.kaggle.com/datasets/shivamb/netflix-shows
# Here are some other great datasets: https://www.kaggle.com/datasets
# (10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.
# (10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# (10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import copy
import pathlib as Path
import os
import re

#create charts folder to store .png files
try:
    os.makedirs('charts')
except FileExistsError:
    pass

#import books_data.csv
books = pd.read_csv("books_data.csv", index_col=0)
'''
books1 = re.compile('English')
Language = books["Language"].describe()

foundCount = 0
for language in Language:
    mo.books1.search(line)
    if mo.group():
        foundCount =+1
    print(mo.count("English"))
'''

selectLanguage = ["German", "Italian", "Portuguese"]
df1 = pd.read_csv("books_data.csv")
mask = df1["Language"].isin(selectLanguage)
selectRecords = df1[mask]
print(selectRecords)

ax1 = selectRecords.plot(x='Authors', y='Sales_in_millions')
plt.title("Book Sales in Millions of Dollars")
plt.show()
plt.savefig("charts/" + "BookSalesinMillions.png")

authors = selectRecords["Authors"].value_counts()
ax2 = authors.plot()
ax2.set_title("Count of Books by Author")
chart2="Count of Books by Author"
ax2.legend()
plt.show()
plt.savefig("charts/"+"CountofBookbyAuthor.png")

languages = selectRecords["Language"].value_counts()
ax3 = languages.plot.bar(x='Language', y='Book Count', color='r')
plt.title("Count of Books by Language")
plt.xlabel("Language")
plt.ylabel("Book Count")
plt.show()
plt.savefig("charts/"+"CountofBooksbyLanguage.png")

df = pd.DataFrame({'Language':['Chinese', 'Czech', 'Dutch', 'English', 'French','German', 'Gujarati', 'Italian','Japanese','Norwegian','Polish','Portuguese','Russian','Spanish','Swedish','Yiddish'],'Number of Books':[5,1,2,210, 11,6,1,5,26,4,1,1,7,3,6,1]})
ax = df.plot.bar(x='Language', y='Number of Books', rot=0, color = "g")
plt.title("Number of Books by Language")
plt.xlabel("Language")
plt.ylabel("Number of books")
plt.show()
plt.savefig("charts/" + "NumberOfBooks.png")


