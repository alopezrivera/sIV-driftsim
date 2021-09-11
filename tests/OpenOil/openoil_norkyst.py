# SPDX-FileCopyrightText: © 2021 Antonio López Rivera <antonlopezr99@gmail.com>
# SPDX-License-Identifier: GPL-3.0-only

from numpy import random as rnd

from opendrift.opendrift.models.openoil import OpenOil
from opendrift.opendrift.readers import reader_netCDF_CF_generic
from opendrift.opendrift.readers import reader_global_landmask

"""
# Model:
    OceanDrift
        - loglevel: (0: debug info); (20: reduced output); (50: no output)

# Readers:
    Sea current
        -
    Landmask
    reader_global_landmask
        - Taken from the [GSHHG](https://www.soest.hawaii.edu/pwessel/gshhg/) database
"""
# Model
o = OpenOil(loglevel=0)

# Readers
reader_norkyst = reader_netCDF_CF_generic.Reader(
    'https://thredds.met.no/thredds/dodsC/sea/norkyst800m/1h/aggregate_be')
reader_landmask = reader_global_landmask.Reader(
    extent=[2, 59, 8, 63])  # lonmin, latmin, lonmax, latmax

print(reader_norkyst)

o.add_reader([reader_landmask, reader_norkyst])

# Seed
o.seed_elements(lon=4.3, lat=60, number=100, radius=1000,
                density=rnd.uniform(880, 920, 100),
                time=reader_norkyst.start_time)

# Model configuration
o.set_config('drift:advection_scheme', 'runge-kutta')       # Propagation
o.set_config('seed:wind_drift_factor', .02)                 # Wind speed drift factor

o.run(end_time=reader_norkyst.end_time, time_step=900,
      time_step_output=3600, outfile='openoil.nc',
      export_variables=['density', 'water_content'])

# o.plot(linecolor='z',
#        background=['x_sea_water_velocity', 'y_sea_water_velocity'])
#
# o.animation()
