from graph_model import Graph


# 读入nodes文件，存到列表中
def get_vertices(nodes_file_path):
    # 先按字典形式读入，再获取每行key为node_no时对应的value
    with open(nodes_file_path, 'r') as csvfile:
        node_reader = csv.DictReader(csvfile)
        vertices = [int(row["node_no"]) for row in node_reader]

    return vertices


#读入edges文件，存在列表中，每条边以元组形式存放
def get_edges(edges_file_path):

    #将读入的边以列表形式存放，以便将字符串改为整型。
    # 因为读入的边的列表的每个元素是字符串，例如[['1','2'],['1','5']]
    with open(edges_file_path) as f:
        edges = [list(line) for line in csv.reader(f)]

    #将每条边的首尾改为整型，并把每条边转换为元组形式存放
    for i in range(len(edges)):
        edges[i][0] = int(edges[i][0])
        edges[i][1] = int(edges[i][1])
        edges[i] = tuple(edges[i])


    return edges




import csv
if __name__ == "__main__":
    #定义存放图的节点和边信息的文件路径
    nodes_file_path = "data/nodes.csv"
    edges_file_path = "data/edges.csv"



    #获取vertices和edges
    vertices = get_vertices(nodes_file_path)
    edges = get_edges(edges_file_path)



    #根据上方得到的vertices和edges进行相应的计算
    no = 1
    graph = Graph(vertices, edges)


    # 计算average clustering_coefficient
    aver_clust_coeffi = graph.average_clustering_coefficient()
    print("average_clustering_coefficient is:" + str(aver_clust_coeffi))

    #计算betweeness
    betweeness = graph.betweenness_centrality(no)
    print(str(no) + "'betweeness is:" + str(betweeness))