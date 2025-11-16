# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.1] - 2025-11-16

### Added
- Bootstrap method implementation
- Pseudoinverse method (baseline)
- Lorimier smoothing splines method
- PCA analysis
- Nelson-Siegel parametric method
- Built-in help system
- Example scripts
- Sphinx documentation
- Test suite

### Accuracy
- Bootstrap: ±13 bps on 30Y forward rates (Filipović quiz)
- Lorimier: ±3 bps on Swiss government bonds

### Known Limitations
- Pseudoinverse uses bootstrap baseline (full implementation pending)
- Simplified interpolation in long-term swaps
- No business day calendar support yet

## [Unreleased]

### Planned for v0.1.0
- Improve bootstrap accuracy to <10 bps
- Full pseudoinverse with cash flow matrix
- Lorimier optimization with α parameter
- Business day calendars
- More day-count conventions
