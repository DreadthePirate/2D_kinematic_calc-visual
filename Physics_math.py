# This series of functions will take in a list of parameters and then return the ∆X 
# then take into account a 2% variance since the gun hits a little farther than what
# is expected.

import math
import matplotlib.pyplot as plt

def velocity_y(angle, Velocity_x):
   Velocity_y = Velocity_x * math.tan(math.radians(angle))  
   return Velocity_y

def max_height_time(Velocity_y, height):
    time = Velocity_y / 9.81
    Y_flight_height = 0.5 * 9.81 * time ** 2
    print("Max flight height:", Y_flight_height, "Meters\n")
    Y_max_height = height + Y_flight_height
    return Y_max_height, time

def flight_time(Y_max_height, time):
    Flight_time = math.sqrt((Y_max_height*2)/9.81) + time
    return Flight_time

def horizontal_distance(Flight_time, Velocity_x):
    X_distance = Flight_time * Velocity_x
    return X_distance

def variance_calc(X_distance):
    X_Distance_with_variance_1 = X_distance * 1.05  # Add 2% variance

    return X_Distance_with_variance_1

def main():

    height = float(input("What is the given height in meters: "))
    angle = int(input("What is the given angle in degrees: "))
    Velocity_x = float(input("What is the velocity in meters/second:\n"))

    Velocity_y = velocity_y(angle, Velocity_x)
    print("Initial Vertical velocity:", Velocity_y, " meters/second:\n")

    Y_max_height, time = max_height_time(Velocity_y, height)
    print("Max height with given height:", Y_max_height, "meters\n")
    print("Flight time for max height:", time, "seconds\n")

    Flight_time = flight_time(Y_max_height, time)
    print("Total flight time:", Flight_time, "Seconds\n")

    X_distance = horizontal_distance(Flight_time, Velocity_x)
    print("Your total X distance in meters is:", X_distance, "meters\n")

    X_Distance_with_variance = variance_calc(X_distance)
    print("Your total X Velocity in meters with a 2% variance is:", X_Distance_with_variance, "meters\n")



    # graph of trajectory:
    # Generate trajectory data
    time_values = [i * 0.01 for i in range(int(Flight_time * 100))]  # Time values at 0.01 second intervals
    height_values = [height + (Velocity_y * t - 0.5 * 9.81 * t ** 2) for t in time_values]  # Calculate height for each time point
    horizontal_values = [Velocity_x * t for t in time_values]  # Calculate horizontal distance for each time point


    # Plot trajectory
    plt.plot(horizontal_values, height_values)
    plt.xlabel('horizontal distance (m)')
    plt.ylabel('Height (m)')
    plt.title('Flight Trajectory')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()

   
