import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread('C:/Users/Rasta/Downloads/i.jpg')

# Debugging
image_np = np.array(image)
plt.imshow(image_np)
plt.show()
print(image_np)


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray,(51,51),1)
plt.imshow(blurred)
plt.show()

hist = cv2.calcHist([gray],[0],None,[256],[0,256])
hist = hist.ravel()
sum_hist = np.cumsum(hist)
sum_hist_norm = sum_hist / sum_hist[-1]


# The palette 
colors = [
    [200, 150, 200],  # Purple/lilac flowers
    [90, 130, 180],   # Sky
    [230, 240, 255],  # Clouds
    [180, 180, 170],  # Stone pavement
    [40, 40, 40],     # Shadows and details
    [245, 235, 220],  # Light stone wall
    [120, 90, 70],    # Wood or door
    [60, 90, 40],     # Dark leaves
    [140, 190, 100],  # Light leaves
    [220, 100, 120],  # Pink-red flowers

]




def sort_colors_by_brightness(colors):
    def brightness(c):
        return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
    return sorted(colors, key=brightness)

    
colors_sorted = sort_colors_by_brightness(colors)


n_color = len(colors_sorted)
bounds = np.linspace(0,1,n_color +1)

# Threshold
thresholds = []
for b in bounds[1:-1]:
    id = np.searchsorted(sum_hist_norm, b)
    thresholds.append(id)
thresholds = [0] + thresholds + [255]



color_image = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)

for k in range(len(colors)):
    low_lim = thresholds[k]
    up_lim = thresholds[k+1]
    mask = (gray >= low_lim) & (gray < up_lim)  
    color_image[mask] = colors_sorted[k][::-1]

plt.imshow(cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
