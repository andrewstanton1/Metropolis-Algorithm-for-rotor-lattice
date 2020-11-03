"""
Default parameters used for quick start demo. 
"""

# NxN size of lattice
N = 4
# number of data points
num_data_points = 10
# starting data value
l_range = 0.6
# ending data value
r_range = 2.6
# number of monte carlo steps for equilibration
equilibration_steps = 1000
# number of monte carlo steps to average over
steps_to_average = 1000
# 18.80436397 # coefficient of rotation potential
rotational_potential = 0

"""
Suggested parameters to see equilibration based on rotational potential are: 
  rotational_potential = 0         # expected runtime = 1.25 hours
  N = 16
  num_data_points = 10  
  l_range = 0.6
  r_range = 2.6
  equilibration_steps = 10000
  steps_to_average = 1000
"""

