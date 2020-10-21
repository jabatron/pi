#!/usr/bin/python3
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Hello!!")
print(ascii_banner)

ascii_banner = pyfiglet.figlet_format("ja", font="utopia")
print (ascii_banner)
for i in range (10):
    print(pyfiglet.figlet_format(str(i)))
