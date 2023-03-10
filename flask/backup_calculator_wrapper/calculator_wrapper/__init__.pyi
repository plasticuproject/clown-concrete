"__init__.pyi"

from typing import Union


class Calculator:
    def __init__(self) -> None: ...

    def _square_calculation(self,
                            *,
                            length: Union[float, int],
                            width: Union[float, int],
                            depth: Union[float, int],
                            units: str = "ft") -> Union[float, int]: ...

    def _round_calculation(self,
                           *,
                           diameter: Union[float, int],
                           depth: Union[float, int],
                           units: str = "ft") -> Union[float, int]: ...

    def square_slab(self,
                    *,
                    length: Union[float, int],
                    width: Union[float, int],
                    depth: Union[float, int],
                    units: str = "ft") -> str: ...

    def wall(self,
             *,
             length: Union[float, int],
             thickness: Union[float, int],
             height: Union[float, int],
             units: str = "ft") -> str: ...

    def footer(self,
               *,
               length: Union[float, int],
               width: Union[float, int],
               depth: Union[float, int],
               units: str = "ft") -> str: ...

    def square_column(self,
                      *,
                      length: Union[float, int],
                      width: Union[float, int],
                      height: Union[float, int],
                      units: str = "ft") -> str: ...

    def round_slab(self,
                   *,
                   diameter: Union[float, int],
                   depth: Union[float, int],
                   units: str = "ft") -> str: ...

    def round_column(self,
                     *,
                     diameter: Union[float, int],
                     depth: Union[float, int],
                     units: str = "ft") -> str: ...

    def steps(self,
              *,
              platform_depth: Union[float, int],
              run: Union[float, int],
              rise: Union[float, int],
              width: Union[float, int],
              steps: int,
              units: str = "ft") -> str: ...

    def curbs_and_gutters(self,
                          *,
                          curb_depth: Union[float, int],
                          curb_height: Union[float, int],
                          gutter_width: Union[float, int],
                          flag_thickness: Union[float, int],
                          length: Union[float, int],
                          units: str = "ft") -> str: ...

