"""PyTermStructure - Core Classes"""
from enum import Enum
from dataclasses import dataclass
from typing import Optional

class InstrumentType(Enum):
    LIBOR = "LIBOR"
    FUTURE = "Future"
    SWAP = "Swap"
    BOND = "Bond"

@dataclass
class MarketInstrument:
    instrument_type: InstrumentType
    maturity: float
    quote: float
    name: Optional[str] = None

class TermStructureBase:
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.instruments = []
        self.discount_curve = None
        self.maturities = None
    
    def add_instrument(self, instrument: MarketInstrument):
        self.instruments.append(instrument)
    
    def fit(self):
        raise NotImplementedError
