#!/usr/bin/python3
"""Created a uniq 'FileStorage' instance for the application"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
