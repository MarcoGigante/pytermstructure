# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Enhanced Lorimier method with optimization
- Full pseudoinverse with cash flow matrix
- Business day calendars
- Additional day-count conventions

## [0.1.0] - 2025-11-17

### Added
- Exact calendar date support for all instruments
- ACT/360 day-count convention implementation
- Automatic curve densification with interpolated swap rates
- Three-phase bootstrap algorithm (market → densify → long swaps)
- Enhanced `MarketInstrument` with `maturity_date` parameter
- `_get_exact_swap_schedule()` method for precise swap payment dates
- Accuracy information in built-in help system (`pts.help("accuracy")`)

### Changed
- Bootstrap method now uses exact dates instead of year fractions
- Improved bootstrap accuracy from ~13 bps to <1 bps on benchmark data
- Enhanced documentation with v0.1.0 improvements
- Updated help system with new accuracy results

### Fixed
- 33 bps error on 30Y discount factors (now 0.5 bps)
- Long swap pricing now uses densified curve for accuracy
- `helpers.py` indentation and formatting

### Removed
- Unused dependencies: `pandas`, `openpyxl`

### Dependencies
- Added: `python-dateutil>=2.8.0` for date handling

### Accuracy Improvements
- Bootstrap 30Y forward rate: 0.00 bps deviation (target: 2.56%)
- Bootstrap 30Y discount factor: 0.50 bps deviation (target: 0.483194)
- Lorimier 6Y yield: 3.0 bps deviation (target: -0.41%)
- Overall improvement: ~13 bps → <1 bps (70x better)

## [0.0.1] - 2025-11-16

### Added
- Bootstrap method implementation
- Pseudoinverse method (uses bootstrap baseline)
- Lorimier smoothing splines method
- PCA analysis
- Nelson-Siegel parametric method
- Built-in help system with comprehensive documentation
- Example scripts for all methods
- Sphinx documentation structure
- Test suite with academic benchmark validation

### Accuracy
- Bootstrap: ±13 bps on 30Y forward rates
- Lorimier: ±3 bps on Swiss government bonds

### Known Limitations
- Pseudoinverse uses bootstrap baseline (full implementation pending)
- Simplified interpolation in long-term swaps
- No business day calendar support
- Year fractions only (no exact date support)

[Unreleased]: https://github.com/MarcoGigante/pytermstructure/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/MarcoGigante/pytermstructure/compare/v0.0.1...v0.1.0
[0.0.1]: https://github.com/MarcoGigante/pytermstructure/releases/tag/v0.0.1)
