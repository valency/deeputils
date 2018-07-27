import markdown2
from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = '\n'.join(f.readlines())

setup(
    name='deeputils',
    version='1.7.27',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/valency/deeputils/',
    license='CPL-3.0',
    author='Deepera Co., Ltd.',
    author_email='yding@deepera.com',
    description=markdown2.markdown(long_description),
    keywords=['utils', 'logging'],
    install_requires=[
        'django',
        'djangorestframework',
        'coreapi',
        'markdown',
        'requests'
    ],
)
