from tkinter import StringVar


class StringVar:
    def __init__(self, value=""):
      self.value = value

    def get(self):
      return self.value

    def set(self, new_value):
      self.value = new_value

my_string = StringVar("Hello World")
print(my_string.get())

my_string.set("New String Value")
print(my_string.get())



































































