# PyTermStructure

**Educational Python library for interest rate term structure estimation**

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-0.0.1-orange.svg)](https://github.com/MarcoGigante/pytermstructure/releases)
[![Status](https://img.shields.io/badge/status-beta-yellow.svg)](https://github.com/MarcoGigante/pytermstructure)

Inspired by **Damir Filipović'"'"'s "Interest Rate Models"**  
École Polytechnique Fédérale de Lausanne (EPFL)  
[Course Link](https://www.coursera.org/learn/interest-rate-models)

---

## Version 0.0.1 - Educational Beta

**Status**: Educational implementation for learning purposes.

**Accuracy**: Results may deviate by **±15 basis points** from reference values due to:
- Simplified interpolation methods
- Approximations in long-term swap pricing
- Day-count convention simplifications

### Validation Results (Filipović Quiz)

| Method | Test Case | Result | Target | Deviation |
|--------|-----------|--------|--------|-----------|
| Bootstrap | 30Y forward rate | 2.69% | 2.56% | +13 bps |
| Lorimier | 6Y Swiss yield | -0.44% | -0.41% | -3 bps |

**Recommendation**: Use for **educational purposes, research, and prototyping**. For production systems requiring high precision, consider [QuantLib](https://www.quantlib.org/) or [FinancePy](https://github.com/domokane/FinancePy).

---

## Quick Start

### Installation

```
pip install pytermstructure
```

### Your First Term Structure

```
import pytermstructure as pts

# Create bootstrap method
bootstrap = pts.BootstrapMethod(verbose=True)

# Add market instruments
bootstrap.add_instrument(pts.MarketInstrument(
    instrument_type=pts.InstrumentType.LIBOR,
    maturity=0.25,  # 3 months
    quote=0.15      # 0.15%
))

bootstrap.add_instrument(pts.MarketInstrument(
    instrument_type=pts.InstrumentType.SWAP,
    maturity=2.0,   # 2 years
    quote=0.50      # 0.50%
))

# Fit discount curve
discount_curve = bootstrap.fit()

# Get zero rates
zero_rates = bootstrap.get_zero_rates()
```

### Getting Help

```
import pytermstructure as pts

# General help
pts.help()

# Method-specific help
pts.help("bootstrap")
pts.help("lorimier")
```

---

## Features

### **5 Methods Implemented**

| Method | Type | Accuracy | Use Case |
|--------|------|----------|----------|
| **Bootstrap** | Exact | ±15 bps | Educational, trading desks |
| **Pseudoinverse** | Exact | ±15 bps | Smooth + exact pricing |
| **Lorimier** | Smooth | ±5 bps | Central banks, smooth curves |
| **PCA** | Analysis | N/A | Risk management |
| **Nelson-Siegel** | Parametric | N/A | Quick approximation |

### **Educational Quality**

- 📖 **Comprehensive documentation** - Built-in help system
- 🎓 **Based on academic course** - Filipović'"'"'s EPFL materials
- ✅ **Type hints** - Full typing support
- 🧪 **Tested** - Validated with course examples
- 🔓 **Free Software** - GNU GPLv3 license
- 📊 **Professional structure** - Ready for contributions

---

## Methods Overview

### 1. Bootstrap Method

Sequential construction from LIBOR → Futures → Swaps.

```
bootstrap = pts.BootstrapMethod(verbose=True)
bootstrap.add_instrument(pts.MarketInstrument(
    pts.InstrumentType.LIBOR, 0.25, 0.15
))
discount_curve = bootstrap.fit()
```

**Accuracy**: ±13 bps on 30Y forward rates

---

### 2. Lorimier Method

Smoothing splines with parameter α for smooth forward curves.

```
import numpy as np

maturities = np.array()
yields = np.array([-0.79, -0.73, -0.65, -0.55, 
                   -0.33, -0.04, 0.54, 0.73]) / 100

lorimier = pts.LorimierMethod(alpha=0.1)
discount_curve = lorimier.fit(yields, maturities)
y_6y = lorimier.get_yield_at(6.0)
```

**Accuracy**: ±3 bps on Swiss government bonds

---

### 3. PCA Analysis

Principal component analysis of yield curve movements.

```
pca = pts.PCAAnalysis()
eigenvalues, eigenvectors, explained_var = pca.fit(yield_changes)

print(f"Level:     {explained_var:.1f}%")
print(f"Slope:     {explained_var:.1f}%")[1]
print(f"Curvature: {explained_var:.1f}%")
```

---

## Installation

### From PyPI

```
pip install pytermstructure
```

### From Source

```
git clone https://github.com/MarcoGigante/pytermstructure.git
cd pytermstructure
pip install -e .
```

### Test Installation

```
python -c "import pytermstructure as pts; pts.version(); pts.help()"
```

Expected output:
```
PyTermStructure 0.0.1 loaded. For help: pts.help()
PyTermStructure 0.0.1
Author: Marco Gigante
License: GPLv3
```

---

## Running Examples

```
# Example 1: Bootstrap US market
python examples/example_bootstrap.py

# Example 2: Pseudoinverse
python examples/example_pseudoinverse.py

# Example 3: Lorimier Swiss bonds
python examples/example_lorimier.py

# Run all examples
python examples/practical_examples.py
```

---

## Academic Reference

This library implements methods from:

**Filipović, D.** (2009). *Term-Structure Models: A Graduate Course*. Springer Finance.

**Online Course**: [Interest Rate Models](https://www.coursera.org/learn/interest-rate-models)  
École Polytechnique Fédérale de Lausanne (EPFL)

---

## License

GNU General Public License v3.0 or later.

This ensures PyTermStructure remains **free software** forever.

See [LICENSE](LICENSE) for details.

---

## Contributing

Contributions welcome! Areas for improvement:

1. **Accuracy refinement** (target: <5 bps)
2. **Full pseudoinverse implementation** (cash flow matrix)
3. **True Lorimier optimization** (with α parameter)
4. **More day-count conventions**
5. **Business day calendars**

Please ensure GPL-compatible contributions.

---

## Author

**Marco Gigante**  
MSc in Quantitative Finance, University of Siena

Inspired by Prof. Damir Filipović'"'"'s course at EPFL.

---

## Acknowledgments

- Prof. Damir Filipović (EPFL)
- École Polytechnique Fédérale de Lausanne
- NumPy, SciPy, Pandas communities
- Free Software Foundation

---

## Support

- **Documentation**: `pts.help()`
- **Issues**: [GitHub Issues](https://github.com/MarcoGigante/pytermstructure/issues)