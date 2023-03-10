"__init__.py"

from typing import Union
from concrete_calculator import (UnitConverter, ConcreteStructureData)
from concrete_calculator import (RoundSlabConcreteCalculator)
from concrete_calculator import (SquareSlabConcreteCalculator)


class Calculator:
    """
    A calculator that can compute the volume of concrete needed for
        a given structure.

    Args:
        None

    Attributes:
        unit_converter (UnitConverter): An object for converting
            units of measurement.
    """

    def __init__(self) -> None:
        self.unit_converter = UnitConverter()

    def _square_calculation(self,
                            *,
                            length: Union[float, int],
                            width: Union[float, int],
                            depth: Union[float, int],
                            units: str = "ft") -> Union[float, int]:
        """
        Calculate the volume of concrete needed for a square structure.

        All method parameter dimensional measuments provided in feet units.

        Args:
            length (Union[float, int]): The length of the square structure.
            width (Union[float, int]): The width of the square structure.
            depth (Union[float, int]): The depth of the square structure.
            units (str): The units of measurement to use for the
                output. Default is "ft".

        Returns:
            str: The volume of concrete needed for the square structure, in
                the specified units.
        """
        calculator_data = ConcreteStructureData(length=length,
                                                width=width,
                                                depth=depth)
        calculator = SquareSlabConcreteCalculator(self.unit_converter)
        volume = calculator.calculate_volume(calculator_data, units=units)

        return volume

    def _round_calculation(self,
                           *,
                           diameter: Union[float, int],
                           depth: Union[float, int],
                           units: str = "ft") -> Union[float, int]:
        """
        Calculate the volume of concrete needed for a round structure.

        All method parameter dimensional measuments provided in feet units.

        Args:
            diameter (Union[float, int]): The diameter of the round structure.
            depth (Union[float, int]): The depth of the round structure.
            units (str): The units of measurement to use for the
                output. Default is "ft".

        Returns:
            str: The volume of concrete needed for the round structure, in
                the specified units.
        """
        calculator_data = ConcreteStructureData(diameter=diameter, depth=depth)
        calculator = RoundSlabConcreteCalculator(self.unit_converter)
        volume = calculator.calculate_volume(calculator_data, units=units)

        return volume

    def square_slab(self,
                    *,
                    length: Union[float, int],
                    width: Union[float, int],
                    depth: Union[float, int],
                    units: str = "ft") -> str:
        """
        Calculate the volume of concrete needed for a square slab.

        All method parameter dimensional measuments provided in feet units.

        Args:
            length (Union[float, int]): The length of the square slab.
            width (Union[float, int]): The width of the square slab.
            depth (Union[float, int]): The depth of the square slab.
            units (str): The units of measurement to use for the
                output. Default is "ft".

        Returns:
            str: The volume of concrete needed for the square slab, in
                the specified units.

        Usage:
        >>> calculate = Calculator()
        >>> square_slab_in_feet = calculate.square_slab(length=10,
        ...  width=5, depth=3)
        >>> assert square_slab_in_feet == '150.0'
        >>>
        >>> square_slab_in_yards = calculate.square_slab(length=10,
        ...  width=5, depth=3, units="yd")
        >>> assert square_slab_in_yards == '5.555555555555555'
        >>>
        >>> square_slab_in_meters = calculate.square_slab(length=10,
        ...  width=5, depth=3, units="m")
        >>> assert square_slab_in_meters == '4.245'
        >>>
        """
        volume = self._square_calculation(length=length,
                                          width=width,
                                          depth=depth,
                                          units=units)

        return str(volume)

    def wall(self,
             *,
             length: Union[float, int],
             thickness: Union[float, int],
             height: Union[float, int],
             units: str = "ft") -> str:
        """
        Calculate the volume of concrete needed for a wall.

        All method parameter dimensional measuments provided in feet units.

        Args:
            length (Union[float, int]): The length of the wall.
            thickness (Union[float, int]): The thickness of the wall.
            height (Union[float, int]): The height of the wall.
            units (str): The units of measurement to use for the
                output. Default is "ft".

        Returns:
            str: The volume of concrete needed for the wall, in
                the specified units.

        Usage:
        >>> calculate = Calculator()
        >>> wall_in_feet = calculate.wall(length=10,
        ...  thickness=5, height=3)
        >>> assert wall_in_feet == '150.0'
        >>>
        >>> wall_in_yards = calculate.wall(length=10,
        ...  thickness=5, height=3, units="yd")
        >>> assert wall_in_yards == '5.555555555555555'
        >>>
        >>> wall_in_meters = calculate.wall(length=10,
        ...  thickness=5, height=3, units="m")
        >>> assert wall_in_meters == '4.245'
        >>>
        """
        volume = self._square_calculation(length=length,
                                          width=thickness,
                                          depth=height,
                                          units=units)

        return str(volume)

    def footer(self,
               *,
               length: Union[float, int],
               width: Union[float, int],
               depth: Union[float, int],
               units: str = "ft") -> str:
        """
        Calculate the volume of concrete needed for a footer.

        All method parameter dimensional measuments provided in feet units.

        Args:
            length (Union[float, int]): The length of the footer.
            width (Union[float, int]): The width of the footer.
            depth (Union[float, int]): The depth of the footer.
            units (str): The units of measurement to use for the
                output. Default is "ft".

        Returns:
            str: The volume of concrete needed for the footer, in
                the specified units.

        Usage:
        >>> calculate = Calculator()
        >>> footer_in_feet = calculate.footer(length=10,
        ...  width=5, depth=3)
        >>> assert footer_in_feet == '150.0'
        >>>
        >>> footer_in_yards = calculate.footer(length=10,
        ...  width=5, depth=3, units="yd")
        >>> assert footer_in_yards == '5.555555555555555'
        >>>
        >>> footer_in_meters = calculate.footer(length=10,
        ...  width=5, depth=3, units="m")
        >>> assert footer_in_meters == '4.245'
        >>>
        """
        volume = self._square_calculation(length=length,
                                          width=width,
                                          depth=depth,
                                          units=units)

        return str(volume)

    def square_column(self,
                      *,
                      length: Union[float, int],
                      width: Union[float, int],
                      height: Union[float, int],
                      units: str = "ft") -> str:
        """
        Calculate the volume of concrete needed for a square column.

        All method parameter dimensional measuments provided in feet units.

        Args:
            length (Union[float, int]): The length of the square column.
            width (Union[float, int]): The width of the square column.
            height (Union[float, int]): The height of the square column.
            units (str): The units of measurement to use for the
                output. Default is "ft".

        Returns:
            str: The volume of concrete needed for the square column, in
                the specified units.

        Usage:
        >>> calculate = Calculator()
        >>> square_column_in_feet = calculate.square_column(length=10,
        ...  width=5, height=3)
        >>> assert square_column_in_feet == '150.0'
        >>>
        >>> square_column_in_yards = calculate.square_column(length=10,
        ...  width=5, height=3, units="yd")
        >>> assert square_column_in_yards == '5.555555555555555'
        >>>
        >>> square_column_in_meters = calculate.square_column(length=10,
        ...  width=5, height=3, units="m")
        >>> assert square_column_in_meters == '4.245'
        >>>
        """
        volume = self._square_calculation(length=length,
                                          width=width,
                                          depth=height,
                                          units=units)

        return str(volume)

    def round_slab(self,
                   *,
                   diameter: Union[float, int],
                   depth: Union[float, int],
                   units: str = "ft") -> str:
        """
        Calculate the volume of concrete needed for a round slab.

        All method parameter dimensional measuments provided in feet units.

        Args:
            diameter (Union[float, int]): The diameter of the round slab.
            depth (Union[float, int]): The depth of the round slab.
            units (str): The units of measurement to use for the
                output. Default is "ft".

        Returns:
            str: The volume of concrete needed for the round slab, in
                the specified units.

        Usage:
            >>> calculate = Calculator()
            >>> round_slab_in_feet = calculate.round_slab(diameter=10,
            ...  depth=5)
            >>> assert round_slab_in_feet == '392.69908169872417'
            >>>
            >>> round_slab_in_yards = calculate.round_slab(diameter=10,
            ...  depth=5, units="yd")
            >>> assert round_slab_in_yards == '14.54441043328608'
            >>>
            >>> round_slab_in_meters = calculate.round_slab(diameter=10,
            ...  depth=5, units="m")
            >>> assert round_slab_in_meters == '11.113384012073894'
            >>>
        """
        volume = self._round_calculation(diameter=diameter,
                                         depth=depth,
                                         units=units)

        return str(volume)

    def round_column(self,
                     *,
                     diameter: Union[float, int],
                     depth: Union[float, int],
                     units: str = "ft") -> str:
        """
        Calculate the volume of concrete needed for a round column.

        All method parameter dimensional measuments provided in feet units.

        Args:
            diameter (Union[float, int]): The diameter of the round column.
            depth (Union[float, int]): The depth of the round column.
            units (str): The units of measurement to use for the
                output. Default is "ft".

        Returns:
            str: The volume of concrete needed for the round column, in
                the specified units.

        Usage:
            >>> calculate = Calculator()
            >>> round_column_in_feet = calculate.round_column(diameter=10,
            ...  depth=5)
            >>> assert round_column_in_feet == '392.69908169872417'
            >>>
            >>> round_column_in_yards = calculate.round_column(diameter=10,
            ...  depth=5, units="yd")
            >>> assert round_column_in_yards == '14.54441043328608'
            >>>
            >>> round_column_in_meters = calculate.round_column(diameter=10,
            ...  depth=5, units="m")
            >>> assert round_column_in_meters == '11.113384012073894'
            >>>
        """
        volume = self._round_calculation(diameter=diameter,
                                         depth=depth,
                                         units=units)

        return str(volume)

    def steps(self,
              *,
              platform_depth: Union[float, int],
              run: Union[float, int],
              rise: Union[float, int],
              width: Union[float, int],
              steps: int,
              units: str = "ft") -> str:
        """
        Calculate the volume of concrete needed for a set of steps.

        All method parameter dimensional measuments provided in feet units.

        Args:
            platform_depth (Union[float, int]): The depth of the platform step.
            run (Union[float, int]): The the run depth of the step.
            rise (Union[float, int]): The rise height of the step.
            width (Union[float, int]): The width of the step.
            steps (int): The number of steps, including the platform step.
            units (str): The units of measurement to use for the
                output. Default is "ft".

        Returns:
            str: The volume of concrete needed for the steps, in
                the specified units.

        Usage:
            >>> calculate = Calculator()
            >>>
            >>> steps_in_feet = calculate.steps(platform_depth=2,
            ...  run=2, rise=2, width=2, steps=14)
            >>> assert steps_in_feet == '840.0'
            >>>
            >>> steps_in_yards = calculate.steps(platform_depth=2,
            ...  run=2, rise=2, width=2, steps=14, units="yd")
            >>> assert steps_in_yards == '31.111111111111107'
            >>>
            >>> steps_in_meters = calculate.steps(platform_depth=2,
            ...  run=2, rise=2, width=2, steps=14, units="m")
            >>> assert steps_in_meters == '23.772'
            >>>
        """
        platform_volume = self._square_calculation(length=platform_depth,
                                                   width=width,
                                                   depth=rise,
                                                   units=units)
        step_volumes: Union[float, int] = 0
        for i in range(1, steps):
            step_volumes += self._square_calculation(length=run,
                                                     width=width,
                                                     depth=rise * i,
                                                     units=units)
        volume = platform_volume * steps + step_volumes

        return str(volume)

    def curbs_and_gutters(self,
                          *,
                          curb_depth: Union[float, int],
                          curb_height: Union[float, int],
                          gutter_width: Union[float, int],
                          flag_thickness: Union[float, int],
                          length: Union[float, int],
                          units: str = "ft") -> str:
        """
        Calculate the volume of concrete needed for curbs and gutters.

        All method parameter dimensional measuments provided in feet units.

        Args:
            curb_depth (Union[float, int]): The depth of the curbs.
            curb_height (Union[float, int]): The height of the curbs.
            gutter_width (Union[float, int]): The width of the gutters.
            flag_thickness (Union[float, int]): The thickness of the flag.
            length (Union[float, int]): Total length of the curbs and gutters.
            units (str): The units of measurement to use for the
                output. Default is "ft".

        Returns:
            str: The volume of concrete needed for the curbs and gutters, in
                the specified units.

        Usage:
        >>> calculate = Calculator()
        >>>
        >>> volume_in_feet = calculate.curbs_and_gutters(curb_depth=6,
        ... curb_height=4, gutter_width=5, flag_thickness=3, length=8)
        >>> assert volume_in_feet == '456.0'
        >>>
        >>> volume_in_yards = calculate.curbs_and_gutters(curb_depth=6,
        ... curb_height=4, gutter_width=5, flag_thickness=3, length=8,
        ... units='yd')
        >>> assert volume_in_yards == '16.888888888888886'
        >>>
        >>> volume_in_meters = calculate.curbs_and_gutters(curb_depth=6,
        ... curb_height=4, gutter_width=5, flag_thickness=3, length=8,
        ... units='m')
        >>> assert volume_in_meters == '12.904799999999998'

        """
        curb_volume = self._square_calculation(length=length,
                                               width=curb_height +
                                               flag_thickness,
                                               depth=curb_depth,
                                               units=units)

        gutter_volume = self._square_calculation(length=length,
                                                 width=gutter_width,
                                                 depth=flag_thickness,
                                                 units=units)
        volume = curb_volume + gutter_volume

        return str(volume)
