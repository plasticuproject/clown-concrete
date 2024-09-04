"__init__.py"
from __future__ import annotations
from dataclasses import dataclass
from math import pi
from abc import ABC, abstractmethod
# pylint: disable=too-few-public-methods


@dataclass
class ConcreteStructureData:
    """
    A data class for containing concrete slab measurements in feet.
    """
    diameter: float | int | None = None
    depth: float | int | None = None
    length: float | int | None = None
    width: float | int | None = None


class ConcreteCalculator(ABC):
    """
    A base class for concrete calculators.

    Concrete calculators are used to calculate the volume of concrete needed
    for different types of structures.
    """

    def __init__(self, unit_converter: "UnitConverter") -> None:
        """
        Initialize a new concrete calculator.

        Args:
            unit_converter (UnitConverter): A unit converter used to convert
                between different units of measurement.
        """
        self.unit_converter = unit_converter

    @abstractmethod
    def calculate_volume(self,
                         data: ConcreteStructureData,
                         units: str = "ft") -> float | int:
        """
        Calculate the volume of concrete needed for a structure.

        Args:
            data (ConcreteStructureData): Data class containing values
                needed to calculate the volume.
            units (str): The desired units of measurement for the volume.

        Returns:
            Union[float, int]: The volume of concrete needed.
        """
        raise NotImplementedError()


class RoundSlabConcreteCalculator(ConcreteCalculator):
    """
    A concrete calculator for round slabs.

    Round slabs are circular structures, such as the base of a silo or a
    swimming pool.
    """

    def calculate_volume(self,
                         data: ConcreteStructureData,
                         units: str = "ft") -> float | int:
        """
        Calculate the volume of concrete needed for a round slab.

        Args:
            data (ConcreteStructureData(diameter = Union[float, int],
                                        depth = Union[float, int])):
                Data class containing the diameter and depth of the
                slab in feet.
            units (str): The desired units of measurement for the volume.

        Returns:
            Union[float, int]: The volume of concrete needed.

        Usage:
        >>> unit_converter = UnitConverter()
        >>>
        >>> round_slab_data = ConcreteStructureData(diameter=10,
        ...  depth=3)
        >>>
        >>> calculator = RoundSlabConcreteCalculator(unit_converter)
        >>>
        >>> volume_in_feet = calculator.calculate_volume(round_slab_data)
        >>> assert volume_in_feet == 235.61944901923448
        >>>
        >>> volume_in_yards = calculator.calculate_volume(round_slab_data,
        ... units="yd")
        >>> assert volume_in_yards == 8.726646259971647
        >>>
        >>> volume_in_meters = calculator.calculate_volume(round_slab_data,
        ... units="m")
        >>> assert volume_in_meters == 6.668030407244336
        >>>
        """
        if data.diameter is None or data.depth is None:
            raise ValueError("'diameter' and 'depth' must be set in the."
                             "provided ConcreteStructureData data class.")
        radius = data.diameter / 2
        area = pi * radius**2
        volume = data.depth * area

        return self.unit_converter.convert(volume, units)


class SquareSlabConcreteCalculator(ConcreteCalculator):
    """
    A concrete calculator for square slabs.

    Square slabs are structures with a rectangular shape, such as a patio or a
    sidewalk.
    """

    def calculate_volume(self,
                         data: ConcreteStructureData,
                         units: str = "ft") -> float | int:
        """
        Calculate the volume of concrete needed for a square slab.

        Args:
            data (ConcreteStructureData(width = Union[float, int],
                                        length = Union[float, int],
                                        depth = Union[float, int])):
                Data class containing the width, length, and depth of the
                slab in feet.
            units (str): The desired units of measurement for the volume.

        Returns:
            Union[float, int]: The volume of concrete needed.

        Usage:
            >>> unit_converter = UnitConverter()
            >>>
            >>> square_slab_data = ConcreteStructureData(width=5,
            ...  length = 10, depth=3)
            >>>
            >>> calculator = SquareSlabConcreteCalculator(unit_converter)
            >>>
            >>> volume_in_feet = calculator.calculate_volume(square_slab_data)
            >>> assert volume_in_feet == 150.0
            >>>
            >>> volume_in_yards = calculator.calculate_volume(square_slab_data,
            ...  units="yd")
            >>> assert volume_in_yards == 5.555555555555555
            >>>
            >>> volume_in_meters = calculator.calculate_volume(
            ...  square_slab_data, units="m")
            >>> assert volume_in_meters == 4.245
            >>>
        """
        if data.width is None or data.length is None or data.depth is None:
            raise ValueError("'width', 'length', and 'depth' must be set in "
                             "the provided ConcreteStructureData data class.")
        volume = data.width * data.length * data.depth

        return self.unit_converter.convert(volume, units)


class UnitConverter:
    """
    A class for converting between different units of measurement.
    """

    UNIT_CONVERSION = {
        "ft": 1.0,
        "yd": 1 / 27,
        "m": 0.0283,
    }

    def convert(self, value: float | int, units: str) -> float | int:
        """
        Convert a value from one unit of measurement to another.

        Args:
            value (Union[float, int]): The value to convert.
            units (str): The current units of measurement.

        Returns:
            Union[float, int]: The converted value.

        Usage:
        >>> unit_converter = UnitConverter()
        >>> unit_to_feet = unit_converter.convert(20, "ft")
        >>> assert unit_to_feet == 20.0
        >>>
        >>> unit_to_yards = unit_converter.convert(20, "yd")
        >>> assert unit_to_yards == 0.7407407407407407
        >>>
        >>> unit_to_meters = unit_converter.convert(20, "m")
        >>> assert unit_to_meters == 0.566
        >>>
        """
        try:
            conversion_factor = self.UNIT_CONVERSION[units]
        except KeyError as exc:
            raise ValueError("Invalid unit") from exc
        return value * conversion_factor
