from distutils.core import setup

setup(
    name='deeputils',
    version='1.7.4',
    packages=['deeputils'],
    url='https://github.com/valency/deeputils',
    license='CPL-3.0',
    author='Deepera Co., Ltd.',
    author_email='yding@deepera.com',
    description='Deepera Development Utils',
    keywords=['utils', 'logging'],
    install_requires=[
        'django',
        'djangorestframework',
        'coreapi',
        'markdown'
    ],
)
