import torch

def impingement_length(CT_activity, TA_activity):
    """
    Port of impingement_length.m (mouse constants).

    Args:
        CT_activity: tensor, values in [0, 1]. Cricothyroid activation —
            increases impingement length.
        TA_activity: tensor, values in [0, 1]. Thyroarytenoid activation —
            decreases impingement length (weighted at 0.24x CT's effect).

    Returns:
        Tensor of jet impingement length (m), same shape as the
        (broadcast) inputs.
    """
    length_max = 1.5e-3  # 150% of max, mouse (Mahrt et al. 2016, fig 1F)
    length_min = 0.1e-3  # 50% of min, mouse (Mahrt et al. 2016, fig 1F)

    return length_min + (CT_activity - 0.24 * TA_activity) * (length_max - length_min)