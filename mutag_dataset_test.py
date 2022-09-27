from __future__ import print_function
print(__doc__)

import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import networkx as nx
import plotly
from grakel.datasets import fetch_dataset
from grakel.kernels import WeisfeilerLehman, VertexHistogram
import matplotlib.pyplot as plt
# Loads the MUTAG dataset
MUTAG = fetch_dataset("MUTAG", verbose=False)
G, y = MUTAG.data, MUTAG.target


print("MUTAG dataset loaded",y)
# Splits the dataset into a training and a test set
G_train, G_test, y_train, y_test = train_test_split(G, y, test_size=0.1, random_state=42)

color_dict= {0:"Red", 1:"Blue", 2:"Yellow",3:"Green", 4:"Gray", 5:"Purple", 6:"Pink"}
#[{(2188, 2189), (2190, 2189), (2198, 2196), (2189, 2190), (2193, 2188), (2193, 2194), (2195, 2194), (2194, 2195), (2191, 2190), (2191, 2196), (2187, 2186), (2196, 2198), (2190, 2191), (2187, 2195), (2192, 2191), (2195, 2187), (2186, 2187), (2191, 2192), (2196, 2191), (2188, 2187), (2197, 2196), (2189, 2188), (2187, 2188), (2196, 2197), (2188, 2193), (2192, 2193), (2193, 2192), (2194, 2193)}, {2186: 0, 2187: 1, 2188: 0, 2189: 0, 2190: 0, 2191: 0, 2192: 0, 2193: 0, 2194: 0, 2195: 1, 2196: 1, 2197: 2, 2198: 2}, {(2187, 2186): 1, (2186, 2187): 1, (2188, 2187): 2, (2187, 2188): 2, (2189, 2188): 1, (2188, 2189): 1, (2190, 2189): 2, (2189, 2190): 2, (2191, 2190): 1, (2190, 2191): 1, (2192, 2191): 2, (2191, 2192): 2, (2193, 2192): 1, (2192, 2193): 1, (2193, 2188): 1, (2188, 2193): 1, (2194, 2193): 1, (2193, 2194): 1, (2195, 2194): 2, (2194, 2195): 2, (2195, 2187): 1, (2187, 2195): 1, (2196, 2191): 1, (2191, 2196): 1, (2197, 2196): 2, (2196, 2197): 2, (2198, 2196): 1, (2196, 2198): 1}]

fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(2,5,1)

for i in range(10):
    ax = fig.add_subplot(2,5,i+1)
    color_map = {n: color_dict[c] for n, c in G[i][1].items()}
    edge_color_map = {e: color_dict[c] for e, c in G[i][2].items()}
    G1 = nx.Graph(G[i][0])
    nx.draw(G1, node_color=color_map.values(),edge_color = edge_color_map.values(), with_labels=True)
    plt.title("Graph "+str(i))
    plt.axis('off')

plt.savefig("MUTAG.png")
