class Camera(object):

    """Class describing the camera"""

    def __init__(self, location, lens=None):

        # Camera location, Location object
        self.location = location

        # Lens projection parameters
        # * Lens object
        # * semi-static parameters for the camera
        # - projection type
        # - projection center location
        # - other relevant stuff to describe the projection
        self.lens = lens

        # Camera orientation
        # * needs more frequent updates
        self.tilt = 0.0
        self.yaw = 0.0
        self.pitch = 0.0

        # Other stuff that could be here:
        # - saturation limit
        # - camera ID
        # - sensor size
        # - pixel size
        # - pixel aspect ratio
        # - interlace/progressive scan

    def calibrate(self, img, full=False):
        """Calibrate camera orientation"""
        # If full calibration, calibrate also lens parameters,
        # otherwise only camera orientation.
        if full or self.lens is None:
            # self.lens = Lens()
            # self.lens.calibrate(img, otherstuff)
            pass
        angles = self._calibrate(img)
        self.tilt = angles[0]
        self.yaw = angles[1]
        self.pitch = angles[2]

    def xy2altaz(self, x_vals, y_vals):
        """Convert image X/Y coordinates to altitude and azimuth using lens
        parameters, camera pointing angles and other stuff
        """
        from vostok import implementation
        return implementation(x_vals, y_vals)


class Lens(object):

    """Class to describe lens(+camera?) projection parameters
    """

    def __init__(self):
        self.proj_type = "asdasd"
        self.focal_length = 3.0

    def calibrate
