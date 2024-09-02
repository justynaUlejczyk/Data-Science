import pandas as pd

#adding my data sets, listin all columns

content = pd.read_csv("Content.csv")
print(content.head())
print(content.columns)

reactions=pd.read_csv("Reactions.csv")
print(reactions.columns)
print(reactions.head())

reactionTypes=pd.read_csv("ReactionTypes.csv")
print(reactionTypes.columns)
print(reactionTypes.head())

#drop all rowns with any missing values 
content_cleaned = content.dropna()
reactions_cleaned = reactions.dropna()
reactionTypes_cleaned= reactionTypes.dropna()

#remove columns useless for my analyse

content_cleaned = content_cleaned.drop("URL", axis=1)
content_cleaned = content_cleaned.drop("User ID", axis=1)
#change the name of column
content_cleaned['Category'] = content_cleaned['Category'].str.replace('"', '', regex=True)
content_cleaned= content_cleaned.rename(columns={'Type': 'Content Type'})
reactions_cleaned = reactions_cleaned.drop("User ID", axis=1)
#save as new file 
content_cleaned.to_csv('new_data/Content.csv')
reactions_cleaned.to_csv ('new_data/Reactions.csv')
reactionTypes_cleaned.to_csv('new_data/ReactionTypes.csv')
