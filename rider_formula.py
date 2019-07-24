# Jacob Miske

# Functions


def rider_func(W_0, t, Zeff):
    Pbrem = W_0*( 8.511*t**0.5 * (Zeff*(1 + 1.78 * t**1.34) + 2.12*t*(1 + 1.1 * t + t**2 - 1.25*t**2.5)))
    return Pbrem


def w_0_func(e, n_e, m, c, h_bar):
    W_0 = (e**6 * n_e**2 ) / (m * c**2 * h_bar)
    return W_0


def t_func(T_e, m, c):
    t = T_e / (m * c**2)
    return t


# Constants
Z = 3                                   # Protons
T = 200                                 # keV
T_ergs = 3.20435e-7                     # ergs
n_e = 1.6*10**14                        # cm^-3
c = 2.98*10**8 *100                     # cm/s
h_bar = 6.6261*10**-34 *100**2 *1000    # cm^2g/s
e = 1.6022*10**-19                      # Coulombs
m_e = 9.10938*10**-31 *1000             # g

# Declaritives
t_cgs = t_func(T_ergs, m_e, c)

w_0_cgs = w_0_func(e, n_e, m_e, c, h_bar)

rider = rider_func(w_0_cgs, t_cgs, Z)

# Printouts
print(t_cgs)
print(w_0_cgs)
print(rider)