import pandas as pd

# Load the data
df = pd.read_csv("new_data.csv")

# Print columns to check the actual column names
print(df.columns)

if 'Category' in df.columns and 'Score' in df.columns:
    # Group by 'Category' and sum the 'Score'
    total_scores = df.groupby('Category')['Score'].sum().reset_index()
    
    # Rename the columns for clarity (optional)
    total_scores.columns = ['Content category', 'Total Scores']
    
    # Sort by 'Total Scores' in descending order
    total_scores = total_scores.sort_values(by='Total Scores', ascending=False)
    
    # Display the result
    print(total_scores)
    total_scores.to_csv('top_categories.csv')
else:
    print("Required columns are missing in the DataFrame.")

    # Get the top 5 categories by total scores
top5_scores = total_scores.head(5)

import matplotlib.pyplot as plt

# Create a bar plot for the top 5 categories
plt.figure(figsize=(10, 6))
plt.bar(top5_scores['Content category'], top5_scores['Total Scores'], color='skyblue')
plt.xlabel('Content Category')
plt.ylabel('Total Scores')
plt.title('Top 5 Categories by Total Scores')
plt.xticks(rotation=45, ha='right')  # Rotate category labels for better readability
plt.tight_layout()  # Adjust layout to fit labels
plt.show()


total_score_all = total_scores['Total Scores'].sum()
# Calculate the total score of the top 5 categories
total_score_top5 = top5_scores['Total Scores'].sum()
# Calculate the percentage of each top 5 category's score relative to the total score of all categories
top5_scores['Percentage of Total'] = (top5_scores['Total Scores'] / total_score_all) * 100
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 8))
plt.pie(top5_scores['Percentage of Total'], labels=top5_scores['Content category'], autopct='%1.1f%%', colors=plt.cm.Paired(range(len(top5_scores))))
plt.title('Percentage Contribution of Top 5 Categories to Total Scores')
plt.show()


num_rows = total_scores.shape[0]
print(f'Number of rows: {num_rows}')