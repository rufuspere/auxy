#https://www.freecodecamp.org/news/build-your-first-python-package/
from setuptools import setup, find_packages

VERSION = '1.0' 
DESCRIPTION = 'Auxiliar de Elecciones'
LONG_DESCRIPTION = 'Contiene funciones útiles'

# Setting up
setup(
       # the name must match the folder name 'auxy'
        name="auxy", 
        version=VERSION,
        author="Anónimo",
        author_email="rafael.pereira.estal@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=['auxy'],
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        url="https://github.com/rufuspere/auxylia.git",
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
        ]
)