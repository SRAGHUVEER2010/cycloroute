import math
#vector resolution
def velocity_vector(speed, direction):
    direction_radians  = math.radians(direction)
    x_component = speed * math.sin(direction_radians)
    y_component = speed * math.cos(direction_radians)
    return x_component , y_component
#calculating relative vector
def relative_velocity(x_component_wind,y_component_wind,x_component_cyclist,y_component_cyclist):

    x_component_relative = x_component_wind - x_component_cyclist
    y_component_relative = y_component_wind - y_component_cyclist

    return x_component_relative , y_component_relative
#calculating magnitude of relative velocity
def magnitude_relative_velocity(x_component_relative,y_component_relative):
    magnitude_velocity = math.sqrt(x_component_relative**2 + y_component_relative**2)
    return magnitude_velocity
#Calculating direction of relative velocity
def relative_direction(x_component_relative , y_component_relative):
    rel_direction_radian = math.atan2(x_component_relative,y_component_relative)
    rel_direction_degrees = math.degrees(rel_direction_radian)
    rel_direction = rel_direction_degrees % 360
    return rel_direction

#Calculating final relative wind
def relative_wind(wind_speed, wind_direction, cyclist_speed, cyclist_direction):
    wind_vector = velocity_vector(wind_speed, wind_direction)
    cyclist_vector = velocity_vector(cyclist_speed, cyclist_direction)

    # unpack each tuple into its x and y parts
    x_component_wind, y_component_wind = wind_vector
    x_component_cyclist, y_component_cyclist = cyclist_vector

    # now we HAVE these values, so we can pass them in
    relative = relative_velocity(x_component_wind, y_component_wind,
                                  x_component_cyclist, y_component_cyclist)

    # relative_velocity returns a tuple too, so unpack it the same way
    x_component_relative, y_component_relative = relative

    magnitude = magnitude_relative_velocity(x_component_relative, y_component_relative)
    direction = relative_direction(x_component_relative, y_component_relative)

    return magnitude, direction





    

