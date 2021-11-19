
from math import sin, cos, asin, acos, atan, sqrt, radians

Rearth = 6371.07103  # km


def distance(lat1, lon1, lat2, lon2):
    """
    Calculates the distance between two coordinates

    Args:
        lat1 (float): latitude of origin coordinate
        lon1 (float): longitude of origina coordinate
        lat2 (float): latitude of destination coordinate
        lon2 (float): longitude of destination coordinate

    Returns:
        float: distance between two coordinates
    """
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    print(lat1, lat2)
    print(lon1, lon2)

    delta_lat = (lat2 - lat1)
    delta_lon = (lon2 - lon1)
    print(f"delta_lat = {delta_lat}")
    print(f"delta_lon = {delta_lon}")

    # central_angle = 2*asin(
    #     sqrt(
    #         sin(delta_lat/2)**2
    #         + cos(lat2)*cos(lat1)*(sin(delta_lon/2))**2
    #     )
    # )
    central_angle = 2 * atan(
        2 * (

        )

    )

    return Rearth * central_angle


def heading(lat1, lon1, lat2, lon2):
    """
    Calculates the heading between two coordinates

    Args:
        lat1 (float): latitude of origin coordinate
        lon1 (float): longitude of origina coordinate
        lat2 (float): latitude of destination coordinate
        lon2 (float): longitude of destination coordinate

    Returns:
        float: heading between two coordinates
    """
    pass


def course(lat1, lon1, lat2, lon2):
    """
    Calculates the heading and distance between two coordinates

    Args:
        lat1 (float): latitude of origin coordinate
        lon1 (float): longitude of origina coordinate
        lat2 (float): latitude of destination coordinate
        lon2 (float): longitude of destination coordinate

    Returns:
        (float, float): heading and distance between two coordinates
    """
    pass


def destination(lat, lon, heading, distance):
    """
    Starting from a coordinate, calculates the destination coordinates
    given a course

    Args:
        lat (flaot): latitude of origin coordinate
        lon (float): longitude of origin coordinate
        heading (float): 0-180 degrees, North is 0
        distance (float): distance in km along the curvature of the earth

    Returns:
        (flaot, float): destination coordinate
    """
    pass
