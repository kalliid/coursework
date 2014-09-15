# Gotran generated code for the  "hodgkin_huxley_squid_axon_1952" model
from __future__ import division

def init_state_values(**values):
    """
    Initialize state values
    """
    # Imports
    import numpy as np
    from modelparameters.utils import Range

    # Init values
    # m=0.05, h=0.6, n=0.325, V=-75
    init_values = np.array([0.05, 0.6, 0.325, -75], dtype=np.float_)

    # State indices and limit checker
    state_ind = dict([("m",(0, Range())), ("h",(1, Range())), ("n",(2,\
        Range())), ("V",(3, Range()))])

    for state_name, value in values.items():
        if state_name not in state_ind:
            raise ValueError("{0} is not a state.".format(state_name))
        ind, range = state_ind[state_name]
        if value not in range:
            raise ValueError("While setting '{0}' {1}".format(state_name,\
                range.format_not_in(value)))

        # Assign value
        init_values[ind] = value

    return init_values

def init_parameter_values(**values):
    """
    Initialize parameter values
    """
    # Imports
    import numpy as np
    from modelparameters.utils import Range

    # Param values
    # g_Na=120, g_K=36, g_L=0.3, Cm=1, E_R=-75
    init_values = np.array([120, 36, 0.3, 1, -75], dtype=np.float_)

    # Parameter indices and limit checker
    param_ind = dict([("g_Na", (0, Range())), ("g_K", (1, Range())), ("g_L",\
        (2, Range())), ("Cm", (3, Range())), ("E_R", (4, Range()))])

    for param_name, value in values.items():
        if param_name not in param_ind:
            raise ValueError("{0} is not a parameter.".format(param_name))
        ind, range = param_ind[param_name]
        if value not in range:
            raise ValueError("While setting '{0}' {1}".format(param_name,\
                range.format_not_in(value)))

        # Assign value
        init_values[ind] = value

    return init_values

def state_indices(*states):
    """
    State indices
    """
    state_inds = dict([("m", 0), ("h", 1), ("n", 2), ("V", 3)])

    indices = []
    for state in states:
        if state not in state_inds:
            raise ValueError("Unknown state: '{0}'".format(state))
        indices.append(state_inds[state])
    if len(indices)>1:
        return indices
    else:
        return indices[0]

def parameter_indices(*params):
    """
    Parameter indices
    """
    param_inds = dict([("g_Na", 0), ("g_K", 1), ("g_L", 2), ("Cm", 3),\
        ("E_R", 4)])

    indices = []
    for param in params:
        if param not in param_inds:
            raise ValueError("Unknown param: '{0}'".format(param))
        indices.append(param_inds[param])
    if len(indices)>1:
        return indices
    else:
        return indices[0]

def monitor_indices(*monitored):
    """
    Monitor indices
    """
    monitor_inds = dict([("E_Na", 0), ("i_Na", 1), ("alpha_m", 2), ("beta_m",\
        3), ("alpha_h", 4), ("beta_h", 5), ("E_K", 6), ("i_K", 7),\
        ("alpha_n", 8), ("beta_n", 9), ("E_L", 10), ("i_L", 11), ("i_Stim",\
        12), ("dm_dt", 13), ("dh_dt", 14), ("dn_dt", 15), ("dV_dt", 16)])

    indices = []
    for monitor in monitored:
        if monitor not in monitor_inds:
            raise ValueError("Unknown monitored: '{0}'".format(monitor))
        indices.append(monitor_inds[monitor])
    if len(indices)>1:
        return indices
    else:
        return indices[0]

def rhs(states, t, parameters, values=None):
    """
    Compute the right hand side of the hodgkin_huxley_squid_axon_1952 ODE
    """
    # Imports
    import numpy as np
    import math

    # Assign states
    assert(len(states) == 4)
    m, h, n, V = states

    # Assign parameters
    assert(len(parameters) == 5)
    g_Na, g_K, g_L, Cm, E_R = parameters

    # Init return args
    if values is None:
        values = np.zeros((4,), dtype=np.float_)
    else:
        assert isinstance(values, np.ndarray) and values.shape == (4,)

    # Expressions for the Sodium channel component
    E_Na = 115 + E_R
    i_Na = g_Na*(m*m*m)*(V - E_Na)*h

    # Expressions for the m gate component
    alpha_m = (-5.0 - 0.1*V)/(-1 + math.exp(-5 - V/10))
    beta_m = 4*math.exp(-25/6 - V/18)
    values[0] = (1 - m)*alpha_m - beta_m*m

    # Expressions for the h gate component
    alpha_h = 0.07*math.exp(-15/4 - V/20)
    beta_h = 1.0/(1 + math.exp(-9/2 - V/10))
    values[1] = -beta_h*h + (1 - h)*alpha_h

    # Expressions for the Potassium channel component
    E_K = -12 + E_R
    i_K = g_K*math.pow(n, 4)*(-E_K + V)

    # Expressions for the n gate component
    alpha_n = (-0.65 - 0.01*V)/(-1 + math.exp(-13/2 - V/10))
    beta_n = 0.125*math.exp(15/16 + V/80)
    values[2] = -beta_n*n + (1 - n)*alpha_n

    # Expressions for the Leakage current component
    E_L = 10.613 + E_R
    i_L = g_L*(V - E_L)

    # Expressions for the Membrane component
    i_Stim = (20 if (t <= 10.5) and (t >= 10) else 0)
    values[3] = (-i_L - i_K + i_Stim - i_Na)/Cm

    # Return results
    return values

def monitor(states, t, parameters, monitored=None):
    """
    Computes monitored expressions of the hodgkin_huxley_squid_axon_1952 ODE
    """
    # Imports
    import numpy as np
    import math

    # Assign states
    assert(len(states) == 4)
    m, h, n, V = states

    # Assign parameters
    assert(len(parameters) == 5)
    g_Na, g_K, g_L, Cm, E_R = parameters

    # Init return args
    if monitored is None:
        monitored = np.zeros((17,), dtype=np.float_)
    else:
        assert isinstance(monitored, np.ndarray) and monitored.shape == (17,)

    # Expressions for the Sodium channel component
    monitored[0] = 115 + E_R
    monitored[1] = g_Na*(m*m*m)*(V - monitored[0])*h

    # Expressions for the m gate component
    monitored[2] = (-5.0 - 0.1*V)/(-1 + math.exp(-5 - V/10))
    monitored[3] = 4*math.exp(-25/6 - V/18)
    monitored[13] = (1 - m)*monitored[2] - m*monitored[3]

    # Expressions for the h gate component
    monitored[4] = 0.07*math.exp(-15/4 - V/20)
    monitored[5] = 1.0/(1 + math.exp(-9/2 - V/10))
    monitored[14] = -h*monitored[5] + (1 - h)*monitored[4]

    # Expressions for the Potassium channel component
    monitored[6] = -12 + E_R
    monitored[7] = g_K*math.pow(n, 4)*(V - monitored[6])

    # Expressions for the n gate component
    monitored[8] = (-0.65 - 0.01*V)/(-1 + math.exp(-13/2 - V/10))
    monitored[9] = 0.125*math.exp(15/16 + V/80)
    monitored[15] = -monitored[9]*n + (1 - n)*monitored[8]

    # Expressions for the Leakage current component
    monitored[10] = 10.613 + E_R
    monitored[11] = g_L*(V - monitored[10])

    # Expressions for the Membrane component
    monitored[12] = (20 if (t <= 10.5) and (t >= 10) else 0)
    monitored[16] = (-monitored[7] - monitored[11] - monitored[1] +\
        monitored[12])/Cm

    # Return results
    return monitored

def forward_rush_larsen(states, t, dt, parameters):
    """
    Compute a forward step using the rush larsen algorithm to the\
        hodgkin_huxley_squid_axon_1952 ODE
    """
    # Imports
    import numpy as np
    import math

    # Assign states
    assert(len(states) == 4)
    m, h, n, V = states

    # Assign parameters
    assert(len(parameters) == 5)
    g_Na, g_K, g_L, Cm, E_R = parameters

    # Expressions for the Sodium channel component
    E_Na = 115 + E_R
    i_Na = g_Na*(m*m*m)*(V - E_Na)*h

    # Expressions for the m gate component
    alpha_m = (-5.0 - 0.1*V)/(-1 + math.exp(-5 - V/10))
    beta_m = 4*math.exp(-25/6 - V/18)
    dm_dt = (1 - m)*alpha_m - beta_m*m
    dm_dt_linearized = -beta_m - alpha_m
    states[0] = ((-1.0 +\
        math.exp(dt*dm_dt_linearized))*dm_dt/dm_dt_linearized if\
        math.fabs(dm_dt_linearized) > 1e-08 else dt*dm_dt) + m

    # Expressions for the h gate component
    alpha_h = 0.07*math.exp(-15/4 - V/20)
    beta_h = 1.0/(1 + math.exp(-9/2 - V/10))
    dh_dt = -beta_h*h + (1 - h)*alpha_h
    dh_dt_linearized = -beta_h - alpha_h
    states[1] = h + ((-1.0 +\
        math.exp(dt*dh_dt_linearized))*dh_dt/dh_dt_linearized if\
        math.fabs(dh_dt_linearized) > 1e-08 else dt*dh_dt)

    # Expressions for the Potassium channel component
    E_K = -12 + E_R
    i_K = g_K*math.pow(n, 4)*(-E_K + V)

    # Expressions for the n gate component
    alpha_n = (-0.65 - 0.01*V)/(-1 + math.exp(-13/2 - V/10))
    beta_n = 0.125*math.exp(15/16 + V/80)
    dn_dt = -beta_n*n + (1 - n)*alpha_n
    dn_dt_linearized = -alpha_n - beta_n
    states[2] = ((-1.0 +\
        math.exp(dt*dn_dt_linearized))*dn_dt/dn_dt_linearized if\
        math.fabs(dn_dt_linearized) > 1e-08 else dt*dn_dt) + n

    # Expressions for the Leakage current component
    E_L = 10.613 + E_R
    i_L = g_L*(V - E_L)

    # Expressions for the Membrane component
    i_Stim = (20 if (t <= 10.5) and (t >= 10) else 0)
    dV_dt = (-i_L - i_K + i_Stim - i_Na)/Cm
    states[3] = V + dt*dV_dt

    # Return results
    return states
