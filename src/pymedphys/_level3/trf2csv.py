# Copyright (C) 2018 Cancer Care Associates

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version (the "AGPL-3.0+").

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License and the additional terms for more
# details.

# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# ADDITIONAL TERMS are also included as allowed by Section 7 of the GNU
# Affero General Public License. These additional terms are Sections 1, 5,
# 6, 7, 8, and 9 from the Apache License, Version 2.0 (the "Apache-2.0")
# where all references to the definition "License" are instead defined to
# mean the AGPL-3.0+.

# You should have received a copy of the Apache-2.0 along with this
# program. If not, see <http://www.apache.org/licenses/LICENSE-2.0>.


"""Converts a trf file into a csv file.
"""


import sys
import os
from glob import glob

from .._level2.trfdecode import decode_trf

from .._level0.libutils import get_imports
IMPORTS = get_imports(globals())


def trf2csv(trf_filepath, csv_filepath=None, skip_if_exists=True):
    if not os.path.exists(trf_filepath):
        raise Exception("The provided trf filepath cannot be found.")

    if csv_filepath is None:
        extension_removed = os.path.splitext(trf_filepath)[0]
        csv_filepath = "{}_python_decode.csv".format(extension_removed)

    # Skip if conversion has already occured
    if not skip_if_exists or not os.path.exists(csv_filepath):
        print("Converting {}".format(trf_filepath))
        dataframe = decode_trf(trf_filepath)
        dataframe.to_csv(csv_filepath)
    # else:
    #     print("Skipping {}".format(trf_filepath))


def trf2csv_cli():
    if len(sys.argv) == 1:
        print(
            "=============================================================\n"
            "Need to provide filename(s).\n\n"
            "Example usage for converting all files in current directory:\n"
            "    trf2csv *.trf\n"
            "=============================================================")

    glob_strings = sys.argv[1::]
    for glob_string in glob_strings:
        filepaths = glob(glob_string)
        for filepath in filepaths:
            trf2csv(filepath)
