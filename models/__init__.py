#!/usr/bin/python3
"""Module for the __init__ pyfile"""
# FileStorage = __import__("engine/file_storage").FileStorage
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
