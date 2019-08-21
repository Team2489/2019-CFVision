import vis
import cv2
import matplotlib.pyplot as plt

path_str = "2019VisionImages/RocketPanelStraightDark%sin.jpg"
distances = [16, 24, 36, 48, 60, 72, 96]
est_dist = []
err = []

for d in distances:
    img = cv2.imread(path_str % str(d))
    tx, ty = vis.process(img)

    est_dist.append(ty)
    err.append(abs(d - ty))

# plt.plot(distances, est_dist, c='r')
# plt.plot(distances, distances, c='g')
plt.scatter(distances, err)

plt.show()

