"""Utility to visualize photo plans.
"""

import typing as T

import plotly.graph_objects as go

from src.data_model import Waypoint


def plot_photo_plan(photo_plans: T.List[Waypoint]) -> go.Figure:
    """Plot the photo plan on a 2D grid.

    Args:
        photo_plans: List of waypoints for the photo plan.

    Returns:
        Plotly figure object.
    """
    xs = [wp.position[0] for wp in photo_plans]
    ys = [wp.position[1] for wp in photo_plans]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=xs, y=ys,
        mode='lines+markers',
        name='Flight Path',
        marker=dict(size=6),
        line=dict(width=2),
    ))

    fig.add_trace(go.Scatter(
        x=[xs[0]], y=[ys[0]],
        mode='markers',
        name='Start',
        marker=dict(size=10, symbol='x')
    ))

    fig.add_trace(go.Scatter(
        x=[xs[-1]], y=[ys[-1]],
        mode='markers',
        name='End',
        marker=dict(size=10, symbol='x')
    ))

    fig.update_layout(
        title="Drone Photo Plan (Top View)",
        xaxis_title="X Position (meters)",
        yaxis_title="Y Position (meters)",
        xaxis=dict(scaleanchor="y", scaleratio=1),
        template="plotly_white",
        showlegend=True
    )

    return fig
