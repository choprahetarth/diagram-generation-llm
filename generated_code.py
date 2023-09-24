from graphviz import Digraph

dot = Digraph(comment='image', format='png')

# Step 1: Draw the sun
dot.node('sun', shape='circle', label='Sun')


# Step 2: Draw rays extending from the sun
for i in range(4):
    dot.node(f'ray{i}', shape='point')
    dot.edge('sun', f'ray{i}')


# Step 3: Draw the ground
dot.node('ground', shape='rectangle', label='Ground')


# Step 4: Draw the stem
dot.node('stem', shape='point')
dot.edge('ground', 'stem')


# Step 5: Draw the leaf
dot.node('leaf', shape='oval', label='Leaf')
dot.edge('stem', 'leaf')


# Step 6: Draw chloroplasts inside the leaf

for i in range(3):
    dot.node(f'chloroplast{i}', shape='circle', label='Chloroplast')
    dot.edge('leaf', f'chloroplast{i}')


# Step 7: Connect chloroplasts with curved lines

for i in range(2):
    dot.edge(f'chloroplast{i}', f'chloroplast{i+1}', style='dashed')


# Step 8: Label chloroplasts as "chlorophyll pigments"

for i in range(3):
    dot.node(f'chlorophyll{i}', label='Chlorophyll\nPigment')
    dot.edge(f'chloroplast{i}', f'chlorophyll{i}')


# Step 9: Draw arrows from the sun to the leaf

for i in range(4):
    dot.edge(f'ray{i}', 'leaf', arrowhead='vee')


dot.render('image.gv')