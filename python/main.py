import numpy as np
import ctypes

# Import my C++ function
_libutils = ctypes.cdll.LoadLibrary("c++/utils.so")


def c_dummy_sum(a, b):
    func = _libutils.dummy_sum
    func.restype = ctypes.c_int
    return func(ctypes.c_int(a), ctypes.c_int(b))


def c_array_sum(arr, dim):
    c_arr = (ctypes.c_float * len(arr))(*arr)
    c_dim = (ctypes.c_int * len(dim))(*dim)
    func = _libutils.array_sum
    func.restype = ctypes.c_float
    return func(c_arr, c_dim, ctypes.c_int(len(dim)))


def main():
    # Test 1
    res = c_dummy_sum(a=1, b=3)
    print("Dummy sum (C++): {}\n".format(res))

    # Test 2
    arr = np.array(
         [[1.0, 2.0],
          [3.0, 4.0],
          [5.0, 6.0]],
        dtype=np.float32
    )
    print("Array:")
    print(arr)
    print("")

    print("Array 1d (row-major)")
    arr1d = list(arr.flatten(order='C'))  # Row major
    arr_dim = list(arr.shape)
    print(arr1d)
    print("")

    res_c = c_array_sum(arr1d, arr_dim)
    print("Array sum (C++): {}".format(res_c))


if __name__ == "__main__":
    main()
