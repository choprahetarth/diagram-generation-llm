import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

fig, ax = plt.subplots()

# Draw arrows as edges
arrow = FancyArrowPatch((0.3, 0.5), (0.7, 0.6),mutation_scale=15, arrowstyle='-|>', color='k',lw=1)
ax.add_patch(arrow)

arrow = FancyArrowPatch((0.3, 0.4), (0.7, 0.4),mutation_scale=15, arrowstyle='-|>', color='k',lw=1)
ax.add_patch(arrow)

# Create Nodes using text
plt.text(0.2, 0.6, "Light-Dependent Reactions:\nAbsorb sunlight\nSplit H2O\nGenerate ATP \n& NADPH", 
         size=12, ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec="black",
                   fc="white",
                   )
         )

plt.text(0.8, 0.6, r"ATP & NADPH for Next Steps", 
         size=12, ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec="black",
                   fc="white",
                   )
         )

plt.text(0.2, 0.4, "Light-Independent Reactions\n(Calvin Cycle):\nUse ATP and NADPH\nFix CO2\nProduce & Store Glucose", 
         size=12, ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec="black",
                   fc="white",
                   )
         )

plt.text(0.8, 0.4, r"Glucose Stored", 
         size=12, ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec="black",
                   fc="white",
                   )
         )

# Hide axis
ax.axis('off')
plt.show()