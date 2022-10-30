#!/usr/bin/python3
"""Module containing the class City"""
import models.base_model


class City(models.base_model.BaseModel):
    """Class that inherits from BaseModel"""
    state_id = ""
    name = ""
