class Location(object):

    """Location stuff"""

    def __init__(self, lat, lon, alt):
        # TODO: handle also
        # - image x/y
        # - cartesian x/y/z
        # - spherical r/theta/phi
        # - geographic lat/lon/alt
        self.lat = lat
        self.lon = lon
        self.alt = alt


class VisibleTrajectory(Location):

    """Visible trajectory, either in image coordinates or actual 3D
    atmospheric path.
    """

    def __init__(self):
        super(VisibleTrajectory, self).__init__()
        # Other maybe relevant things, same shape as coordinates

        # Timestamp for each location
        self.time = None
        # Optional brightness?
        # * relative brightness, could maybe calibrated to abs. magnitudes
        #   in later stages when combined with other
        #   images/distances/brightnesses
        # - single pixel value, or
        # - sum of the trajectory cross section, or
        # - something else
        self.brightness = None
        # Angular or actual speed
        # * should be vector?
        # * at least for the last value we should bet 3D direction
        #   with velocity
        self.speed = None
        # Acceleration/deceleration?
        self.acceleration = None
