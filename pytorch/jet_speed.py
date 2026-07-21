import torch

def jet_speed_from_pressure(glottal_area, pressure):
    """
    Port of jet_speed.m, 'p' mode.

    Computes jet speed from subglottal pressure using a fluid-dynamics
    orifice/constriction model (uses Bernoulli formula).

    Args:
        glottal_area: tensor, glottal cross-sectional area (m^2).
        pressure: tensor, subglottal pressure (Pa).

    Returns:
        Tensor of jet speed (m/s), broadcast shape of inputs.
    """
    tracheal_area = 0.95e-6  # m^2, mouse (extrapolated, Håkansson et al. 2022)
    tracheal_diameter = 2 * torch.sqrt(torch.tensor(tracheal_area) / torch.pi)
    glottal_diameter = 2 * torch.sqrt(glottal_area / torch.pi)

    beta = glottal_diameter / tracheal_diameter

    room_pressure = 101.325  # Pa
    air_density = 1.225      # kg/m^3

    driving_pressure = torch.clamp(pressure - room_pressure, min=1e-6)

    return torch.sqrt(2 * driving_pressure / (air_density * (1 - beta**4)))


def jet_speed_from_airflow(glottal_area, airflow):
    """
    Port of jet_speed.m, 'f' mode.

    Computes jet speed directly from volumetric airflow and glottal area
    (velocity = flow rate / area).

    Args:
        glottal_area: tensor, glottal cross-sectional area (m^2).
        airflow: tensor, volumetric airflow.

    Returns:
        Tensor of jet speed (m/s), broadcast shape of inputs.
    """
    return airflow / glottal_area