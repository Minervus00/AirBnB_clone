#!/usr/bin/python3
"""Module for the __init__ pyfile"""
import models.engine.file_storage

storage = models.engine.file_storage.FileStorage()
storage.reload()
