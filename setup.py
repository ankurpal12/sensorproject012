from setuptools import setup, find_packages
# setuptools>> is a package that provides tools for packaging Python projects.
# find_packages is a utility function that automatically discovers all packages and subpackages in a directory.
from typing import List
# typing>> it is used to display output in lists format.

HYPEN_E_DOT = '-e.' # this is present in requirements.txt file. it is used to install the dependencies directly from the file.
def get_requirements(file_path:str) -> List[str]: # here we are defining a function which will read the requirements.txt file and return a list of dependencies.
    requirements=[]
    with open(file_path) as file_obj: # here we are opening the file in read mode.
        requirements=file_obj.readlines() # here we are reading all the lines in the file and storing them in a list.
        requirements=[req.replace("\n","") for req in requirements]

    if HYPEN_E_DOT in requirements:  # here we are checking if -e. is present in the list of dependencies or requirements.txt file.
        requirements.remove(HYPEN_E_DOT) # we remove -e. from the list of dependencies because it is not a valid dependency.
    return requirements


setup(
    name='fault detection',
    version='1.0.0',
    author='Ankur',
    author_email='ankurpal7827@gmail.com',
    install_requirements=get_requirements('requirements.txt'), # we can write dependencies(pandas, numpy etc.) manually but here we are using file requirements.txt
    # here get_requirements is a function which will read the requirements.txt file and return a list of dependencies.
    # install_requirements>> it is used to install all the dependencies mentioned in requirements.txt file
    packages=find_packages(), # it will find all the packages in the directory automatically. & store in metadata file.

)
# we use commad 'python setup.py install' to install the package. then some files are created in the directory. such as 
# build, dist, fault_detection.egg-info
# build>> it contains all the files which are required to build the package.
# dist>> it contains the final package which can be distributed.
# fault_detection.egg-info>> it contains the metadata of the package.
# pip list >> it shows all the packages which are installed in the system.
# we can create a test filt the test the package. in this we rerunt the command 'python setup.py install' and check the pip list.
# we can see that in fault-detection file test file is created as package. this can be seen in fault_detection.egg-info>>Sources.txt as package.
# we  can install the dependencies by adding -e. . in requirements.txt file. this will install the dependencies directly from the file.



#updating new li