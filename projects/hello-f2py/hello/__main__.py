
if __name__ == "__main__":
    from . import _cylinder_methods as cylinder_methods
    radius = 0.5
    height = 3
    area = cylinder_methods.calculate_area(radius, height)
    print("Cylinder of radius [%s] and height [%s] has an area of [%s]" % (radius, height, area))
