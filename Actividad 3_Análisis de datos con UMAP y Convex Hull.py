# Carlos Ignacio Ramirez Preciado - 219431231
# Osiris Josue Carrillo Galvan - 219440516

!pip install anndata
from google.colab import drive
drive.mount('/content/drive')
import anndata as ad
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.spatial import ConvexHull

file_path = '/content/drive/MyDrive/Analisis de Algoritmos/Datos.h5ad'
adata = ad.read_h5ad(file_path)
umap_coords = adata.obsm['X_UMAP']
clusters = adata.obs['cluster_id']

print(adata, '\n', umap_coords, '\n', clusters)

def plot_clusters_with_hulls(umap_coords, clusters):
    plt.figure(figsize=(8, 8))
    unique_clusters = np.unique(clusters)

    for cluster in unique_clusters:
        cluster_points = umap_coords[clusters == cluster]
        hull = ConvexHull(cluster_points)
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f'Cluster {cluster}')

        for simplex in hull.simplices:
            plt.plot(cluster_points[simplex, 0], cluster_points[simplex, 1], 'k-')

    plt.title('Convex Hull')
    plt.legend()
    plt.show()

plot_clusters_with_hulls(umap_coords, clusters)
