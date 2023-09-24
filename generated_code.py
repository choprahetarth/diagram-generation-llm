from graphviz import Digraph

dot = Digraph(comment='image', format='png')

dot.node('A', 'Sunlight')
dot.node('B', 'Chlorophyll')
dot.node('C', 'Photosynthesis')
dot.node('D', 'Glucose and Oxygen')

dot.edge('A', 'B', 'Absorption')
dot.edge('B', 'C', 'Conversion')
dot.edge('C', 'D', 'Production')

dot.render('image.gv')