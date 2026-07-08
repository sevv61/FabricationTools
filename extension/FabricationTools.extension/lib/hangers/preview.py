class HangerPreview(object):

    def build_report(self, hanger_points):

        lines = []

        for hanger in hanger_points:

            lines.append(
                "{:6.2f} ft   {}".format(
                    hanger.station,
                    hanger.status
                )
            )

            for note in hanger.notes:

                lines.append(
                    "   - {}".format(note)
                )

        return "\n".join(lines)