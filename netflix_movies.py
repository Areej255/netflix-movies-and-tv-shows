# import libs
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# specify datatypes for each column
dtype = {
    "show_id":"object",
    "type":"category",
    "title":"object",
    "director":"object",
    "cast":"object",
    "country":"category",
    "release_year":"int16",
    "rating":"category",
    "duration":"object",
    "listed_in":"object"
}
# load the dataset with dtype specifications
netflix_data = pd.read_csv('C:\\Users\\PMLS\\Downloads\\netflix_titles.csv.zip', dtype=dtype)
# print(netflix_data.head(20))

# doing this piece of code bcoz dataset is too large to handle it
# load the dataset into the chunks(e.g 1000 rows at a time )
chunk_size = 1000
netflix_data_chunks = pd.read_csv('C:\\Users\\PMLS\\Downloads\\netflix_titles.csv.zip', dtype=dtype,chunksize=chunk_size)
# initialize the empty dataframe to store results
netflix_data = pd.DataFrame()
# process each chunk
for chunk in netflix_data_chunks:
    # you can do processing on each chunk here
    netflix_data=pd.concat([netflix_data,chunk])

# Convert object columns to categories
netflix_data['type'] = netflix_data['type'].astype('category')
netflix_data['country'] = netflix_data['country'].astype('category')
netflix_data['rating'] = netflix_data['rating'].astype('category')

# Downcast numerical columns
netflix_data['release_year'] = pd.to_numeric(netflix_data['release_year'], downcast='integer')

# Randomly sample 10% of the dataset for EDA
netflix_sample = netflix_data.sample(frac=0.1, random_state=42)

import gc
# Trigger garbage collection manually after major operations
gc.collect()

# Drop unnecessary columns
netflix_data.drop(columns=['director', 'cast',"duration"], inplace=True)


# print(netflix_data.info())
# print(netflix_data.columns)

# # Check for missing values in all columns
# print(netflix_data.isnull().sum())
# netflix_data["country"] = netflix_data["country"].cat.add_categories('Unknown')
# # Fill missing values in the 'country' column
# netflix_data["country"] = netflix_data['country'].fillna('Unknown')

# eda
# Plot the distribution of Movies vs. TV Shows
# sns.countplot(data=netflix_data,x='type')
# plt.title('Movies vs TV Shows on Netflix')
# plt.show()

# Analyze and visualize the trend of content added to Netflix over the years
# netflix_data['release_year'] = pd.DatetimeIndex(netflix_data['date_added']).year
# sns.countplot(data=netflix_data, x='release_year',order=netflix_data["release_year"].value_counts().index)
# plt.title("Content Added Per Year")
# plt.xticks(rotation=90)
# plt.show()

# genre distribution
# Visualize the most common genres in the dataset:
# plt.figure(figsize=(10,6))
# sns.countplot(y='listed_in',data=netflix_data,order=netflix_data['listed_in'].value_counts().iloc[:10].index)
# plt.title("Top Ten Genres on Netflix")
# plt.tight_layout()
# plt.show()

# Country-Wise Content Production
# Visualize the countries with the most content production:
# country_data = netflix_data["country"].value_counts().head(10)
# sns.barplot(x=country_data,y=country_data.index)
# plt.title("'Top 10 Countries Producing Content'")
# plt.show()

# Genre Heatmap
# Create a heatmap to show relationships between content types and genres:
# genre_data = pd.crosstab(netflix_data['type'], netflix_data['listed_in'])
# plt.figure(figsize=(12,8))
# sns.heatmap(genre_data, cmap='coolwarm', linewidths=1, linecolor='white')
# plt.title('Genre vs Type Heatmap')
# # plt.tight_layout()
# plt.show()

from wordcloud import WordCloud
wordcloud = WordCloud(width=800, height=400).generate(' '.join(netflix_data['title']))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Netflix Titles')
plt.show()
