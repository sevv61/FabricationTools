# -*- coding: utf-8 -*-

import sys
import os

from pyrevit import revit, forms


# ---------------------------------------------------------
# Add extension lib folder to Python path
# ---------------------------------------------------------

extension_path = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                __file__
            )
        )
    )
)

lib_path = os.path.join(
    extension_path,
    "lib"
)

if lib_path not in sys.path:
    sys.path.append(lib_path)


# ---------------------------------------------------------
# Import Pipeline
# ---------------------------------------------------------

from pipeline.hanger_pipeline import HangerPipeline


# ---------------------------------------------------------
# Revit Context
# ---------------------------------------------------------

doc = revit.doc


# ---------------------------------------------------------
# Execute Pipeline
# ---------------------------------------------------------

try:

    pipeline = HangerPipeline(doc)

    hanger_points = pipeline.execute()

    print("")
    print("===================================")
    print(" HANGER PIPELINE COMPLETE")
    print("===================================")
    print("")

    print("Generated {} hanger point(s).".format(
        len(hanger_points)
    ))

    for i, point in enumerate(hanger_points):

        print(
            "{:03d} : {}".format(
                i + 1,
                point
            )
        )

    forms.alert(
        "{} hanger point(s) generated.".format(
            len(hanger_points)
        ),
        title="Pipeline Complete"
    )


except Exception as ex:

    import traceback

    print("")
    print("===================================")
    print(" PIPELINE FAILED")
    print("===================================")
    print("")

    traceback.print_exc()

    forms.alert(
        str(ex),
        title="Pipeline Error"
    )