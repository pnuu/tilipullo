class VisibleFlight(object):

    """Collects Observations, merges them and calculates the 3D
    atmoshpheric trajectory for the visible portion of the flight.

    Could be used by eg. DarkFlight() and SolarOrbit() classes

    """

    def __init__(self):
        # Separate observations
        self.observations = []

        # Trajectory for visible flight will in the end hold
        # - x/y/z coordinates, or
        # - lat/lon/alt, or
        # - spherical coordinates
        # - time at each point
        # - speed, deceleration at each point
        # - brightness?
        self.trajectory = None

    def add_observation(self, obs):
        self.observations.append(obs)

    def solve_trajectory(self):
        self.trajectory = self._solve_trajectory()
