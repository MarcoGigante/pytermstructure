PyTermStructure Documentation
==============================

**Educational Python library for interest rate term structure estimation**

Version: 0.0.1 (Beta)

By **Marco Gigante** | Inspired by Damir Filipović's "Interest Rate Models" (EPFL)

.. note::
   This is an **educational implementation** with ±15 basis points accuracy.
   See :ref:`accuracy-section` for details.

.. image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0
   :alt: License: GPL v3

.. image:: https://img.shields.io/badge/python-3.8+-blue.svg
   :target: https://www.python.org/downloads/
   :alt: Python 3.8+

Quick Start
-----------

Installation
~~~~~~~~~~~~

.. code-block:: bash

   pip install pytermstructure

First Example
~~~~~~~~~~~~~

.. code-block:: python

   import pytermstructure as pts

   # Create bootstrap method
   bootstrap = pts.BootstrapMethod(verbose=True)

   # Add LIBOR instrument
   bootstrap.add_instrument(pts.MarketInstrument(
       instrument_type=pts.InstrumentType.LIBOR,
       maturity=0.25,  # 3 months
       quote=0.15      # 0.15%
   ))

   # Add swap instrument
   bootstrap.add_instrument(pts.MarketInstrument(
       instrument_type=pts.InstrumentType.SWAP,
       maturity=2.0,   # 2 years
       quote=0.50      # 0.50%
   ))

   # Fit discount curve
   discount_curve = bootstrap.fit()
   print(f"Discount factors: {discount_curve}")

   # Get zero rates
   zero_rates = bootstrap.get_zero_rates()
   print(f"Zero rates: {zero_rates}")

.. _accuracy-section:

Accuracy & Validation
---------------------

**Status**: Educational Beta (v0.0.1)

Test Results
~~~~~~~~~~~~

Validation using Filipović'"'"'s course quiz examples:

.. list-table::
   :header-rows: 1
   :widths: 20 20 15 15 15

   * - Method
     - Test Case
     - Result
     - Target
     - Deviation
   * - Bootstrap
     - 30Y forward rate
     - 2.69%
     - 2.56%
     - +13 bps
   * - Lorimier
     - 6Y Swiss yield
     - -0.44%
     - -0.41%
     - -3 bps

Expected Deviations
~~~~~~~~~~~~~~~~~~~

- **Bootstrap method**: ±15 bps on long-term (>10Y) forward rates
- **Lorimier method**: ±5 bps on interpolated yields
- **Pseudoinverse**: ±15 bps (currently uses bootstrap baseline)

**Recommendation**: Use for educational purposes, research, and prototyping.
For production systems, consider `QuantLib <https://www.quantlib.org/>`_ or 
`FinancePy <https://github.com/domokane/FinancePy>`_.

Methods
-------

Bootstrap Method
~~~~~~~~~~~~~~~~

Classic sequential construction from LIBOR → Futures → Swaps.

**Example**:

.. code-block:: python

   from pytermstructure import BootstrapMethod
   from pytermstructure.core import MarketInstrument, InstrumentType

   bootstrap = BootstrapMethod(verbose=True)
   
   # LIBOR 3M @ 0.15%
   bootstrap.add_instrument(MarketInstrument(
       InstrumentType.LIBOR, 0.25, 0.15
   ))
   
   # Future @ 99.68
   bootstrap.add_instrument(MarketInstrument(
       InstrumentType.FUTURE, 1.0, 0.32  # 100 - 99.68
   ))
   
   # Swap 2Y @ 0.50%
   bootstrap.add_instrument(MarketInstrument(
       InstrumentType.SWAP, 2.0, 0.50
   ))
   
   curve = bootstrap.fit()

**Expected Output**:

.. code-block:: text

   Bootstrap: 3 instruments
   P(0, 0.25Y) = 0.999625
   P(0, 1.00Y) = 0.996800
   P(0, 2.00Y) = 0.990099

Lorimier Method
~~~~~~~~~~~~~~~

Smoothing splines for smooth forward curves.

**Example**:

.. code-block:: python

   import numpy as np
   from pytermstructure import LorimierMethod

   # Swiss government bond yields (July 2015)
   maturities = np.array([2, 3, 4, 5, 7, 10, 20, 30])
   yields = np.array([-0.79, -0.73, -0.65, -0.55, 
                      -0.33, -0.04, 0.54, 0.73]) / 100

   lorimier = LorimierMethod(alpha=0.1, verbose=True)
   curve = lorimier.fit(yields, maturities)
   
   # Interpolate at 6 years
   y_6y = lorimier.get_yield_at(6.0)
   print(f"6Y yield: {y_6y*100:.2f}%")  # Expected: ~-0.44%

PCA Analysis
~~~~~~~~~~~~

Principal component analysis of yield curve movements.

.. code-block:: python

   import numpy as np
   from pytermstructure import PCAAnalysis

   # Historical yield changes (100 days × 5 maturities)
   yield_changes = np.random.randn(100, 5) * 0.01

   pca = PCAAnalysis(verbose=True)
   eigenvalues, eigenvectors, explained_var = pca.fit(yield_changes)

   print(f"Level (PC1):     {explained_var[0]:.1f}%")
   print(f"Slope (PC2):     {explained_var[1]:.1f}%")
   print(f"Curvature (PC3): {explained_var[2]:.1f}%")

Built-in Help System
--------------------

.. code-block:: python

   import pytermstructure as pts

   pts.help()                  # General help
   pts.help("bootstrap")       # Bootstrap method
   pts.help("lorimier")        # Lorimier method
   pts.help("quickstart")      # Quick start guide

Common Issues
-------------

Import Error
~~~~~~~~~~~~

If you get ``ModuleNotFoundError: No module named '"'"'pytermstructure'"'"'``:

.. code-block:: bash

   pip install -e .  # Development mode
   # or
   pip install pytermstructure  # From PyPI

Accuracy Concerns
~~~~~~~~~~~~~~~~~

If results deviate >15 bps from expected values:

1. Check input data format
2. Verify day-count convention (ACT/360 assumed)
3. Review instrument types (LIBOR, Futures, Swaps)
4. See :ref:`accuracy-section` for known limitations

API Reference
-------------

Core Classes
~~~~~~~~~~~~

.. autoclass:: pytermstructure.core.MarketInstrument
   :members:

.. autoclass:: pytermstructure.core.InstrumentType
   :members:

Methods
~~~~~~~

.. autoclass:: pytermstructure.methods.BootstrapMethod
   :members:

.. autoclass:: pytermstructure.methods.LorimierMethod
   :members:

.. autoclass:: pytermstructure.methods.PCAAnalysis
   :members:

Academic Reference
------------------

This library implements methods from:

**Filipović, D.** (2009). *Term-Structure Models: A Graduate Course*. Springer Finance.

**Online Course**: `Interest Rate Models <https://www.coursera.org/learn/interest-rate-models>`_

École Polytechnique Fédérale de Lausanne (EPFL)

Contributing
------------

Contributions welcome! Priority areas:

1. **Accuracy improvement** (target: <5 bps)
2. **Full pseudoinverse** with proper cash flow matrix
3. **True Lorimier optimization** with α parameter
4. **Day-count conventions** (30/360, ACT/365, etc.)
5. **Business day calendars**

See `CONTRIBUTING.md <https://github.com/MarcoGigante/pytermstructure/blob/main/CONTRIBUTING.md>`_.

License
-------

GNU General Public License v3.0 or later.

This ensures PyTermStructure remains **free software** forever.

See `LICENSE <https://github.com/MarcoGigante/pytermstructure/blob/main/LICENSE>`_ for details.

Links
-----

* **GitHub**: https://github.com/MarcoGigante/pytermstructure
* **PyPI**: https://pypi.org/project/pytermstructure/
* **Issues**: https://github.com/MarcoGigante/pytermstructure/issues
* **Read the Docs**: https://pytermstructure.readthedocs.io

Acknowledgments
---------------

- Prof. Damir Filipović (EPFL)
- École Polytechnique Fédérale de Lausanne
- NumPy, SciPy communities
- Free Software Foundation

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   installation
   quickstart
   examples
   api

.. toctree::
   :maxdepth: 1
   :caption: Development

   contributing
   changelog

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
