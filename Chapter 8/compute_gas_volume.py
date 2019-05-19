gas_const = 8.3144621

def compute_gas_volume(p, t, m):
    m_vol = (m * gas_const * t) / p
    return m_vol

gas_pressure = 100.0
gas_moles = 1.0
gas_temperature = 273.0
gas_volume = 0.0

gas_volume = compute_gas_volume(gas_pressure, gas_temperature, gas_moles)
print('Gas volume:', gas_volume, 'm^3')