import pathlib

__all__ = [
    'TEMPLATE_DIR',
    'DATABASE_TEMPLATE_DIRS',
    'DATABASE_TEMPLATE_FILES',
]


TEMPLATE_NAME = 'template_project'
TEMPLATE_DIR = pathlib.Path(__file__).parent / TEMPLATE_NAME
DATABASE_TEMPLATE_DIRS = ['users', 'migrations', ]
DATABASE_TEMPLATE_FILES = ['alembic.ini', ]
