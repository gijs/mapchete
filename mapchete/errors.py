"""Errors and Warnings."""


class MapcheteProcessImportError(ImportError):
    """Raised when a module of a mapchete process cannot be imported."""


class MapcheteProcessSyntaxError(SyntaxError):
    """Raised when mapchete process file cannot be imported."""


class MapcheteProcessException(Exception):
    """Raised when a mapchete process execution fails."""


class MapcheteProcessOutputError(ValueError):
    """Raised when a mapchete process output is invalid."""
