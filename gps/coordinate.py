class Coordinate(object):

    def __init__(self, lat=0.0, lon=0.0):

        self.latitude = lat
        self.longitude = lon

    def distance(self, coordinate_obj):
        """
        Calculates the distance (spherical surface of earth) between yourself
        and a destination Coordinate

        Args:
            <Coordinate>: destination coordinate

        Returns:
            float: distance in kilometers
        """
        pass

    def add(self, heading, distance):
        """
        Calculates the GPS coordinates from your location to a distance
        (spherical surface of earth) along a heading

        Args:
            heading (float): 0-180 degrees, North is 0
            distance (float): distance in km along the curvature of the earth

        Returns:
            <gps.Coordinate> object
        """
        pass
