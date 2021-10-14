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
LON0 = -6.99328484
LAT0 = 36.4607901
# RADAR POSITIONING UNCERTAINTY
RADIUS2SIGMA  = 2000             # [m]

# SHIP COORDINATES AT START OF RETRIEVAL MANEUVER
SHIP_LON      = -7.069652
SHIP_LAT      = 37.150779
# SHIP CRUISE SPEED DURING APPROXIMATION TO LKNRC
CRUISE_SPEED  = 14               # [kt]
s = ship(lon=SHIP_LON,
         lat=SHIP_LAT,
         cruise_speed=CRUISE_SPEED)

# SHIP TRAVEL TIME
TRAVEL_TIME   = s.travel_time(dest_lon=LON0, dest_lat=LAT0, estimate=4*60*60)

# 0: DEBUG OUTPUT | 20: REDUCED OUTPUT | 50: NO OUTPUT
LOGLEVEL      = 50


def main():
    """
    SIMULATION
    """

    # SIMULATION
    lon, lat = drift(nosecone_lon0=LON0,
                     nosecone_lat0=LAT0,
                     radius2sigma=RADIUS2SIGMA,
                     loglevel=LOGLEVEL,
                     travel_time=TRAVEL_TIME,
                     )

    print(f"NOSECONE :: LONGITUDE forecast :: [deg]")
    print(f"{int(lon[0])}\n{int(lon[1]):.2f}'\n")
    print(f"NOSECONE :: LATITUDE forecast  :: [deg]")
    print(f"{int(lat[0])}\n{int(lat[1]):.2f}'\n")


if __name__ == "__main__":
    main()
