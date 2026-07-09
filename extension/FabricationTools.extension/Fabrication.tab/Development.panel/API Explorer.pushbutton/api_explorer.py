# -*- coding: utf-8 -*-

import json
import os

from Autodesk.Revit.DB import *


# ---------------------------------------------------------
# Unicode cleanup
# ---------------------------------------------------------

def clean_unicode(value):

    if value is None:
        return None

    try:

        return value.encode(
            "utf-8",
            "replace"
        ).decode(
            "utf-8"
        )

    except:

        return str(value)



def sanitize_dictionary(obj):

    if isinstance(obj, dict):

        return {
            clean_unicode(k):
            sanitize_dictionary(v)

            for k, v in obj.items()
        }


    elif isinstance(obj, list):

        return [
            sanitize_dictionary(x)
            for x in obj
        ]


    else:

        return clean_unicode(obj)



# ---------------------------------------------------------
# Fabrication API Explorer
# ---------------------------------------------------------

def explore_fabrication_part(part):

    data = {}


    # -----------------------------------------------------
    # Element Information
    # -----------------------------------------------------

    data["Element"] = {}

    data["Element"]["Id"] = (
        part.Id.IntegerValue
    )


    try:

        data["Element"]["Category"] = (
            part.Category.Name
        )

    except:

        data["Element"]["Category"] = None



    # -----------------------------------------------------
    # Fabrication Information
    # -----------------------------------------------------

    data["Fabrication"] = {}


    try:

        data["Fabrication"]["Service"] = (
            part.ServiceName
        )

    except Exception as e:

        data["Fabrication"]["Service_Error"] = (
            str(e)
        )


    try:

        data["Fabrication"]["GUID"] = (
            str(part.Guid)
        )

    except Exception as e:

        data["Fabrication"]["GUID_Error"] = (
            str(e)
        )



    # -----------------------------------------------------
    # Location
    # -----------------------------------------------------

    data["Location"] = {}


    try:

        location = part.Location


        if hasattr(location, "Curve"):

            curve = location.Curve


            data["Location"]["Start"] = (
                str(curve.GetEndPoint(0))
            )


            data["Location"]["End"] = (
                str(curve.GetEndPoint(1))
            )


    except Exception as e:

        data["Location"]["Error"] = (
            str(e)
        )



    # -----------------------------------------------------
    # Parameters
    # -----------------------------------------------------

    data["Parameters"] = []


    try:

        for p in part.Parameters:

            parameter = {}


            try:

                parameter["Name"] = (
                    p.Definition.Name
                )

            except:

                parameter["Name"] = None



            try:

                parameter["StorageType"] = (
                    str(p.StorageType)
                )

            except:

                parameter["StorageType"] = None



            try:

                if p.HasValue:

                    value = (
                        p.AsValueString()
                    )


                    if value is None:

                        value = (
                            p.AsString()
                        )


                    parameter["Value"] = (
                        value
                    )


            except Exception as e:

                parameter["Value_Error"] = (
                    str(e)
                )


            data["Parameters"].append(
                parameter
            )


    except Exception as e:

        data["Parameters_Error"] = (
            str(e)
        )



    # -----------------------------------------------------
    # Connectors
    # -----------------------------------------------------

    data["Connectors"] = []


    try:

        connector_manager = (
            part.ConnectorManager
        )


        for connector in connector_manager.Connectors:


            item = {}


            try:

                item["Origin"] = (
                    str(connector.Origin)
                )

            except:

                pass



            try:

                item["Domain"] = (
                    str(connector.Domain)
                )

            except:

                pass



            try:

                item["Shape"] = (
                    str(connector.Shape)
                )

            except:

                pass



            try:

                item["Radius"] = (
                    str(connector.Radius)
                )

            except:

                pass



            try:

                item["Width"] = (
                    str(connector.Width)
                )

            except:

                pass



            try:

                item["Height"] = (
                    str(connector.Height)
                )

            except:

                pass



            data["Connectors"].append(
                item
            )


    except Exception as e:

        data["Connectors_Error"] = (
            str(e)
        )



    # -----------------------------------------------------
    # Export JSON
    # -----------------------------------------------------

    output_folder = (
        r"C:\Temp"
    )


    if not os.path.exists(output_folder):

        os.makedirs(output_folder)



    output_file = os.path.join(
        output_folder,
        "fabrication_api_explorer.json"
    )


    cleaned_data = sanitize_dictionary(
        data
    )


    with open(
        output_file,
        "w"
    ) as f:

        json.dump(
            cleaned_data,
            f,
            indent=4
        )


    return cleaned_data