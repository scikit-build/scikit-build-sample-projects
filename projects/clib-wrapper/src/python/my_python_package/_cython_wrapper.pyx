cimport numpy as np


cdef extern from "../../cxx/my_c_module.h":
    cdef int my_c_func(int* int32_array, int num_items);


def my_cython_func(np.ndarray[np.int32_t, ndim=1] int32_array):
    """
    Example:
        >>> import numpy as np
        >>> int32_array = np.arange(10) * 10
        >>> result = my_cython_func(int32_array)
        >>> print('result = {!r}'.format(result))
    """

    # Get a raw c view of the ndarray
    cdef int [:] int32_array_view = int32_array
    cdef int num_items = len(int32_array)

    cdef int result = my_c_func(&int32_array_view[0], num_items)
    return result
