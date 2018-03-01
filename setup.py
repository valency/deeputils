from distutils.core import setup

setup(
    name='deeputils',
    version='1.3.1',
    packages=['deeputils'],
    url='http://open.deepera.com',
    license='CPL-3.0',
    author='Deepera Co., Ltd.',
    author_email='yding@deepera.com',
    description='Deepera Development Utils',
    install_requires=[
        'django',
        'djangorestframework'
    ],
)
