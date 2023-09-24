from graphviz import Digraph

dot = Digraph(comment='image', format='png')

dot.node('A', 'Producers (Plants)')
dot.node('B', 'Primary Consumers')
dot.node('C', 'Secondary Consumers')
dot.node('D', 'Tertiary Consumers')

dot.edges(['AB', 'BC', 'CD'])

dot.render('image.gv')