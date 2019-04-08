import numpy as np
import ctypes

# Import my C++ function
_libutils = ctypes.cdll.LoadLibrary("../c++/utils.so")
_libwrapper = ctypes.cdll.LoadLibrary("../c++/wrapper.so")


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
    # func.restype = np.ctypeslib.ndpointer(dtype=ctypes.POINTER(ctypes.c_float), ndim=a.ndim, flags='C_CONTIGUOUS')
    # cc = func(a, b, len(a))  # returns a pointer

    return cc


# Item - init
_libwrapper.Item_init.restype = ctypes.c_void_p
_libwrapper.Item_init.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]

# Item - getName
_libwrapper.Item_getName.restype = ctypes.c_char_p
_libwrapper.Item_getName.argtypes = [ctypes.c_void_p]

# Container - init
_libwrapper.Container_init.restype = ctypes.c_void_p
_libwrapper.Container_init.argtypes = ()

# Container - addItem
_libwrapper.Container_addItem.restype = ctypes.c_int
_libwrapper.Container_addItem.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

# Container - getItem
_libwrapper.Container_getItem.restype = ctypes.c_void_p
_libwrapper.Container_getItem.argtypes = [ctypes.c_void_p, ctypes.c_int]


class Item:

    def __init__(self, id, name, obj=None):
        if obj:
            self.obj = obj
        else:
            c_id = ctypes.c_int(id)
            c_name = ctypes.c_char_p(bytes(name.encode('ascii')))
            c_length = ctypes.c_int(len(name))

            self.obj = _libwrapper.Item_init(c_id, c_name, c_length)

    @classmethod
    def from_pointer(cls, obj):
        return cls(None, None, obj)

    def get_name(self):
        res = _libwrapper.Item_getName(self.obj).decode('ascii')
        return res


class Container:
    def __init__(self):
        self.obj = _libwrapper.Container_init()

    def addItem(self, item):
        return _libwrapper.Container_addItem(self.obj, item.obj)

    def getItem(self, id):
        c_id = ctypes.c_int(id)
        _item = _libwrapper.Container_getItem(self.obj, c_id)
        return Item.from_pointer(_item)


def main():
    # print("Variables: *******************************")
    # # Declare (test) variables
    # a, b = 1, 3
    # arr_m = np.array(
    #     [[1.0, 2.0],
    #      [3.0, 4.0],
    #      [5.0, 6.0]],
    #     dtype=np.float32
    # )
    # arr_v = np.array([1, 2, 3], dtype=np.float32)
    # arr_w = np.array([4, 5, 6], dtype=np.float32)
    # print("a = {}".format(a))
    # print("b = {}".format(b))
    # print("Array v: {}".format(arr_v))
    # print("Array w: {}".format(arr_w))
    # print("Array M:")
    # print(arr_m)
    # print("")
    #
    # print("Tests: *******************************")
    #
    # # Test 1: Sum two integers *******************************************************************
    # res = c_dummy_sum(a, b)
    # print("Dummy sum (C++): a+b={}".format(res))
    #
    # # Test 2: Sum array (from Python List)  *****************************************************
    # arr1d = list(arr_m.flatten(order='C'))  # Row major
    # arr_dim = list(arr_m.shape)
    # res_c = c_array_sum(arr1d, arr_dim)
    # print("Array M sum (from Python list; C++): {}".format(res_c))
    #
    # # Test 3: Sum array (from Numpy array)  *****************************************************
    # arr_dim = np.array(arr_m.shape, dtype=np.int32)
    # res_c_p = c_array_sum_p(arr_m, arr_dim)
    # print("Array M sum (from Numpy array; C++): {}".format(res_c_p))
    #
    # # Test 4: Sum two vectors bit-wise  *****************************************************
    # res_c = c_add_vectors(arr_v, arr_w)
    # print("Sum two vectors bit-wise (C++): v+w={}".format(list(res_c)))


    # Test 5: Class Item  *****************************************************
    item1 = Item(1, "My item 1")
    item1_name = item1.get_name()
    print("Item name: {}".format(item1_name))

    item2 = Item(2, "My item 2")
    item2_name = item2.get_name()
    print("Item name: {}".format(item2_name))

    c = Container()
    res1 = c.addItem(item1)
    res2 = c.addItem(item2)

    print("Container add item: {}".format(res1))
    print("Container add item: {}".format(res2))

    ci_1 = c.getItem(1)
    ci_2 = c.getItem(2)
    print("Container item name: {}".format(ci_1.get_name()))
    print("Container item name: {}".format(ci_2.get_name()))


if __name__ == "__main__":
    main()
