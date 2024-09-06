#!/usr/bin/env python3
import math

# Function to calculate change in angle
def calculate_angle_change(offset_m, length_m):
    angle_radians = math.atan(offset_m / length_m)
    angle_degrees = math.degrees(angle_radians)
    return round(angle_degrees, 2)

# Main function to accept user inputs and calculate angles
def main():
    depth = float(input("Enter the depth (in meters): "))
    offset = float(input("Enter the offset (in meters): "))
    designed_angle = float(input("Enter the designed angle (in degrees): "))
    
    angle_change = calculate_angle_change(offset, depth)
    expected_drilling_angle = designed_angle + angle_change
    
    print(f"The change in angle for a depth of {depth}m and offset of {offset}m is: {angle_change} degrees")
    print(f"The expected drilling angle to achieve the design is: {expected_drilling_angle} degrees")

if __name__ == "__main__":
    main()
