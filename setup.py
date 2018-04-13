from distutils.core import setup

setup(
    name='deeputils',
    version='1.3.2',
    packages=['deeputils'],
    url='https://github.com/valency/deeputils',
    download_url = 'https://github.com/valency/deeputils/releases/download/v1.3.2/deeputils-1.3.2.tar.gz',
    license='CPL-3.0',
    author='Deepera Co., Ltd.',
    author_email='yding@deepera.com',
    description='Deepera Development Utils',
    keywords = ['utils', 'logging'],
    install_requires=[
        'django',
        'djangorestframework'
    ],
)
