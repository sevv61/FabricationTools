class HangerPlacer(object):

    def __init__(self,
                 options):

        self.options = options

    def place(self,
              doc,
              run):

        result = PlacementResult()

        for hanger in run.hanger_points:

            if hanger.skip:

                result.skipped_count += 1

                continue

            #
            # Revit API goes here later
            #

            result.placed_count += 1

        return result