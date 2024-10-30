"""
Code which simulates the Izhikevich Neuron Model.
Equations:
    v' = 0.04v^2 + 5v + 140 - u + I
    u' = a.( b.v - u )
    if v = 30 mV -> v = c, u = u + d
"""