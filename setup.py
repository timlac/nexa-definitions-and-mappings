from setuptools import setup, find_packages

setup(
    name='nexa-definitions-and-mappings',
    version='1.1',
    packages=find_packages(),
    data_files=[("json_files", ["py_sentimotion_definitions/sentimotion_definitions.json"])],
    install_requires=[
    ],
)
