"""PyTermStructure - Helpers"""
import numpy as np

def calculate_forward_rate(discount_factors, maturities, T1, T2):
    from scipy.interpolate import interp1d
    interp = interp1d(maturities, discount_factors, kind='linear')
    P1 = interp(T1)
    P2 = interp(T2)
    return (P1 / P2 - 1) / (T2 - T1)
