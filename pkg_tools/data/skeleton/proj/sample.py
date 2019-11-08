"""
This module implements
"""
import numpy as np

# TODO: implement, add descriptions etc
def haversine(start_lat,
          start_lon,
          end_lat,
          end_lon):
    """
        Calculate the great circle distance between two points
        on the earth (specified in decimal degrees).
        Computes distance in kms

            Parameters
        ----------
        start_lat: description
        start_lon: description

        Returns
        -------
        description
    """
    lat_1_rad, lon_1_rad = np.radians(start_lat), np.radians(start_lon)
    lat_2_rad, lon_2_rad = np.radians(end_lat), np.radians(end_lon)
    dlon = lon_2_rad - lon_1_rad
    dlat = lat_2_rad - lat_1_rad

    a = np.sin(dlat / 2.0) ** 2 + np.cos(lat_1_rad) * np.cos(lat_2_rad) * np.sin(dlon / 2.0) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    haversine_distance = 6371 * c

    return haversine_distance
