#!/usr/bin/python3

print("content-type:text/html")
print()

import cgi
import subprocess

field_input=cgi.FieldStorage()
x=field_input.getvalue("input")
output=subprocess.getoutput(x)
print(output)