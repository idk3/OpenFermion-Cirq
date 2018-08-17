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

import numpy as np
import pytest

from openfermioncirq.gates.angle import chosen_angle_to_half_turns


def test_chosen_angle_to_half_turns():
    assert chosen_angle_to_half_turns() == 1
    assert chosen_angle_to_half_turns(default=0.5) == 0.5
    assert chosen_angle_to_half_turns(half_turns=0.25,
                                      default=0.75) == 0.25
    np.testing.assert_allclose(
        chosen_angle_to_half_turns(rads=np.pi/2),
        0.5,
        atol=1e-8)
    np.testing.assert_allclose(
        chosen_angle_to_half_turns(rads=-np.pi/4),
        -0.25,
        atol=1e-8)
    np.testing.assert_allclose(
        chosen_angle_to_half_turns(duration=3*np.pi/4),
        1.5,
        atol=1e-8)
    np.testing.assert_allclose(
        chosen_angle_to_half_turns(duration=-np.pi/8),
        -0.25,
        atol=1e-8)
    assert chosen_angle_to_half_turns(degs=90) == 0.5
    assert chosen_angle_to_half_turns(degs=1080) == 6.0
    assert chosen_angle_to_half_turns(degs=990) == 5.5

    with pytest.raises(ValueError):
        _ = chosen_angle_to_half_turns(half_turns=0, rads=0)
    with pytest.raises(ValueError):
        _ = chosen_angle_to_half_turns(half_turns=0, degs=0)
    with pytest.raises(ValueError):
        _ = chosen_angle_to_half_turns(degs=0, rads=0)
    with pytest.raises(ValueError):
        _ = chosen_angle_to_half_turns(half_turns=0, rads=0, degs=0)
    with pytest.raises(ValueError):
        _ = chosen_angle_to_half_turns(duration=0, half_turns=0)
    with pytest.raises(ValueError):
        _ = chosen_angle_to_half_turns(degs=0, duration=0)
    with pytest.raises(ValueError):
        _ = chosen_angle_to_half_turns(duration=0, rads=0)
    with pytest.raises(ValueError):
        _ = chosen_angle_to_half_turns(duration=0, degs=0, half_turns=0)
    with pytest.raises(ValueError):
        _ = chosen_angle_to_half_turns(rads=0, duration=0,
                                       degs=0, half_turns=0)
