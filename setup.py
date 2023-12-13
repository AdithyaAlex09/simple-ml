from setuptools import find_packages,setup
from typing import List

hyphen='-e .'

def get_requirements(file_path:str)->list[str]:
    '''this function returns list of requirements'''
    requirements=[]
    with open(file_path) as file_object:
        requirements=file_object.readlines()
        requirements=[re.replace("\n"," ")for re in requirements]
        
        if hyphen in requirements:
            requirements.remove(hyphen)
    return requirements



setup(
    name='mlproject',
    version='0.0.1',
    author='alex',
    author_email='sunkariadithya46@gmail.com',
    packages=find_packages(),
    install_requirements=get_requirements('requirements.txt')
    )