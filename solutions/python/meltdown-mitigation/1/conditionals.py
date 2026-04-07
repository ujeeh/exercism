"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    # checking parameters to goal to determine criticality
    criticality = False
    if temperature >= 800.00:
        criticality = False
    elif neutrons_emitted <= 500.00:
        criticality = False
    elif temperature * neutrons_emitted >= 500000.00:
        criticality = False
    else:
        criticality = True
    # return criticality value
    return criticality




def reactor_efficiency(voltage, current, theoretical_max_power):
    # find generated power
    generated_power = voltage * current
    # find the efficiency
    percentage = generated_power/theoretical_max_power
    efficiency = 'black'
    # compare efficiencies
    if percentage >= 0.8:
        efficiency = 'green'
    elif 0.6 <= percentage < 0.8:
        efficiency = 'orange'
    elif 0.3 <= percentage < 0.6:
        efficiency = 'red'
    else:
        efficiency = 'black'
    return efficiency
    


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    failsafe = 'NORMAL'
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').


    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """
    comaprison = temperature * neutrons_produced_per_second
    if comaprison < 0.9 * threshold:
        failsafe = 'LOW'
    elif 0.9 * threshold <= comaprison <= 1.1 * threshold:
        failsafe = 'NORMAL'
    else:
        failsafe = 'DANGER'
    return failsafe
