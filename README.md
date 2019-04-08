# Py2C 🥧👀

Simple demo to pass Python objects such as classes, numpy arrays, strings, ints,.. to a C/C++ function and get its result back.


1. Compile your C/C++ library as a shared library

    1.1 Compile a shared library (here `utils`):
    
    ````
    g++ -std=c++11 -Wall -shared -fPIC utils.cpp -o utils.so
    ````
    
    1.2 Check for name mangling: 
    You should see your function's name clearly, like "_func_name", and not mangled (e.g.: "__Z9func_namePiS_i")
    
    ```
    nm utils.so | grep (func_name)
    ```
    
    If you have this problem, simply add `extern "C"` to your function declaration.
    
2. Then, use `ctypes` to load your C/C++ library in Python

3. Write a pretty Python function to wrap the C binding
