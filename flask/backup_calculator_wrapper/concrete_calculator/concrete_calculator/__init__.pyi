from typing import Union, Optional
from dataclasses import dataclass
from abc import ABC, abstractmethod

class ConcreteStructureData:
    diameter: Optional[Union[float, int]]
    depth: Optional[Union[float, int]]
    length: Optional[Union[float, int]]
    width: Optional[Union[float, int]]

    def __init__(self, diameter: Optional[Union[float, int]] = None,
                 depth: Optional[Union[float, int]] = None,
                 length: Optional[Union[float, int]] = None,
                 width: Optional[Union[float, int]] = None) -> None: ...


class ConcreteCalculator(ABC):
    def __init__(self, unit_converter: 'UnitConverter') -> None: ...

    @abstractmethod
    def calculate_volume(self, data: ConcreteStructureData,
                         units: str = 'ft') -> Union[float, int]: ...


class RoundSlabConcreteCalculator(ConcreteCalculator):
    def calculate_volume(self, data: ConcreteStructureData,
                         units: str = 'ft') -> Union[float, int]: ...


class SquareSlabConcreteCalculator(ConcreteCalculator):
    def calculate_volume(self, data: ConcreteStructureData,
                         units: str = 'ft') -> Union[float, int]: ...


class UnitConverter:
    def convert(self, value: Union[float, int],
                units: str) -> Union[float, int]: ...
