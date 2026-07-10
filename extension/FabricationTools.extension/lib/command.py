# -*- coding: utf-8 -*-

"""
FabricationTools Command Base

Provides a common environment for all FabricationTools commands.
"""

from bootstrap import initialize

initialize()

import time
from contextlib import contextmanager

from pyrevit import revit, forms

from Autodesk.Revit.DB import Transaction
from Autodesk.Revit.UI.Selection import ObjectType


class Command(object):

    def __init__(self):

        self.doc = revit.doc
        self.uidoc = revit.uidoc
        self.app = self.doc.Application
        self.uiapp = self.uidoc.Application

        self._start_time = None

    # ---------------------------------------------------------
    # Output
    # ---------------------------------------------------------

    def header(self, title):

        print("")
        print("=" * 70)
        print(title)
        print("=" * 70)
        print("")

    def info(self, message):

        print(message)

    def success(self, message):

        print("[SUCCESS] {}".format(message))

    def warning(self, message):

        print("[WARNING] {}".format(message))

    def error(self, message):

        print("[ERROR] {}".format(message))

    # ---------------------------------------------------------
    # Dialogs
    # ---------------------------------------------------------

    def alert(self,
              message,
              title="FabricationTools"):

        forms.alert(
            message,
            title=title
        )

    # ---------------------------------------------------------
    # Pretty Printer
    # ---------------------------------------------------------

    def print_object(self,
                     obj,
                     title=None):

        if title:

            print("-" * 70)
            print(title)

        if obj is None:

            print("  <None>")
            return

        if hasattr(obj, "to_dict"):

            data = obj.to_dict()

            for key in sorted(data.keys()):

                print(
                    "  {:22} {}".format(
                        key + ":",
                        data[key]
                    )
                )

            return

        if isinstance(obj, dict):

            for key in sorted(obj.keys()):

                print(
                    "  {:22} {}".format(
                        key + ":",
                        obj[key]
                    )
                )

            return

        if isinstance(obj, (list, tuple)):

            for item in obj:

                print("  {}".format(item))

            return

        print("  {}".format(obj))

    # ---------------------------------------------------------
    # Selection
    # ---------------------------------------------------------

    def pick_element(self,
                     message="Select Element"):

        reference = self.uidoc.Selection.PickObject(
            ObjectType.Element,
            message
        )

        return self.doc.GetElement(reference)

    # ---------------------------------------------------------
    # Transactions
    # ---------------------------------------------------------

    @contextmanager
    def transaction(self, name):

        transaction = Transaction(
            self.doc,
            name
        )

        transaction.Start()

        try:

            yield transaction

            transaction.Commit()

        except Exception:

            if transaction.HasStarted():

                transaction.RollBack()

            raise

    # ---------------------------------------------------------
    # Timer
    # ---------------------------------------------------------

    def start_timer(self):

        self._start_time = time.time()

    def stop_timer(self):

        if self._start_time is None:
            return 0.0

        elapsed = time.time() - self._start_time

        self.info(
            "Elapsed Time: {:.2f} seconds".format(
                elapsed
            )
        )

        return elapsed

    # ---------------------------------------------------------
    # Hanger Point Display
    # ---------------------------------------------------------

    def show_hanger_points(self, hanger_points):

        self.header("HANGER POINTS")

        count = len(hanger_points)

        self.info(
            "Generated {} hanger point(s).".format(count)
        )

        print("")

        if count == 0:

            self.warning("No hanger points generated.")

            self.alert(
                "No hanger points generated.",
                title="Pipeline Complete"
            )

            return

        for index, point in enumerate(
                hanger_points,
                start=1):

            self.print_object(
                point,
                "Hanger {}".format(index)
            )

        print("")
        print("=" * 70)
        print("Pipeline Complete")
        print("=" * 70)

    # ---------------------------------------------------------
    # Exception Handling
    # ---------------------------------------------------------

    def handle_exception(self):

        import traceback

        self.header("COMMAND FAILED")

        traceback.print_exc()

        self.alert(
            "See the pyRevit output window for details.",
            title="FabricationTools Error"
        )