# SPDX-FileCopyrightText: © 2021 Antonio López Rivera <antonlopezr99@gmail.com>
# SPDX-License-Identifier: GPL-3.0-only

import os
from datetime import datetime, timedelta

from opendrift.opendrift.models.oceandrift import OceanDrift
from opendrift.opendrift.readers import reader_netCDF_CF_generic
from opendrift.opendrift.readers import reader_global_landmask

from sift.utils import d_to_dms


def drift(nosecone_lon0,
          nosecone_lat0,
          radius2sigma,
          travel_time,
          plot=False,
          animation=False,
          loglevel=0):
    """
    # Model:
        OceanDrift
            - loglevel: (0: debug info); (20: reduced output); (50: no output)

    # Readers:
        Physics
            - https://resources.marine.copernicus.eu/?option=com_csw&view=details&product_id=IBI_ANALYSISFORECAST_PHY_005_001
        Waves
            - https://resources.marine.copernicus.eu/?option=com_csw&view=details&product_id=IBI_ANALYSIS_FORECAST_WAV_005_005
        Landmask
            - Taken from the [GSHHG](https://www.soest.hawaii.edu/pwessel/gshhg/) database
                - mLON: -7.361
                - mLAT: 35.856
                - MLON: -6.488
                - MLAT: 37.150

    :param nosecone_lon0: [deg] Last known nosecone longitude obtained by radar.
    :param nosecone_lat0: [deg] Last known nosecone latitude obtained by radar.
    :param radius2sigma:  [m]   Radar positioning uncertainty.
                                    Radius around radar last known coordinate within
                                    which lie 66.7% of real nosecone coordinates.
    :param travel_time:   [min] Travel time from ship position to _nosecone_loc0_.
    :param plot: Plot nosecone drift simulation trajectories. Default: False
    :param animation: Animate nosecone drift simulation trajectories. Default: False
    :param loglevel: 0 -> Debug, 20 -> Reduced output, 50 -> No output

    :return: [deg] Simulated nosecone longitude _travel_time_ after slpashdown.
             [deg] Simulated nosecone latitude _travel_time_ after slpashdown.
    """

    o = OceanDrift(loglevel=loglevel)

    # Sea dynamics
    reader_phy_15 = reader_netCDF_CF_generic.Reader(os.path.join('data', [i for i in os.listdir('data') if 'phy' in i][0]))
    reader_wav_60 = reader_netCDF_CF_generic.Reader(os.path.join('data', [i for i in os.listdir('data') if 'wav' in i][0]))

    # Land
    reader_landmask = reader_global_landmask.Reader(extent=[-7.361,
                                                            35.856,
                                                            -6.488,
                                                            37.150])  # mLON, mLAT, MLON, MLAT

    o.add_reader([reader_phy_15, reader_wav_60, reader_landmask])

    o.seed_elements(lon=nosecone_lon0, lat=nosecone_lat0,
                    time=datetime.now(),
                    number=10000, radius=radius2sigma,
                    )

    o.set_config('drift:advection_scheme', 'runge-kutta')    # Propagation

    o.run(end_time=datetime.now() + timedelta(minutes=travel_time),
          time_step=5, time_step_output=60,
          )

    if plot:
        o.plot(background=['x_sea_water_velocity', 'y_sea_water_velocity'])

    if animation:
        o.animation(filename='oceandrift_huelva.mp4',
                    background=['x_sea_water_velocity', 'y_sea_water_velocity']
                    )

    sim_lon = d_to_dms(o.elements.lon.mean())
    sim_lat = d_to_dms(o.elements.lat.mean())

    return sim_lon, sim_lat
