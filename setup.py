'''
The setup.py file is a file that is used to create a Python package. It is used by setuptools (or disutils in older Python versions) to install the package. The setup.py file is used to specify the metadata about the package such as the name, version, and dependencies.
'''
from setuptools import find_packages, setup 
from typing import List 

def get_requirements() -> List[str]:
    """ Get the requirements from the requirements.txt file and return list of requirements. """
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt') as file:
            #Read Read lines from the file 
            lines = file.readlines()
            ##Process each line 
            for line in lines:
                requirement = line.strip() 
                #Ignore empty lines and -e.
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement) 
    except FileNotFoundError:
        print("Requirements file not found.")
    return requirement_lst

#print(get_requirements())

setup(
    name = "Network Security",
    version="0.0.1",
    author = "Utkarss",
    author_email="utkrshsharma141@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)
