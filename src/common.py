DATA_FOLDER='../data/' # end with /
ERROR_CODE=999

import numpy as np
import six

import warnings
warnings.filterwarnings('ignore')

def image_visualization(image,title=None):
    import matplotlib.pyplot as plt
    plt.figure()
    plt.imshow(image,interpolation=None)
    plt.colorbar()
    if title!=None:
        plt.title(title)


def logamplitude(S, ref_power=1.0, amin=1e-10, top_db=80.0):
    """Log-scale the amplitude of a spectrogram. as in Librosa"""

    if amin <= 0:
        print 'amin must be strictly positive'

    magnitude = np.abs(S)

    if six.callable(ref_power):
        # User supplied a function to calculate reference power
        __ref = ref_power(magnitude)
    else:
        __ref = np.abs(ref_power)

    log_spec = 10.0 * np.log10(np.maximum(amin, magnitude))
    log_spec -= 10.0 * np.log10(np.maximum(amin, __ref))

    if top_db is not None:
        if top_db < 0:
            print 'top_db must be non-negative positive'
        log_spec = np.maximum(log_spec, log_spec.max() - top_db)

    return log_spec
