from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path :str)->List[str]:
    with open("requirements.txt",'r') as file_obj:
        requirements = file_obj.readline()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name = "Scientific Paper Summerizer",
    version= "1.1.1",
    author = "Umme",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)