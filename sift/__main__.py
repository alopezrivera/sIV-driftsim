# SPDX-FileCopyrightText: © 2021 Antonio López Rivera <antonlopezr99@gmail.com>
# SPDX-License-Identifier: GPL-3.0-only

import datetime as dt

from sift.ship import ship
from sift.drift import drift
from sift.utils import title


title()


"""
PARAMETERS
"""
# LAST KNOWN COORDINATE (LKNRC)
LON0          = -6.99328484
LAT0          = 36.4607901
# RADAR POSITIONING UNCERTAINTY
RADIUS2SIGMA  = 2000             # [m]

# SHIP COORDINATES AT START OF RETRIEVAL MANEUVER
SHIP_LON      = -7.069652
SHIP_LAT      = 37.150779
# SHIP CRUISE SPEED DURING APPROXIMATION TO LKNRC
CRUISE_SPEED  = 14               # [kt]
s             = ship(lon=SHIP_LON,
                     lat=SHIP_LAT,
                     cruise_speed=CRUISE_SPEED)

# SHIP TRAVEL TIME
TRAVEL_TIME   = s.travel_time(dest_lon=LON0, dest_lat=LAT0, estimate=4*60*60):wq


# 0: DEBUG OUTPUT | 20: REDUCED OUTPUT | 50: NO OUTPUT
LOGLEVEL      = 50


def main():
    """
    SIMULATION
    """

    # SIMULATION
    drift(lon0=LON0,
          lat0=LAT0,
          radius2sigma=RADIUS2SIGMA,
          loglevel=LOGLEVEL,
          travel_time=TRAVEL_TIME,
          n=1000
          )


if __name__ == "__main__":
    main()
