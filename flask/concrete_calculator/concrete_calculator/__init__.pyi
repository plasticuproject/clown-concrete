"""__init__.pyi"""
from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class ConcreteStructureData:
    diameter: float | int | None
    depth: float | int | None
    length: float | int | None
    width: float | int | None

    def __init__(self,
                 diameter: float | int | None = None,
                 depth: float | int | None = None,
                 length: float | int | None = None,
                 width: float | int | None = None) -> None:
        ...


class ConcreteCalculator(ABC):

    def __init__(self, unit_converter: "UnitConverter") -> None:
        ...

    @abstractmethod
    def calculate_volume(self,
                         data: ConcreteStructureData,
                         units: str = "ft") -> float | int:
        ...


class RoundSlabConcreteCalculator(ConcreteCalculator):

    def calculate_volume(self,
                         data: ConcreteStructureData,
                         units: str = "ft") -> float | int:
        ...


class SquareSlabConcreteCalculator(ConcreteCalculator):

    def calculate_volume(self,
                         data: ConcreteStructureData,
                         units: str = "ft") -> float | int:
        ...


class UnitConverter:

    def convert(self, value: float | int, units: str) -> float | int:
        ...
