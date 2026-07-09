# -*- coding: utf-8 -*-

class HangerPreview(object):

    def build_report(self, run):

        lines = []

        lines.append(run.part.name)

        lines.append("")

        lines.append(
            "Length : {:.2f}".format(
                run.total_length
            )
        )

        lines.append("")

        lines.append(
            "Hangers : {}".format(
                run.hanger_count
            )
        )

        lines.append("")

        for hanger in run.hanger_points:

            lines.append(hanger.to_string())

        return "\n".join(lines)