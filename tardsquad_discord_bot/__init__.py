# try:
# from importlib import metadata
# except ImportError:  # for Python<3.8. Reference: https://stackoverflow.com/a/59734959/265508
# import importlib_metadata as metadata

# # Read version from pyproject.toml. Might not be correct in dev enviorment, but will be when distributed.
# # Reference: https://stackoverflow.com/a/67097076/265508
# __version__ = metadata.version("tardsquad-discord-bot")

from pathlib import Path

from single_source import get_version

__version__ = get_version(__name__, Path(__file__).parent.parent)
