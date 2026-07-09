# -*- coding: utf-8 -*-

from Autodesk.Revit.DB import FabricationPart

from fabrication_data import FabricationPartData



def extract_fabrication_part(part):


    data = FabricationPartData()



    #
    # Identity
    #

    data.element_id = (
        part.Id.IntegerValue
    )


    try:

        data.category = (
            part.Category.Name
        )

    except:

        pass



    #
    # Fabrication
    #

    try:

        data.service = (
            part.ServiceName
        )

    except:

        pass



    try:

        data.guid = (
            str(part.Guid)
        )

    except:

        pass



    #
    # Connector information
    #

    try:

        connectors = (
            part.ConnectorManager.Connectors
        )


        for c in connectors:

            data.connectors.append(c)


        data.connector_count = len(
            data.connectors
        )


    except:

        pass



    #
    # Initial classification
    #

    data.part_type = (
        classify_part(data)
    )



    return data





def classify_part(data):


    category = (
        data.category or ""
    ).lower()



    if "duct" in category:

        return "DUCT"



    if "pipe" in category:

        return "PIPE"



    return "UNKNOWN"