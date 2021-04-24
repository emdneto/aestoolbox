"""Top-level package for aestoolbox."""
from pkgutil import extend_path
from .release import __version__  # noqa: F401

__path__ = extend_path(__path__, __name__)
