"""
It is used by setupt tools to define the configuration of the project like metadata , dependencies
"""
from setuptools import find_packages , setup 
from typing import List 


def get_requirements() -> List[str]:
    
    """
    Function returns list as requirements 
    """
    req_list:List[str] =[]
    try:
        with open('requirements.txt' , 'r') as file:
            # Read lines from the file
            lines = file.readlines()
            # Process each line 
            for line in lines:
                req = line.strip()
                # Ignore the empty lines and -e.
                if req and req!= '-e .':
                    req_list.append(req)
    except FileNotFoundError:
        print("Requirements.txt file not found")
    
    return req_list

print(get_requirements())

setup(
    name = "AI in Network Security",
    version = "0.0.1",
    author = "Leerish Arvind",
    author_email = "arvindleerish@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)