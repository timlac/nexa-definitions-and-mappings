from setuptools import setup, find_packages

setup(
    name='nexa-definitions-and-mappings',
    version='1.91',
    packages=find_packages(),
    include_package_data=True,
    # data_files=[("json_files", ["definitions/sentimotion_definitions.json"])],
    install_requires=[
        "numpy"
    ],
)
