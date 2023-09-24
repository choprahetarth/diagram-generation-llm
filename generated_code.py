from graphviz import Digraph

dot = Digraph(comment='image', format='png')

# Step 1
dot.node('line', shape='plaintext', label='')

# Step 2
dot.node('sun', shape='circle', label='Sun/Plant')

# Step 3
dot.node('herbivore', shape='circle', label='Herbivore')

# Step 4
dot.edge('sun', 'herbivore')

# Step 5
dot.node('carnivore', shape='circle', label='Carnivore')

# Step 6
dot.edge('herbivore', 'carnivore')

# Step 7
dot.node('consumer', shape='circle', label='Consumer')
dot.edge('carnivore', 'consumer')

# Step 8
dot.node('top_predator', shape='circle', label='Top Predator')
dot.edge('consumer', 'top_predator')

# Step 9
dot.node('omnivore', shape='circle', label='Omnivore')
dot.edge('herbivore', 'omnivore')

# Step 10
dot.node('title', shape='plaintext', label='Food Chain')
dot.edge('title', 'sun')

dot.render('image.gv')