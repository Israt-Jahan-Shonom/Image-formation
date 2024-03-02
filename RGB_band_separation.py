from google.colab import drive
drive.mount('/content/drive')

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Read the image
img = mpimg.imread('/content/drive/MyDrive/RGB_image.jpg')  # Replace 'RGB_image.jpg' with the path to your image file

# Separate the RGB channels
red_channel = img[:,:,0]
green_channel = img[:,:,1]
blue_channel = img[:,:,2]

# Display the original image and the separated channels
plt.figure(figsize=(10, 6))

# Display the original image
plt.subplot(2, 2, 1)
plt.imshow(img)
plt.title('Original RGB Image')

# Display the red channel
plt.subplot(2, 2, 2)
plt.imshow(red_channel, cmap='Reds')
plt.title('Red Channel')

# Display the green channel
plt.subplot(2, 2, 3)
plt.imshow(green_channel, cmap='Greens')
plt.title('Green Channel')

# Display the blue channel
plt.subplot(2, 2, 4)
plt.imshow(blue_channel, cmap='Blues')
plt.title('Blue Channel')

# Adjust spacing between subplots
plt.subplots_adjust(hspace=0.3, wspace=0.2)
plt.savefig("separated_R_G_B.png")

plt.show()