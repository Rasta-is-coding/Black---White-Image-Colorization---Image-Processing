# :paintbrush:🎨 Colorizing Black & Withe Images using Python
There are several tecniques to paint black and white pictures, and this task is no longer something wild. AI can do this for you almost flawlessly in less than a minute. But I tried one of the popular tecniques called **Histogram-Based Painting Technique in Coloring Pictures**, which was so cool to try! 

<br>

# :rainbow: How does the program work?
This program follows these steps:

- 📷 Loads the original black and white image  
- 📊 Calculates the histogram (distribution of brightness values)  
- 🎚️ Sorts custom colors by brightness  
- 🔪 Determines threshold values based on the histogram  
- 🖌️ Maps each brightness range to a corresponding color — and voilà, it's painted!

<br>


## :framed_picture: Results

### Original Image
For example, this is the original Image:

<br>
<p align ="center">
    <image src="images/Figure_1_The_Image.png" alt="Original Image" width="50%">
</p>
<br>
<br>

### Colorized Image
After applying the color, the picture would be like this: 

<br>
<p align ="center">
    <image src="images/Figure_2_Colorized_Image.png" alt="Colored Image" width="50%">
</p>
<br>
<br>

**Ta da!**:sparkles: The image is colored now! Aesthetic!:lollipop:

The reason the image is colored this way *-and not like a classic spectacular image-* is that this technique has limitations due to the black and white mapping not being efficient enough and the *color palette* you use.

I used this palette:
```python
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
``` 

You can use other palettes!
<br>
<br>
<br>
* If you have any comments on this, let me know!
