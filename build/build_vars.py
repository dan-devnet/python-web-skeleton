import os
from pathlib import Path

DIR_BASE = Path(__file__).resolve().parent.parent
DIR_APP                 = os.path.join(DIR_BASE, 'app')
DIR_VENV                = os.path.join(DIR_BASE, 'venv')
DIR_REQUIREMENTS_TXT    = os.path.join(DIR_BASE, 'app/app')
