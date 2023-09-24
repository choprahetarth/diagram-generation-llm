from graphviz import Digraph

dot = Digraph(comment='image', format='png')

dot.node('A', 'Plants', color='green', shape='ellipse')

dot.node('B', 'Herbivores', color='yellow', shape='rectangle')
dot.edge('A', 'B', arrowhead='vee')

dot.node('C', 'Carnivores', color='orange', shape='rectangle')
dot.edge('B', 'C', arrowhead='vee')

dot.node('D', 'Apex Predators', color='red', shape='rectangle')
dot.edge('C', 'D', arrowhead='vee')

dot.render('image.gv')