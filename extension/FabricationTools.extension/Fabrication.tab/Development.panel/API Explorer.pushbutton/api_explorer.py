# -*- coding: utf-8 -*-

import json
import clr

from Autodesk.Revit.DB import *


def explore_fabrication_part(part):

    data = {}

    #
    # Basic Identity
    #

    data["Element"] = {}

    data["Element"]["Id"] = part.Id.IntegerValue
    data["Element"]["Category"] = (
        part.Category.Name
        if part.Category
        else None
    )


    #
    # Fabrication Identity
    #

    data["Fabrication"] = {}

    try:
        data["Fabrication"]["Service"] = (
            part.ServiceName
        )
    except:
        pass


    try:
        data["Fabrication"]["GUID"] = (
            str(part.Guid)
        )
    except:
        pass


    #
    # Location
    #

    data["Location"] = {}

    try:

        loc = part.Location

        if hasattr(loc, "Curve"):

            curve = loc.Curve

            data["Location"]["Start"] = (
                str(curve.GetEndPoint(0))
            )

            data["Location"]["End"] = (
                str(curve.GetEndPoint(1))
            )

    except Exception as e:

        data["Location"]["Error"] = str(e)



    #
    # Parameters
    #

    data["Parameters"] = []

    for p in part.Parameters:

        try:

            item = {}

            item["Name"] = p.Definition.Name
            item["Storage"] = str(
                p.StorageType
            )


            if p.HasValue:

                item["Value"] = (
                    p.AsValueString()
                    or str(p.AsString())
                )


            data["Parameters"].append(item)

        except:
            pass



    #
    # Connectors
    #

    data["Connectors"] = []

    try:

        manager = (
            part.ConnectorManager
        )

        for c in manager.Connectors:

            connector = {}

            connector["Origin"] = str(
                c.Origin
            )

            connector["Domain"] = (
                str(c.Domain)
            )

            connector["Shape"] = (
                str(c.Shape)
            )


            data["Connectors"].append(
                connector
            )


    except Exception as e:

        data["Connectors_Error"] = str(e)



    #
    # Save Result
    #

    path = (
        r"C:\Temp\fabrication_api_explorer.json"
    )


    with open(
        path,
        "w"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )


    return data