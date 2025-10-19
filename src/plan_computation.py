import typing as T
import math

import numpy as np

from src.data_model import Camera, DatasetSpec, Waypoint
from src.camera_utils import (
    compute_image_footprint_on_surface,
    compute_ground_sampling_distance,
)


def compute_distance_between_images(
    camera: Camera, dataset_spec: DatasetSpec
) -> np.ndarray:
    """Compute the distance between images in the horizontal and vertical directions for specified overlap and sidelap.

    Args:
        camera: Camera model used for image capture.
        dataset_spec: user specification for the dataset.

    Returns:
        The horizontal and vertical distance between images (as a 2-element array).
    """
    footprint = compute_image_footprint_on_surface(camera, dataset_spec.height)

    dx = footprint[0] * (1 - dataset_spec.overlap)
    dy = footprint[1] * (1 - dataset_spec.sidelap)

    return np.array([dx, dy], dtype=np.float32)


def compute_speed_during_photo_capture(
    camera: Camera, dataset_spec: DatasetSpec, allowed_movement_px: float = 1
) -> float:
    """Compute the speed of drone during an active photo capture to prevent more than 1px of motion blur.

    Args:
        camera: Camera model used for image capture.
        dataset_spec: user specification for the dataset.
        allowed_movement_px: The maximum allowed movement in pixels. Defaults to 1 px.

    Returns:
        The speed at which the drone should move during photo capture.
    """
    distance_from_surface = dataset_spec.height
    gsd = compute_ground_sampling_distance(camera, distance_from_surface)
    allowed_movement_m = allowed_movement_px * gsd
    exposure_time_s = dataset_spec.exposure_time_ms / 1000.0
    speed = allowed_movement_m / exposure_time_s

    return speed


def generate_photo_plan_on_grid(
    camera: Camera, dataset_spec: DatasetSpec
) -> T.List[Waypoint]:
    """Generate the complete photo plan as a list of waypoints in a lawn-mower pattern.

    Args:
        camera: Camera model used for image capture.
        dataset_spec: user specification for the dataset.

    Returns:
        Scan plan as a list of waypoints.

    """
    dx, dy = compute_distance_between_images(camera, dataset_spec)
    num_x = math.ceil(dataset_spec.scan_dimension_x / dx)
    num_y = math.ceil(dataset_spec.scan_dimension_y / dy)

    capture_speed = compute_speed_during_photo_capture(camera, dataset_spec)

    waypoints: T.List[Waypoint] = []
    z = dataset_spec.height

    for j in range(num_y):
        if j % 2 == 0:
            x_positions = [i * dx for i in range(num_x)]
        else:
            x_positions = [i * dx for i in reversed(range(num_x))]
        y = j * dy

        for x in x_positions:
            waypoints.append(Waypoint(position=(x, y, z), speed=capture_speed))

    return waypoints