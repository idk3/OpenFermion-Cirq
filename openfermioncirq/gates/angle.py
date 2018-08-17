#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""Angle conversion functions for gates."""

from typing import Union, Optional

import numpy as np

import cirq


def chosen_angle_to_half_turns(
    half_turns: Optional[Union[cirq.value.symbol.Symbol, float]] = None,
        rads: Optional[float] = None,
        degs: Optional[float] = None,
        duration: Optional[float] = None,
        default: float = 1.0,
) -> Union[cirq.value.symbol.Symbol, float]:
    """Returns a half_turns value based on the given arguments.

    At most one of half_turns, rads, degs, or duration must be specified. If
    none are specified, the output defaults to half_turns=1.

    Args:
        half_turns: The number of half turns to rotate by.
        rads: The number of radians to rotate by.
        degs: The number of degrees to rotate by.
        duration: The exponent as a duration of time.
        default: The half turns angle to use if nothing else is specified.

    Returns:
        A number of half turns.
    """

    if len([1 for e in [half_turns, rads, degs, duration]
            if e is not None]) > 1:
        raise ValueError('Redundant angle specification. '
                         'Use ONE of half_turns, rads, degs, or duration.')

    if duration is not None:
        return 2 * duration / np.pi

    return cirq.value.chosen_angle_to_half_turns(
        half_turns=half_turns, rads=rads, degs=degs, default=default)
