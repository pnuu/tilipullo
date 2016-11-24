class DarkFlight(object):

    """Dark flight calculation handler"""

    def __init__(self, config):
        self.config = config
        self.data = None

    def run(self):
        if config["mode"] == "simple":
            self.data = self._simple_dark_flight()
        elif config["mode"] == "mc":
            self.data = self._monte_carlo()
