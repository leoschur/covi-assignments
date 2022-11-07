# %%
import cv2


# %%
kurbis_stats, labels, stats, centroids = cv2.connectedComponentsWithStats(
    kuerbis_tresh)
plt.imshow(labels, cmap='rainbow')

# %%
sorted_stats = []
labels_copy = np.zeros_li
