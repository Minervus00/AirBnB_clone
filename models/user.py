#!/usr/bin/python3
"""Module containing the class User"""
import models.base_model


class User(models.base_model.BaseModel):
    """Class that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
