import ctypes
import os

# Полный путь к библиотеке
libgobject_path = r'C:\msys64\mingw64\bin\libgobject-2.0-0.dll'

try:
    libgobject = ctypes.cdll.LoadLibrary(libgobject_path)
    print("Библиотека libgobject-2.0-0 успешно загружена!")
except Exception as e:
    print(f"Ошибка загрузки библиотеки: {e}")