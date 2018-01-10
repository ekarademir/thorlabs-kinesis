# thorlabs_kinesis

Python bindings for Thorlabs Kinesis DLLs. This project aims to map all C API
functions provided by Kinesis libraries to python. More information on
Kinesis Motion Control Software can be found on
[Thorlabs' Website](https://www.thorlabs.com/software_pages/ViewSoftwarePage.cfm?Code=Motion_Control).

The version I'm using to map the libraries is **1.14.4.0 64 Bit**

This project emerged as a need to use it with Thorlabs BSC201, BSC203, and LTS150.
So examples are tested with those controllers on Windows 7 with Python 3.6.

Binding methodology is inspired by
[PySDL2](https://github.com/marcusva/py-sdl2) project.

Code structure in the original DLLs is transferred 1-1, even though it could
have benefited from some refactoring. This makes easier to map examples given in
Thorlabs' documentation.