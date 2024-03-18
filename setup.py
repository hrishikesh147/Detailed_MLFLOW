from setuptools import setup,find_packages

NAME="Detailed_project"
VERSION="0.0.0.1"
DESC="Detailed_project describption"
URL="url link"
REQUIREMENTS_FILE="requirements.txt"
HYPHEN_E_DOT="-e ."


def get_requirements():
    with open(REQUIREMENTS_FILE) as f:
        f=f.readlines()
        f=[i.replace(HYPHEN_E_DOT,"") for i in f if HYPHEN_E_DOT in i]
        f=[j.replace("\n","") for j in f if "\n" in j]
        
    return f

setup(name=NAME,
      version=VERSION,
      description=DESC,
      author='hrishikesh',
      author_email='gward@python.net',
      url=URL,
      packages=find_packages(),
      install_requires=get_requirements()
     )