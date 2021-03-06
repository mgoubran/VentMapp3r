import os

import ventmapper.convert
import ventmapper.preprocess
import ventmapper.segment
import ventmapper.stats
import ventmapper.qc
import ventmapper.utils

VERSION = (0, 1, 0)
__version__ = '.'.join(map(str, VERSION))

__all__ = ['convert',  'preprocess', 'qc', 'segment', 'stats', 'utils']

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DEPENDS_DIR = os.path.abspath(os.path.join(ROOT_DIR, "..", "depends"))