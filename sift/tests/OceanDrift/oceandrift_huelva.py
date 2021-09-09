from datetime import datetime, timedelta

from opendrift.models.oceandrift import OceanDrift
from opendrift.readers import reader_netCDF_CF_generic
from opendrift.readers import reader_global_landmask

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
"""

NOSECONE_LON0 = -6.99328484
NOSECONE_LAT0 = 36.4607901
# RADAR POSITIONING UNCERTAINTY
RADIUS2SIGMA  = 500             # [m]
# TRAVEL TIME
TRAVEL_TIME = 67.17457798331138

o = OceanDrift()

# Sea dynamics
reader_phy_15 = reader_netCDF_CF_generic.Reader(
        'C:/Users/xXY4n/DARE/_Active/Stratos IV/_Recovery/Retrieval/Search pattern/src/data/cmems_mod_ibi_phy_anfc_0.027deg-2D_PT15M-m_1627995734718.nc')
reader_wav_60 = reader_netCDF_CF_generic.Reader(
        'C:/Users/xXY4n/DARE/_Active/Stratos IV/_Recovery/Retrieval/Search pattern/src/data/dataset-ibi-analysis-forecast-wav-005-005-hourly_1627995778445.nc')

# Land
reader_landmask = reader_global_landmask.Reader(extent=[-7.361,
                                                        35.856,
                                                        -6.488,
                                                        37.150])  # mLON, mLAT, MLON, MLAT

o.add_reader([reader_phy_15, reader_wav_60, reader_landmask])

o.seed_elements(lon=NOSECONE_LON0, lat=NOSECONE_LAT0,
                time=reader_phy_15.start_time,
                number=10000, radius=RADIUS2SIGMA,
                )

o.set_config('drift:advection_scheme', 'runge-kutta')    # Propagation

o.run(end_time=reader_phy_15.start_time + timedelta(minutes=TRAVEL_TIME),
      time_step=5, time_step_output=60,
      )

loc = (o.elements.lon.mean(), o.elements.lat.mean())

o.plot(background=['x_sea_water_velocity', 'y_sea_water_velocity'])

o.animation(filename='oceandrift_huelva.mp4',
            background=['x_sea_water_velocity', 'y_sea_water_velocity']
            )
