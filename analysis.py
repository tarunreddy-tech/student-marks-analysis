import pandas as pd

data = {
    'Name': ['A', 'B', 'C'],
    'Marks': [85, 90, 78]
}

df = pd.DataFrame(data)

print("Average Marks:", df['Marks'].mean())
print("Highest Marks:", df['Marks'].max())
