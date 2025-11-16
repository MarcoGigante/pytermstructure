"""
PyTermStructure Help System
Comprehensive built-in documentation
"""

def show_help(topic=None):
    """Display help for PyTermStructure."""
    
    if topic is None:
        _show_general_help()
    elif topic.lower() == "bootstrap":
        _show_bootstrap_help()
    elif topic.lower() == "pseudoinverse":
        _show_pseudoinverse_help()
    elif topic.lower() == "lorimier":
        _show_lorimier_help()
    elif topic.lower() == "pca":
        _show_pca_help()
    elif topic.lower() == "nelson-siegel":
        _show_nelson_siegel_help()
    elif topic.lower() == "quickstart":
        _show_quickstart()
    elif topic.lower() == "examples":
        _show_examples()
    elif topic.lower() == "accuracy":
        _show_accuracy()
    else:
        print(f"Unknown topic: {topic}")
        print("Available topics: bootstrap, pseudoinverse, lorimier, pca, nelson-siegel, quickstart, examples, accuracy")


def _show_general_help():
    """Show general help."""
    print("""
PyTermStructure v0.0.1
==================================================
Educational library for interest rate term structure

Methods:
  - Bootstrap: Sequential construction (LIBOR → Futures → Swaps)
  - Pseudoinverse: Smooth + exact pricing
  - Lorimier: Smoothing splines with parameter α
  - PCA: Principal component analysis
  - Nelson-Siegel: Parametric curve fitting

Accuracy: ±15 bps (educational purposes)

Usage:
  import pytermstructure as pts
  pts.help("bootstrap")      # Method-specific help
  pts.help("quickstart")     # Quick start guide
  pts.help("examples")       # Example scripts
  pts.help("accuracy")       # Accuracy information

Author: Marco Gigante
License: GNU GPLv3
Inspired by: Damir Filipović'"'"'s "Interest Rate Models" (EPFL)
GitHub: https://github.com/MarcoGigante/pytermstructure
    """)


def _show_bootstrap_help():
    """Show bootstrap method help."""
    print("""
Bootstrap Method
==================================================

Sequential construction from short to long maturities.

Formula:
  LIBOR:   P(0,T) = 1 / (1 + δ*L)
  Futures: P(T1) = P(T0) / (1 + δ*F)
  Swaps:   P(Tn) = (1 - R*Σδ*P) / (1 + R*δ)

Usage:
  from pytermstructure import BootstrapMethod
  from pytermstructure.core import MarketInstrument, InstrumentType
  
  bootstrap = BootstrapMethod(verbose=True)
  
  # Add LIBOR 3M @ 0.15%
  bootstrap.add_instrument(MarketInstrument(
      InstrumentType.LIBOR,
      maturity=0.25,
      quote=0.15
  ))
  
  # Add Swap 2Y @ 0.50%
  bootstrap.add_instrument(MarketInstrument(
      InstrumentType.SWAP,
      maturity=2.0,
      quote=0.50
  ))
  
  # Fit
  curve = bootstrap.fit()
  
  # Get results
  zero_rates = bootstrap.get_zero_rates()
  forward_rates = bootstrap.get_forward_rates()

Accuracy: ±13 bps on 30Y forward rates

Reference: Filipović Chapter 2.1
    """)


def _show_pseudoinverse_help():
    """Show pseudoinverse method help."""
    print("""
Pseudoinverse Method
==================================================

Exact pricing with smooth curves using Moore-Penrose pseudoinverse.

Current Implementation:
  v0.0.1 uses bootstrap as baseline
  Full cash flow matrix implementation planned for v0.1.0

Usage:
  from pytermstructure import PseudoinverseMethod
  
  pseudoinv = PseudoinverseMethod(verbose=True)
  pseudoinv.instruments = bootstrap.instruments
  
  curve = pseudoinv.fit(bootstrap_curve=bootstrap)

Accuracy: ±15 bps (currently same as bootstrap)

Reference: Filipović Chapter 2.2
    """)


def _show_lorimier_help():
    """Show Lorimier method help."""
    print("""
Lorimier Smoothing Splines
==================================================

Smooth forward curves using cubic splines with parameter α.

Formula:
  f(T) = β₀ + Σ βᵢ * hᵢ(T)
  with smoothing parameter α controlling flexibility

Usage:
  import numpy as np
  from pytermstructure import LorimierMethod
  
  # Swiss government bond yields
  maturities = np.array([2, 3, 4, 5, 7, 10, 20, 30])
  yields = np.array([-0.79, -0.73, -0.65, -0.55,
                     -0.33, -0.04, 0.54, 0.73]) / 100
  
  lorimier = LorimierMethod(alpha=0.1, verbose=True)
  curve = lorimier.fit(yields, maturities)
  
  # Interpolate at 6 years
  y_6y = lorimier.get_yield_at(6.0)
  print(f"6Y yield: {y_6y*100:.2f}%")

Parameters:
  α = 0.0: Exact fit (ragged forward curve)
  α = 0.1: Smooth fit (recommended)
  α = 1.0: Very smooth (may lose detail)

Accuracy: ±3 bps on interpolated yields

Reference: Filipović Chapter 2.3
    """)


def _show_pca_help():
    """Show PCA help."""
    print("""
Principal Component Analysis
==================================================

Dimension reduction and risk factor identification.

Typical Results:
  PC1 (Level):     ~90% variance
  PC2 (Slope):     ~8% variance
  PC3 (Curvature): ~2% variance

Usage:
  import numpy as np
  from pytermstructure import PCAAnalysis
  
  # Historical yield changes (T × N matrix)
  yield_changes = np.random.randn(120, 8) * 0.01
  
  pca = PCAAnalysis(verbose=True)
  eigenvalues, eigenvectors, explained = pca.fit(yield_changes)
  
  print(f"Level:     {explained[0]:.1f}%")
  print(f"Slope:     {explained[1]:.1f}%")
  print(f"Curvature: {explained[2]:.1f}%")

Reference: Filipović Chapter 2.4
    """)


def _show_nelson_siegel_help():
    """Show Nelson-Siegel help."""
    print("""
Nelson-Siegel Parametric Model
==================================================

Four-parameter curve fitting.

Formula:
  y(T) = β₀ + β₁*(1-e^(-T/τ))/(T/τ) + β₂*[(1-e^(-T/τ))/(T/τ) - e^(-T/τ)]

Parameters:
  β₀: Long-term level
  β₁: Short-term component
  β₂: Medium-term (hump)
  τ:  Time constant

Usage:
  from pytermstructure import NelsonSiegelMethod
  
  ns = NelsonSiegelMethod()
  maturities = np.array([1, 2, 5, 10, 20, 30])
  
  curve = ns.fit(
      beta0=2.5,  # Long rate
      beta1=-1.5, # Short rate
      beta2=0.5,  # Curvature
      tau=2.0,    # Time constant
      maturities=maturities
  )

Reference: Filipović Chapter 2.3
    """)


def _show_quickstart():
    """Show quick start guide."""
    print("""
Quick Start Guide
==================================================

1. Install:
   pip install pytermstructure

2. Import:
   import pytermstructure as pts
   from pytermstructure.core import MarketInstrument, InstrumentType

3. Create method:
   bootstrap = pts.BootstrapMethod(verbose=True)

4. Add data:
   bootstrap.add_instrument(MarketInstrument(
       InstrumentType.LIBOR, 0.25, 0.15
   ))

5. Fit:
   curve = bootstrap.fit()

6. Results:
   zero_rates = bootstrap.get_zero_rates()

See pts.help("examples") for more examples.
    """)


def _show_examples():
    """Show example scripts."""
    print("""
Example Scripts
==================================================

Location: examples/ directory

1. example_bootstrap.py
   - US market bootstrap
   - LIBOR, Futures, Swaps
   - Run: python examples/example_bootstrap.py

2. example_pseudoinverse.py
   - Pseudoinverse method
   - Smooth curves
   - Run: python examples/example_pseudoinverse.py

3. example_lorimier.py
   - Swiss government bonds
   - Negative rates
   - Run: python examples/example_lorimier.py

4. practical_examples.py
   - All examples
   - Run: python examples/practical_examples.py

GitHub: https://github.com/MarcoGigante/pytermstructure/tree/main/examples
    """)


def _show_accuracy():
    """Show accuracy information."""
    print("""
Accuracy Information
==================================================

Status: Educational Beta (v0.0.1)

Expected Deviations:
  Bootstrap:     ±15 bps on long-term (>10Y) rates
  Lorimier:      ±5 bps on interpolated yields
  Pseudoinverse: ±15 bps (currently uses bootstrap)

Known Limitations:
  - Simplified interpolation in long-term swaps
  - No business day calendar support
  - Limited day-count conventions (ACT/360 only)

Recommendation:
  Use for educational purposes and prototyping.
  For production: QuantLib or FinancePy

See: pts.help("contributing") for how to help improve accuracy
    """)
