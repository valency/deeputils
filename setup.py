from distutils.core import setup

setup(
    name='deeputils',
    version='1.5.8',
    packages=['deeputils'],
    url='https://github.com/valency/deeputils',
    download_url='https://github.com/valency/deeputils/releases/download/v1.5.8/deeputils-1.5.8.tar.gz',
    license='CPL-3.0',
    author='Deepera Co., Ltd.',
    author_email='yding@deepera.com',
    description='Deepera Development Utils',
    keywords=['utils', 'logging'],
    install_requires=[
        'django',
        'djangorestframework'
    ],
)
