# -*- coding: utf-8 -*-

class HangerValidator(object):

    def validate(self, hanger_points, geometry):

        for hanger in hanger_points:

            if hanger.station < 1.0:

                hanger.status = hanger.STATUS_WARNING

                hanger.notes.append(
                    "Closer than 1'-0\" to duct start."
                )

        return hanger_points