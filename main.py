import networkx as nx
import matplotlib.pyplot as plt

def main():
    creneaux = ["jeudi1","jeudi2","vendredi1","vendredi2"]
    groupes = ["A1a", "A1b", "A2a", "A2b", "B2a", "B2b", "C1a", "C1b", "C2a", "C2b", "D1a", "D1b", "D2a", "D2b"]
    cours = ["proba","analyse"]
    repartitions = {}
    for g in groupes:
        if g[0]=="A":
            repartitions[g] = {"proba":"vendredi1","analyse":"jeudi2"}
        if g[0]=="B":
            repartitions[g] = {"proba":"vendredi2","analyse":"jeudi1"}
        if g[0]=="C":
            repartitions[g] = {"proba":"jeudi2","analyse":"vendredi1"}
        if g[0]=="D":
            repartitions[g] = {"proba":"jeudi1","analyse":"vendredi2"}
    intervenants = ["C.B.", "S.V.", "O.D.", "G.L.", "C.H.", "R.G.", "K.D.", "V.T.", "E.M.", "M.B.", "E.K.", "P.M", "A.S" ]
    competences = {"proba":["C.B.", "S.V.", "O.D.", "G.L.", "C.H.", "R.G."],
                "analyse":["K.D.", "V.T.", "E.M.", "M.B.", "E.K.","P.M", "A.S"],
                "proba&analyse":["P.M", "A.S"]}
    G = nx.Graph()
    G.add_nodes_from(creneaux)
    G.add_nodes_from(groupes)
    G.add_nodes_from(intervenants)

    # nx.draw(G,with_labels=True)  
    subgraphs = []
    for c in creneaux:
        subgraph = nx.Graph()
        for m in cours:
            inter = competences[m]
            for g in groupes:
                print(c,m,inter,g)
                if repartitions[g][m] == c:
                    print(c,m,inter,g)
                    if inter != []:
                        subgraph.add_node(g)
                        i = inter.pop()
                        subgraph.add_node(i)
                        subgraph.add_edge(i,g)
        
        subgraphs.append((c,subgraph))
    for g in subgraphs:
        nx.draw(g[1],with_labels=True)
        # plt.show()
        plt.savefig(f"graph-{g[0]}.png")

if __name__ == "__main__":
    main()
