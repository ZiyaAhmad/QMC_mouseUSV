import torch

def glottal_area(PCAIA_activity, TA_activity):
    """
    Port of glottal_area.m (mouse constants).

    Args:
        PCAIA_activity: tensor, values in [0, 1]. Posterior cricoarytenoid/
            interarytenoid activation — controls the cartilaginous portion.
            Higher activation -> smaller cartilaginous area.
        TA_activity: tensor, values in [0, 1]. Thyroarytenoid activation —
            controls the membranous portion. Higher activation -> smaller
            membranous area.

    Returns:
        Tensor of total glottal area (m^2), same shape as the (broadcast)
        inputs.
    """
    area_cart_max = 0.375e-6  # m^2, mouse (Mahrt et al. 2016)
    area_memb_max = 0.26e-6   # m^2, mouse (Riede's email, corrected units)

    area_cart = area_cart_max * (1 - PCAIA_activity)
    area_memb = area_memb_max * (1 - TA_activity)

    return area_cart + area_memb