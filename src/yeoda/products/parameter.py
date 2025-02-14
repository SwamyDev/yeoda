# Copyright (c) 2020, Vienna University of Technology (TU Wien), Department of
# Geodesy and Geoinformation (GEO).
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# The views and conclusions contained in the software and documentation are
# those of the authors and should not be interpreted as representing official
# policies, either expressed or implied, of the FreeBSD Project.

"""
Main code for creating a TUWGEO parameter data cube.
"""

# import TUWGEO product data cube
from yeoda.products.base import ProductDataCube


class ParameterDataCube(ProductDataCube):
    """
    Data cube defining a TUWGEO parameter product, which has a pre-defined start and end date.

    """

    def __init__(self, start_tdim_name='stime', end_tdim_name='etime', **kwargs):
        """
        Constructor of class `ParameterDataCube`.

        Parameters
        ----------
        start_tdim_name : str, optional
            Temporal dimension name of start time (defaults to 'stime').
        end_tdim_name : str, optional
            Temporal dimension name of end time (defaults to 'etime').
        **kwargs
            Keyworded arguments for `ProductDataCube`.

        """
        dimensions = kwargs.pop('dimensions', [])
        if start_tdim_name not in dimensions:
            dimensions.append(start_tdim_name)
        if end_tdim_name not in dimensions:
            dimensions.append(end_tdim_name)

        super().__init__(dimensions=dimensions, **kwargs)

