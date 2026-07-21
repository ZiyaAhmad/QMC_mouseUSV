import torch

def USVfreq(jet_speed, impingement_length):
    """
    Port of USVfreq.m (mouse constants).

    Computes the frequency of ultrasonic vocalizations (USVs) based on
    jet speed and impingement length, using a formula derived from
    fluid dynamics principles.

    Args:
        jet_speed: tensor, speed of the jet (m/s).
        impingement_length: tensor, length of the impingement (m).

    Returns:
        Tensor of USV frequencies, broadcast shape of inputs.
    """
    return jet_speed / impingement_length