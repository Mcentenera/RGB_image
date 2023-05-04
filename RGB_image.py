from astropy.io import fits
from astropy.wcs import WCS
from astropy.nddata import CCDData
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import numpy.ma as ma
from pathlib import Path
from astropy import units as u
from tea_utils import tea_avoid_astropy_warnings
from astropy.visualization import LogStretch
from astropy.visualization import MinMaxInterval
from astropy.visualization import make_lupton_rgb

time_ini = datetime.now()

tea_avoid_astropy_warnings(True)

forCasting = np.float_()

g = fits.open('NGC4490_combination_sdssg.fits')[0].data
r = fits.open('NGC4490_combination_sdssr.fits')[0].data
alpha = fits.open('NGC4490_combination_658_10.fits')[0].data

### CASTING
g = np.array(g,forCasting)
r = np.array(r,forCasting)
alpha = np.array(alpha,forCasting)

stretch = LogStretch() + MinMaxInterval()

g = stretch(g)
r = stretch(r)
alpha = stretch(alpha)

plt.imshow(g, origin='lower')
plt.imshow(r, origin='lower')
plt.imshow(alpha, origin='lower')

lo_val, up_val = np.percentile(np.hstack((g.flatten(), r.flatten(), alpha.flatten())), (0.5, 99.5))  # Get the value of lower and upper 0.5% of all pixels

stretch_val = up_val - lo_val

rgb_default = make_lupton_rgb(alpha*0.6, r*0.9, g*1.1, minimum=lo_val, stretch=stretch_val, Q=0, filename="RGB_image_alpha.pdf")
plt.imshow(rgb_default, origin='lower')
plt.show()

time_end = datetime.now()
print(f"Initial time...: {time_ini}")
print(f"Final time.....: {time_end}")
print(f"Excecution time: {time_end-time_ini}")
