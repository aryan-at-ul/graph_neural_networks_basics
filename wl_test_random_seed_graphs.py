from igraph import *
# from WL import *
import igraph
import matplotlib.pyplot as plt


def generateTree(nodes, seed):
    degree = seed;
    g = Graph.Tree(nodes, degree)
    return g

def generateRandom(seed):
    prob = seed
    g = Graph.GRG(10, prob)

def displayG(g):
    layout = g.layout("kk")
    plot(g, layout = layout)

G1 = generateTree(20, 2)
G2 = generateTree(20, 2)
#G2.layout(layout='kamada_kawai') #docs: https://igraph.org/python/doc/tutorial/tutorial.html#layouts-and-plotting
layout1 = G1.layout_kamada_kawai()
layout2 = G2.layout_circle()

G3 = generateRandom(0.1)
G4 = generateRandom(0.2)
n = 12

# algo = WL()

global_hash_gen = {}

k = 1

G1['name'] = 'G1'
G2['name'] = 'G2'

for vs in G1.vs:
    vs['cl'] = k
    vs['pl'] = k

for vs in G2.vs:
    vs['cl'] = k
    vs['pl'] = k

for v in G1.vs:
    print(v)


def hash_to_nums(h,k):
    # h.sort()
    val = h
    h = ''.join([str(x) for x in h])
    if h not in global_hash_gen.keys():
        global_hash_gen[h] = sum(val)
        k += 1

    return h,global_hash_gen[h]


def gen_hash(v):
    print(" ")
    for v in G1.vs:
        v['hashs'] = [v['cl']]
        for nv in v.neighbors():
            v['hashs'].append(nv['cl'])
        v['hashs'].sort()
        hh,nextc = hash_to_nums(v['hashs'],nv['cl'])

def all_equal(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == x for x in iterator)




def run_iterations(G,n = 2):

    for i in range(n):
        print("iteration",i)

        for index,v in enumerate(G.vs):
            print("node attributes here for one node ",i,hasattr(v,'hashs'),v.attribute_names(),v)
            if  'hashs' in v.attribute_names():
                if not v["hashs"]:
                    v['hashs']  = [v['cl']]
                else:
                    v['hashs'] = v['hashs']
            else:
                v['hashs']  = [v['cl']]
            for nv in v.neighbors():
                v['hashs'].append(nv['cl'])
            print("@@@@@@@@@@@@",v['hashs'])
            # v['hashs'].sort()
            hh,nextc = hash_to_nums(v['hashs'],nv['cl'])
            print("current hash",v,hh,nextc)
            # v['hashs'] = nextc
            # nv['cl'] = nextc
            print("labels : ",v['hashs'])

        for v in G.vs:
            print("======",v,global_hash_gen)
            key = ''.join([str(x) for x in v['hashs']])
            # current_st = global_hash_gen[v['hashs']]
            # print(current_st)
            if all_equal(v['hashs']):
                v['hashs'] = [v['cl']] + [global_hash_gen[key]]
            else:
                v['hashs'].append(global_hash_gen[key])
            v['cl'] = v['hashs'][-1]


run_iterations(G1)






print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#$@#$@#$@#$@#$@#$@#$@#$@#$@#$@#$@#$@#%$#%#$%@$#%@#$%#@$%#$%@$#%#$%#$%$#@%$#%#$%#$%@#$%#@$%#@$")
# colar = []

def update_graph(G):
    colar = []
    for v in G.vs:
        print(v)
        v['hashs'] = int(''.join([str(x) for x in v['hashs']]))#int(''.join([str(x) for x in v['hashs']))
        colar.append(v['hashs'])
    return  colar


colar = update_graph(G1)

id_gen = UniqueIdGenerator()
color_indices = [id_gen.add(value) for value in colar]
palette = ClusterColoringPalette(len(id_gen))
colors = [palette[index] for index in color_indices]
G1.vs["color"] = colors

#displayG(G1)
plot(G1, layout=layout1)


run_iterations(G2)

colar = update_graph(G2)



id_gen = UniqueIdGenerator()
color_indices = [id_gen.add(value) for value in colar]
palette = ClusterColoringPalette(len(id_gen))
colors = [palette[index] for index in color_indices]
G2.vs["color"] = colors

#displayG(G2)
plot(G2, layout=layout2)
# for e in G1.es:
#     print(e.source,e.target)


# displayG(G1)
#displayG(G2)
#print(G1)
#print(G2)
#isomorphic = algo.execute(G1, G1, 1)
#print("Isomorphic = " + str(isomorphic))

