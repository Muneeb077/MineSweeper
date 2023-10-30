# Import the 'configure' module, which likely contains configuration settings

import configure

# Define a function to calculate the height based on a given percentage
def height_prct(percentage):
    return (configure.HEIGHT / 100) * percentage

# Define a function to calculate the width based on a given percentage
def width_prct(percentage):
    return (configure.WIDTH / 100) * percentage
