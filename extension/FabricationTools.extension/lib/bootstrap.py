# -*- coding: utf-8 -*-

import os
import sys


_initialized = False


def initialize():

    global _initialized

    if _initialized:
        return

    extension = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    lib = os.path.join(
        extension,
        "lib"
    )

    if lib not in sys.path:
        sys.path.insert(0, lib)

    _initialized = True