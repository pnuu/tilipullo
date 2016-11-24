
def read_data(filetype, fname, fname2=None):
    """Ingest (read) data and return Trajectory object (x/y image
    coordinates or alt/az values, depending on the source)
    """

    if 'ufo' in filetype:
        data = decode_ufocapture(fname)
    elif 'va' in filetype:
        data = decode_videoanalyzer(fname)
    elif 'skycam' in filetype:
        data = decode_skycam(fname, time_img=fname2)
    elif 'video' in filetype:
        data = decode_video(fname)
    else:
        data = decode_generic_image(fname)

    return data


def decode_ufocapture(fname):
    """Read and decode UFO capture log file"""
    raise NotImplementedError


def decode_videoanalyzer(fname):
    """"""
    raise NotImplementedError


def decode_skycam(fname, time_img=None):
    """"""
    raise NotImplementedError


def decode_video(fname):
    """"""
    raise NotImplementedError


def decode_generic_image(fname):
    """"""
    # Requires lens calibration, camera directions and detection of
    # meteor trail
    raise NotImplementedError
