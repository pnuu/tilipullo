
def get_gfs_sounding(timeslot, lat, lon, interp=None, step=200.):
    """Get GFS sounding data for the given timeslot."""
    fname = fetch_gfs_data(timeslot, lat, lon)
    return read_gfs_data(fname, lat, lon, interp=interp, step=200.)


def fetch_gfs_data(timeslot, lat, lon):
    """Fetch GFS data, manage caching etc"""
    pass


def read_gfs_data(fname, lat, lon, interp=None, step=200.):
    """Read sounding data from GFS grib file."""
    pass


def get_balloon_sounding(timeslot, lat, lon, interp=None, step=200.):
    """Read balloon sounding from UWYO."""
    pass
