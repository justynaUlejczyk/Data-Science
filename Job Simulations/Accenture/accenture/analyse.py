import pandas as pd

content = pd.read_csv("new_data/Content.csv")
reactions=pd.read_csv("new_data/Reactions.csv")
reactionTypes=pd.read_csv("new_data/ReactionTypes.csv")

# Merge Reactions with Content on 'ContentID'
merged_df = pd.merge(reactions, content, on='Content ID', how='left')
# Mergemerged_df with reactionTypes on 'Type'
merged2_df = pd.merge(merged_df, reactionTypes, on='Type', how='left')

print(merged2_df.head())
merged2_df.to_csv('new_data.csv')

import matplotlib.pyplot as plt
import numpy as np

# Count the number of reactions for each type
reaction_counts = merged2_df['Type'].value_counts()

# Create a bar plot
plt.figure(figsize=(10, 6))
reaction_counts.plot(kind='bar', color='skyblue')
plt.title('Distribution of Reaction Types')
plt.xlabel('Reaction Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

merged2_df['Datetime'] = pd.to_datetime(merged2_df['Datetime'])

# Group by date and count reactions
reactions_by_date = merged2_df.groupby('Datetime').size()

# Create a line plot
plt.figure(figsize=(12, 6))
reactions_by_date.plot(kind='line', marker='o', color='orange')
plt.title('Reactions Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Reactions')
plt.grid(True)
plt.show()

# Count the number of reactions for each content type
content_reactions = merged2_df['Content Type'].value_counts()

# Create a pie chart
plt.figure(figsize=(8, 8))
content_reactions.plot(kind='pie', autopct='%1.1f%%', colors=plt.cm.Paired(range(len(content_reactions))))
plt.title('Reactions by Content Type')
plt.ylabel('')
plt.show()
