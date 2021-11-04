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

    def destination(self, heading, distance):
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

    def course(Coordinate, Coordinate):
        """
        Given an origin and destination, this function will calculate the
        course (degrees, distance) necessary to reach the destination

        Args:
            origin (GPSCoordinate):
            destination (GPSCoordinate):

        Returns:
            tuplple(float, float): direction, distance
        """
        pass
