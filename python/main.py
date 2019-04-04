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
    c_size = ctypes.c_int(len(dim))
    func = _libutils.array_sum
    func.restype = ctypes.c_float
    return func(c_arr, c_dim, c_size)


def c_array_sum_p(arr, dim):
    c_arr = arr.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
    c_dim = dim.ctypes.data_as(ctypes.POINTER(ctypes.c_int))
    c_size = ctypes.c_int(len(dim))

    func = _libutils.array_sum_p
    func.restype = ctypes.c_float

    return func(c_arr, c_dim, c_size)


def c_add_vectors(a, b):
    func = _libutils.sum_vector_bw

    # [ARGUMENTS] Option 1:
    # p_a = a.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
    # p_b = b.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
    # c_size = ctypes.c_int(size)

    # [ARGUMENTS] Option 2:
    func.argtypes = [np.ctypeslib.ndpointer(dtype=a.dtype, ndim=a.ndim, flags='C_CONTIGUOUS'),
                     np.ctypeslib.ndpointer(dtype=b.dtype, ndim=b.ndim, flags='C_CONTIGUOUS'),
                     ctypes.c_int
                     ]

    # [OUTPUT] Option 1: (and then cast array -np.fromiter-)
    func.restype = ctypes.POINTER(ctypes.c_float)
    c = func(a, b, len(a))
    cc = np.array(np.fromiter(c, dtype=np.float32, count=len(a)))

    # [OUTPUT] Option 2: (cast directly into Numpy) -not working-
    # func.restype = np.ctypeslib.ndpointer(dtype=ctypes.c_float, ndim=a.ndim, shape=(len(a),), flags='C_CONTIGUOUS')
    # c = func(a, b, len(a))  # returns a pointer

    return c


def main():
    print("Variables: *******************************")
    # Declare (test) variables
    a, b = 1, 3
    arr_m = np.array(
        [[1.0, 2.0],
         [3.0, 4.0],
         [5.0, 6.0]],
        dtype=np.float32
    )
    arr_v = np.array([1, 2, 3], dtype=np.float32)
    arr_w = np.array([4, 5, 6], dtype=np.float32)
    print("a = {}".format(a))
    print("b = {}".format(b))
    print("Array v: {}".format(arr_v))
    print("Array w: {}".format(arr_w))
    print("Array M:")
    print(arr_m)
    print("")
    print("")

    print("Tests: *******************************")

    # Test 1: Sum two integers *******************************************************************
    res = c_dummy_sum(a, b)
    print("Dummy sum (C++): a+b={}".format(res))

    # Test 2: Sum array (from Python List)  *****************************************************
    arr1d = list(arr_m.flatten(order='C'))  # Row major
    arr_dim = list(arr_m.shape)
    res_c = c_array_sum(arr1d, arr_dim)
    print("Array M sum (from Python list; C++): {}".format(res_c))

    # Test 3: Sum array (from Numpy array)  *****************************************************
    arr_dim = np.array(arr_m.shape, dtype=np.int32)
    res_c_p = c_array_sum_p(arr_m, arr_dim)
    print("Array M sum (from Numpy array; C++): {}".format(res_c_p))

    # Test 4: Sum two vectors bit-wise  *****************************************************
    res_c = c_add_vectors(arr_v, arr_w)
    print("Sum two vectors bit-wise (C++): v+w={}".format(list(res_c)))


if __name__ == "__main__":
    main()
