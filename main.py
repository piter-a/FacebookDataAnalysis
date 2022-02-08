# analysing post frequency of my facebook data
import inline as inline
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# create a dataframe based on the json file containing my facebook post data
df = pd.read_json('your_posts_1.json')

# drop all columns except timestamp as we're only interested in frequency of posts
df = df.drop(['attachments', 'title'], axis=1)

# rename timestamp to date and change datatype to datetime
df.rename(columns={'timestamp': 'date'}, inplace=True)
pd.to_datetime(df['date'])

# count the number of posts in each month
df = df.set_index(df['date'])
post_count = df['date'].resample('MS').size()
print(post_count)

# visualize the post frequency data via a barplot using matplotlib and seaborn

# set x and y labels
x = post_count.index
y = post_count

# create bar plot
sns.barplot(x, y, color="red")

# only show x-axis labels for Jan 1 of every other year
tick_positions = np.arange(10, len(x), step=24)

# reformat date to display year only
plt.ylabel('number of posts')
plt.xticks(tick_positions, x[tick_positions].strftime("%Y"))

# display the plot
plt.show()