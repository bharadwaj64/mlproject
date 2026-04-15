from setuptools import setup,find_packages 
from typing import List

requirements = []
hypen_e_dot = '-e .'

def get_requirements(filename:str)->List[str]:
    with open(filename,'r') as file:
        requirements = file.readlines()
        requirements = [requirement.replace('\n','').strip() for requirement in requirements]
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='vittal bharadwaj',
    author_email='t.vittalbharadwaj@gmail.com',
    packages= find_packages(),
    install_requires= get_requirements('requirements.txt')
)
