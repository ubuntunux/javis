import kivy
from kivy.utils import platform

from javis.javis import JavisApp

import numpy
import cython

import cython
@cython.cclass
class A:
    cython.declare(a=cython.int, b=cython.int)
    c = cython.declare(cython.int, visibility='public')
    d = cython.declare(cython.int)  # private by default.
    e = cython.declare(cython.int, visibility='readonly')

    def __init__(self, a, b, c, d=5, e=3):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

print(A(1,2,3).a)

if __name__ == '__main__':
    if platform == 'android':
        from android.permissions import request_permissions, Permission
        request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])

    app = JavisApp()
    JavisApp().run()
