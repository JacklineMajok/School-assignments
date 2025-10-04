#problem1.py
#Name: Jackline Yom Ajoh Majok
#Date: 23/09/025
#Description:A program to calculate the surface area and volume of planets in our solar system,
#   and compute each planet's volume relative to Earth's.

import math

def sphereArea(radius):
    return 4*math.pi*(radius**2)

def sphereVolume(radius):
    return (4/3)*math.pi*(radius**3)

def main():
    planet_radii = {
        "mercury": 2439.7,
        "Venus": 6051.8,
        "Earth": 6378.1,
        "Mars": 3396.2,
        "Jupiter": 71492,
        "Saturn": 60268,
        "Uranus": 25559,
        "Neptune": 24764
    }
    
    earth_Volume = sphereVolume(planet_radii["Earth"])
    print(f"{'Planet':<10}{'Surface Area (km²)':>25}{'Volume (km³)':>25}{'Volume/earth':>20}")
    print("_"*90)
    
    for planet, radius in planet_radii.items():
        area=sphereArea(radius)
        volume=sphereVolume(radius)
        ratio=volume/earth_Volume
        print(f"{planet:<10}{area:>25.2f}{volume:>25.2f}{ratio:>20.2f}")
if __name__ == "__main__":
    main()


    
    

