# SPDX-FileCopyrightText: © 2021 Antonio López Rivera <antonlopezr99@gmail.com>
# SPDX-License-Identifier: GPL-3.0-only

from sift.ship import ship
from sift.drift import drift
from sift.utils import title


"""
PARAMETERS
"""
# LAST KNOWN NOSECONE RADAR COORDINATE (LKNRC)
NOSECONE_LON0 = -6.99328484
NOSECONE_LAT0 = 36.4607901
# RADAR POSITIONING UNCERTAINTY
RADIUS2SIGMA  = 500             # [m]

# SHIP COORDINATES AT START OF RETRIEVAL MANEUVER
SHIP_LON      = -6.75
SHIP_LAT      = 36.3
# SHIP CRUISE SPEED DURING APPROXIMATION TO LKNRC
CRUISE_SPEED  = 15              # [kt/h]

# 0: DEBUG OUTPUT | 20: REDUCED OUTPUT | 50: NO OUTPUT
LOGLEVEL = 50


def main():
    """
    SIMULATION
    """
    title()

    # SETUP
    s = ship(lon=SHIP_LON,
             lat=SHIP_LAT,
             cruise_speed=CRUISE_SPEED)
    t = s.travel_time(dest_lon=NOSECONE_LON0,
                      dest_lat=NOSECONE_LAT0)

    # SIMULATION
    lon, lat = drift(nosecone_lon0=NOSECONE_LON0,
                     nosecone_lat0=NOSECONE_LAT0,
                     radius2sigma=RADIUS2SIGMA,
                     loglevel=LOGLEVEL,
                     travel_time=t
                     )

    print(f"NOSECONE :: LONGITUDE forecast   :: [deg]")
    print(f"{int(lon[0])}\n{int(lon[1])}'\n{lon[2]:.2f}''\n")
    print(f"NOSECONE :: LATITUDE forecast    :: [deg]")
    print(f"{int(lat[0])}\n{int(lat[1])}'\n{lat[2]:.2f}''\n")


if __name__ == "__main__":
    main()
