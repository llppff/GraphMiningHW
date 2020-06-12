import sys
sys.path.append("..")

from utils import calEuclidDistanceMatrix
from utils import myKNN
from utils import calLaplacianMatrix
from utils import genTwoCircles
from utils import plot
from sklearn.cluster import KMeans
import numpy as np
np.random.seed(1)
#生成数据
data, label = genTwoCircles(n_samples=500)
#根据欧几里得距离计算相似度
Similarity = calEuclidDistanceMatrix(data)

#knn构图
Adjacent = myKNN(Similarity, k=10)

#求拉普拉斯矩阵
Laplacian = calLaplacianMatrix(Adjacent)

#进行谱聚类和k均值聚类
x, V = np.linalg.eig(Laplacian)

x = zip(x, range(len(x)))
x = sorted(x, key=lambda x:x[0])

H = np.vstack([V[:,i] for (v, i) in x[:500]]).T

sp_kmeans = KMeans(n_clusters=2).fit(H)

pure_kmeans = KMeans(n_clusters=2).fit(data)

#通过散点图显示聚类结果
plot(data, sp_kmeans.labels_, pure_kmeans.labels_)