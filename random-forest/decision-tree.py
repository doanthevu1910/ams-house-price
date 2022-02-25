from sklearn.tree import export_graphviz
import pydot

tree = rf.estimators_[5]
export_graphviz(tree, out_file ='../graphs/tree.dot', feature_names = feature_list, rounded = True, precision = 1)
(graph, ) = pydot.graph_from_dot_file('../graphs/tree.dot')
graph.write_png('graphs/tree.png')