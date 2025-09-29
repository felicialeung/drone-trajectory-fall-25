"""Data models for the camera and user specification."""
from dataclasses import dataclass

@dataclass
class DatasetSpec:
    """
    Data model for specifications of an image dataset.

    overlap : float
        Ratio (0 to 1) of scene overlap between two consecutive images
        along the flight path (forward overlap).
    sidelap : float
        Ratio (0 to 1) of scene overlap between two adjacent flight lines
        (side overlap).
    height : float
        Flight or scanning height above ground in meters.
    scan_dimension_x : float
        Horizontal size of the area to be scanned, in meters.
    scan_dimension_y : float
        Vertical size of the area to be scanned, in meters.
    exposure_time_ms : float
        Camera exposure time per image, in milliseconds.
    """
    overlap: float
    sidelap: float
    height: float
    scan_dimension_x: float
    scan_dimension_y: float
    exposure_time_ms: float


@dataclass
class Camera:
    """
    Data model for a simple pinhole camera.

    fx : float
        Focal length along the x-axis in pixels.
    fy : float
        Focal length along the y-axis in pixels.
    cx : float
        Optical center (principal point) x-coordinate in pixels.
    cy : float
        Optical center (principal point) y-coordinate in pixels.
    sensor_size_x_mm : float
        Physical sensor width in millimetres.
    sensor_size_y_mm : float
        Physical sensor height in millimetres.
    image_size_x_px : int
        Image width in pixels.
    image_size_y_px : int
        Image height in pixels.

    References:
    - https://github.com/colmap/colmap/blob/3f75f71310fdec803ab06be84a16cee5032d8e0d/src/colmap/sensor/models.h#L220
    - https://en.wikipedia.org/wiki/Pinhole_camera_model
    """
    fx: float
    fy: float
    cx: float
    cy: float
    sensor_size_x_mm: float
    sensor_size_y_mm: float
    image_size_x_px: int
    image_size_y_px: int


class Waypoint:
    """
    Waypoints are positions where the drone should fly to and capture a photo.
    """

    pass
