
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
    pass


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
