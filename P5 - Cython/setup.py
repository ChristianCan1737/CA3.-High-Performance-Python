from setuptools import setup, Extension
from Cython.Build import cythonize
import os

# Specify your .pyx files here
pyx_files = [
    "cython1.pyx",
    "cython2.pyx",
    "cython3.pyx",
    "cython4.pyx",
]

# Automatically generate extensions from the .pyx files
extensions = [Extension(os.path.splitext(file)[0], [file]) for file in pyx_files]

# Cythonize extensions with some additional compiler directives
setup(
    ext_modules=cythonize(
        extensions,
        compiler_directives={'language_level': "3", 'embedsignature': True}
    ),
)
