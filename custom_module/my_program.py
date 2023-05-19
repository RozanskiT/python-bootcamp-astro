import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

from my_module import Vector3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# This is our vector that will be rotating
v = Vector3D(1, 0, 0)

# This is the second vector that will rotate around the tip of the first vector
w = Vector3D(0, 1, 0)

# This is the axis of rotation
axis = Vector3D(0, 0, 1)

# This will store the previous positions of the tip of vector B
trail = []

# This will be used to update our vector in the animation
def update(num):
    ax.cla()  # Clear the current axes
    ax.set_xlim(-2, 2)  # Set x-axis limits
    ax.set_ylim(-2, 2)  # Set y-axis limits
    ax.set_zlim(-2, 2)  # Set z-axis limits

    # Rotate our vector and get the rotated vector
    theta = num * 2  # The angle of rotation will increase with each frame
    rotated_v = v.rotate(axis, theta)
    
    # Rotate the second vector around the tip of the first vector
    rotated_w = w.rotate(rotated_v, 20*theta)
    
    # Add the new position of the tip of vector B to the trail
    trail.append(rotated_v + rotated_w)
    if len(trail) > 20:  # Limit the trail length to 20
        trail.pop(0)

    # Draw the trail
    for i, pos in enumerate(trail):
        ax.plot([pos.x], [pos.y], [pos.z], color='r', marker='o', alpha=i/20)  # Fade out older positions

    # Draw the rotated vectors
    ax.quiver(0, 0, 0, rotated_v.x, rotated_v.y, rotated_v.z, color='b')
    ax.quiver(rotated_v.x, rotated_v.y, rotated_v.z, rotated_w.x, rotated_w.y, rotated_w.z, color='r')

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 0.1), interval=100)

plt.show()

