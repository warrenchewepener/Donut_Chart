import matplotlib.pyplot as plt

# List of Mental Illnesses

labels = ["Schizophrenia", "Depression", "Manic Depression", 
          "Obsessive Compulsive Disorder", "Normal People"]

# Corresponding sizes

sizes = [1, 3.8, 2.4, 3, 89.8]

# Define colors for better visualization

colors = ["firebrick", "olivedrab", "steelblue", "crimson", "gray"]

# Create a figure and axis with extra width for the legend

fig, ax = plt.subplots(figsize=(8.5, 6))  # Increased width to accommodate legend

# Plot the pie chart without labels to avoid congestion

wedges, texts, autotexts = ax.pie(
    sizes, labels=None, autopct="%1.1f%%",
    startangle=120, colors=colors,
    pctdistance=0.85, textprops={'fontsize': 10}
)

# Create the inner circle for the donut effect

centre_circle = plt.Circle((0, 0), 0.70, fc="purple")
ax.add_artist(centre_circle)

# Add a legend slightly inward to fit well within the page

plt.legend(wedges, labels,  
           loc="center right", bbox_to_anchor=(0.85, 1), fontsize=10, frameon=False)

# Set the title

ax.set_title("Mental Illnesses in the World", fontsize=16, fontweight="bold")

# Ensure the pie chart is drawn as a circle

ax.axis("equal")

# Adjust layout to fit everything neatly

fig.tight_layout()

# Show the plot

plt.show()
