import kivy
from kivy.utils import platform

from javis.javis import JavisApp

if __name__ == '__main__':
    if platform == 'android':
        from android.permissions import request_permissions, Permission
        request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])

    app = JavisApp()
    JavisApp().run()
