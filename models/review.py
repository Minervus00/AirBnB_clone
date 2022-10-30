#!/usr/bin/python3
"""Module containing the class Review"""
import models.base_model


class Review(models.base_model.BaseModel):
    """Class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
