from os import path

from setuptools import setup, find_packages

with open(path.join(path.abspath(path.dirname(__file__)), 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='deeputils',
    version='3.8.20',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/valency/deeputils/',
    author='Deepera Co., Ltd.',
    author_email='yding@deepera.com',
    description='Deepera Development Utils',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    keywords=['utils', 'logging'],
    install_requires=[
        'django',
        'djangorestframework',
        'coreapi',
        'markdown',
        'requests',
        'deprecated'
    ]
)
