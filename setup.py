"""
Pinterest Client Package Setup
"""
import os
from pathlib import Path
from setuptools import setup, find_namespace_packages


REQUIRES = [
  "urllib3==1.26.12",
  "python-dateutil",
  "python-dotenv==0.20.0",
  "six==1.16.0",
  "Pinterest-Generated-Client==0.1.5"
]

long_description = (Path(__file__).parent / "README.md").read_text()
package_root = os.path.abspath(os.path.dirname(__file__))


module = {}
with open(os.path.join(package_root, "pinterest/version.py"), encoding='UTF-8') as fp:
    exec(fp.read(), module)  # pylint: disable=exec-used
__version__ = module.get("__version__")

setup(
    name="pinterest-api-sdk",
    description="Pinterest API SDK",
    version=__version__,
    author="Pinterest, Inc.",
    author_email="sdk@pinterest.com",
    url="https://github.com/pinterest/pinterest-python-sdk",
    install_requires=REQUIRES,
    include_package_data=True,
    packages=find_namespace_packages(
        include=['pinterest.*', 'pinterest', 'pinterest.version', 'pinterest.config'],
        exclude=[
            'sample',
            'sample.*',
            'tests',
            'tests.*',
            'integration_tests',
            'integration_tests.*',
            '.github',
        ]
    ),
    license='Apache License 2.0',
    long_description=long_description,
    long_description_content_type='text/markdown',
)
