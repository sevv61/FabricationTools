# -*- coding: utf-8 -*-

from command import Command


cmd = Command()

try:

    hanger_points = cmd.run_pipeline()

    cmd.show_hanger_points(
        hanger_points
    )

except Exception:

    cmd.handle_exception()