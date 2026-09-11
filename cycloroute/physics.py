import math
from cycloroute.wind import relative_wind
#predefining acceleration due to gravity
g = 9.81
#converting road gradient to radian angle measure
def road_gradient(gradient):
    angle_radians= math.atan(gradient/100)
    return angle_radians
#Calculating gravitational resistance
def gravitational_resistance(mass,angle_radians):
    sin_angle = math.sin(angle_radians)
    net_gravitational_force= mass * g * sin_angle
    return net_gravitational_force
#Calculating rolling resistance
def rolling_resistance(angle_radians , mass , rolling_resistance_coefficient):
    cos_angle = math.cos(angle_radians)

    rolling_force = mass * g * cos_angle * rolling_resistance_coefficient
    return rolling_force
#Calculating Aerodynamic drag
v_relative = relative_wind(wind_speed, wind_direction, cyclist_speed, cyclist_direction)
def aero_drag(air_density,coefficient_of_drag,frontal_area,v_relative):
    aerodynamic_drag  = 0.5 * air_density * coefficient_of_drag * frontal_area * v_relative ** 2
    return aerodynamic_drag