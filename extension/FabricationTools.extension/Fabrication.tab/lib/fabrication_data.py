# -*- coding: utf-8 -*-


class FabricationPartData:


    def __init__(self):

        # Revit identity

        self.element_id = None
        self.category = None


        # Fabrication identity

        self.service = None
        self.guid = None


        # Classification

        self.part_type = None


        # Dimensions

        self.width = None
        self.height = None
        self.diameter = None
        self.length = None


        # Connectors

        self.connector_count = 0
        self.connectors = []


        # Rules

        self.requires_hanger = False



    def to_dict(self):

        return {

            "element_id":
                self.element_id,


            "category":
                self.category,


            "service":
                self.service,


            "guid":
                self.guid,


            "part_type":
                self.part_type,


            "width":
                self.width,


            "height":
                self.height,


            "diameter":
                self.diameter,


            "length":
                self.length,


            "connector_count":
                self.connector_count,


            "requires_hanger":
                self.requires_hanger
        }