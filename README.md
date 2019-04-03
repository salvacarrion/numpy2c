# Numpy2c

Simple demo to pass Python variables such as Numpy arrays to a C/C++ function and get the result back.


1. Compile C/C++ library as a shared library

    1.1 Compile utils:
    
    ````
    g++ -std=c++11 -Wall -shared -fPIC utils.cpp -o utils.so
    ````
    
    1.2 Check for name mangling: 
    You should see you function like this "_array_sum", and not mangled ( "__Z9array_sumPiS_i")
    
    ```
    nm utils.so | grep (your_func)
    ```
    
2. Then, use `ctypes` to load your C/C++ library in Python

3. Write a pretty Python function to wrap the C binding