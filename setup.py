from setuptools import setup, find_packages

def get_requirements(file_path: str) -> list:
    '''This function will return the list of requirements from the given file path.'''
    with open(file_path, 'r') as file:
        requirements = file.read().splitlines()
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Divy Anjali',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)