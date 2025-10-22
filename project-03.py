import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample DataFrame
data = {
    "Ship_Mode": ["Standard Class", "First Class", "Same Day", "Standard Class", "First Class"],
    "Product_Category": ["Furniture", "Technology", "Furniture", "Office Supplies", "Technology"],
    "Product_Count": [200, 150, 50, 300, 200]
}
df = pd.read_excel('D:\p.xlsx')
# Pivot the DataFrame for visualization
pivot_table = df.pivot(index="Ship_Mode", columns="Product_Category", values="Product_Count")

# Heatmap Visualization
plt.figure(figsize=(10, 6))
sns.heatmap(pivot_table, annot=True, fmt="d", cmap="Blues")
plt.title("Ship Mode vs Product Category")
plt.xlabel("Product Category")
plt.ylabel("Ship Mode")
plt.show()

