"""Data models for the camera and user specification."""
from dataclasses import dataclass

@dataclass
class DatasetSpec:
    """
    Data model for specifications of an image dataset.
    """
    overlap: float
    sidelap: float
    height: float
    scan_dimension_x: float
    scan_dimension_y: float
    exposure_time_ms: float

class Camera:
    """
    Data model for a simple pinhole camera.

    References:
    - https://github.com/colmap/colmap/blob/3f75f71310fdec803ab06be84a16cee5032d8e0d/src/colmap/sensor/models.h#L220
    - https://en.wikipedia.org/wiki/Pinhole_camera_model
    """

    pass


class Waypoint:
    """
    Waypoints are positions where the drone should fly to and capture a photo.
    """

    pass
