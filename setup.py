from setuptools import setup, find_packages

setup(
    name='nexa-definitions-and-mappings',
    version='1.3',
    packages=find_packages(),
    include_package_data=True,
    # data_files=[("json_files", ["py_sentimotion_definitions/sentimotion_definitions.json"])],
    install_requires=[
    ],
)
