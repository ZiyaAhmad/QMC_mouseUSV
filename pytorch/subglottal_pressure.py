import torch


def subglottal_pressure(respiratory_muscle_activity):
    """
    Port of subglottal_pressure.m (mouse constants).

    Args:
        respiratory_muscle_activity: tensor, values in [0, 1].
            Purely elementwise, so any shape works -> (batch,), (batch, time), etc.

    Returns:
        Tensor of subglottal pressure (Pa), same shape as input.
    """
    pressure_max = 2e3       # mouse value, from Riede's email
    room_pressure = 101.325  # normal air pressure (Pa)
    pressure_min = room_pressure

    return pressure_min + respiratory_muscle_activity * (pressure_max - pressure_min)