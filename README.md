# Introduction

This is a Pygame script that implements basic 2D kinematics. With an object oriented approach, it implements position, velocity, acceleration, friction, and elastic collisions. It is intended to be a very simple starting point for users creating games or simulations that require physics-like motion.

![python_d79uNfejXc](https://github.com/user-attachments/assets/2b188110-a71d-40cf-92c2-67c92f7896b0)

# Usage

To demo the movement, an instance of `playerClass` can be controlled using the arrow keys. This causes constant acceleration in the direction of the arrow, with a magnitude of the constant `speed`. For the demo, the console displays the player's position, velocity, and acceleration.

At the start of the script, the physics constants and window size can be adjusted.
```Python
#physics constants
friction = 0.05
speed = 0.1

#window size
window_x = 1200
windox_y = 1200
```

The `playerClass` allows the user to create a circular rigid body. Its position, velocity, and acceleration can be accessed using the variables: `x, y, velx, vely, accelx, accely`. Every game tick, the instance's movement must be updated by calling `playerPhysics()`. For example, if `player` is an instance of `playerClass`, then `player = playerPhysics(player)` must be called.

`renderCircle` is included to render a circle at the player's position. The first parameter is the object of type `playerClass` and the second is the circle's size.

![image](https://github.com/user-attachments/assets/c2e429b3-e4e8-4746-a142-de97580074aa)

# Installation
Make sure the latest version of Python is installed. The package `pygame` must be installed first.

`pip install pygame`

`git clone https://github.com/shaan-s/2dPhysicsSim`

Then run `main.py`.
