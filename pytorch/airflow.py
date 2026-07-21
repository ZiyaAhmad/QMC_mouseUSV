import torch
from pytorch.jet_speed import jet_speed_from_pressure

def airflow(pressure, glottal_area):
    """
    Port of airflow.m (mouse constants).

    Computes volumetric airflow through the glottis using subglottal
    pressure and glottal area, via jet speed and an empirical discharge
    coefficient correction.

    Args:
        pressure: tensor, subglottal pressure (Pa).
        glottal_area: tensor, glottal cross-sectional area (m^2).

    Returns:
        Tensor of volumetric airflow, broadcast shape of inputs.
    """
    tracheal_area = 0.95e-6  # m^2, mouse (extrapolated, Håkansson et al. 2022)
    tracheal_diameter = 2 * torch.sqrt(torch.tensor(tracheal_area) / torch.pi)
    glottal_diameter = 2 * torch.sqrt(glottal_area / torch.pi)

    beta = glottal_diameter / tracheal_diameter

    # reuse the already-validated jet_speed_from_pressure instead of
    # re-deriving the same formula inline (source duplicates it)
    jet_speed = jet_speed_from_pressure(glottal_area, pressure)

    kinematic_viscosity_air = 1.5111e-5  # room temp, 20 C

    Re = jet_speed * tracheal_diameter / kinematic_viscosity_air

    # discharge coefficient (Çengel & Cimbala, Fluid Mechanics 3rd Ed., p.396, orifice meter)
    Cd = 0.5959 + 0.0312 * beta**2.1 - 0.18 * beta**8 + 91.71 * beta**2.5 / (Re**0.75)

    return glottal_area * Cd * jet_speed