import numpy as np
from sklearn import datasets
from matplotlib import pyplot as plt
from itertools import cycle, islice

#根据欧几里得距离求相似度
def euclidDistance(x1, x2, sqrt_flag=False):
    res = np.sum((x1-x2)**2)
    if sqrt_flag:
        res = np.sqrt(res)
    return res

def calEuclidDistanceMatrix(X):
    X = np.array(X)
    S = np.zeros((len(X), len(X)))
    for i in range(len(X)):
        for j in range(i+1, len(X)):
            S[i][j] = 1.0 * euclidDistance(X[i], X[j])
            S[j][i] = S[i][j]
    return S

#获取数据
def genTwoCircles(n_samples=1000):
    X,y = datasets.make_circles(n_samples, factor=0.5, noise=0.05)
    return X, y


#knn方式构图
def myKNN(S, k, sigma=1.0):
    N = len(S)
    A = np.zeros((N,N))

    for i in range(N):
        dist_with_index = zip(S[i], range(N))
        dist_with_index = sorted(dist_with_index, key=lambda x:x[0])
        neighbours_id = [dist_with_index[m][1] for m in range(k+1)] # xi's k nearest neighbours

        for j in neighbours_id: # xj is xi's neighbour
            A[i][j] = np.exp(-S[i][j]/2/sigma/sigma)
            A[j][i] = A[i][j] # mutually

    return A


#求拉普拉斯矩阵
def calLaplacianMatrix(adjacentMatrix):

    # 计算度矩阵
    degreeMatrix = np.sum(adjacentMatrix, axis=1)


    # 计算拉普拉斯矩阵
    laplacianMatrix = np.diag(degreeMatrix) - adjacentMatrix


    # normailze
    sqrtDegreeMatrix = np.diag(1.0 / (degreeMatrix ** (0.5)))
    return np.dot(np.dot(sqrtDegreeMatrix, laplacianMatrix), sqrtDegreeMatrix)

#以图方式显示结果
def plot(X, y_sp, y_km):
    colors = np.array(list(islice(cycle(['#90EE90', '#ff0000']),
                                        int(max(y_km) + 1))))
    plt.subplot(121)
    plt.scatter(X[:,0], X[:,1], s=10, color=colors[y_sp])
    plt.title("Spectral Clustering")
    plt.subplot(122)
    plt.scatter(X[:,0], X[:,1], s=10, color=colors[y_km])
    plt.title("Kmeans Clustering")
    plt.savefig("spect_vs_km_clst.png")