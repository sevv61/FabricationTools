class PlacementResult(object):

    def __init__(self):

        self.success = True

        self.placed_count = 0

        self.failed_count = 0

        self.skipped_count = 0

        self.placed_elements = []

        self.warnings = []

        self.errors = []