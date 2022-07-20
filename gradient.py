# After redirecting the output of this Python code to an HTML file, 
# a gradient is produced on a webpage

# Make a black-to-red gradient by stacking <hr>s directly on top of one another
# Afterwards, play around with the RGB values to create different colors of gradients.

print("<!DOCTYPE html>")
print("<html>")

print("<head>")
print("<style>")
print("  hr {margin-top:0; margin-bottom:0}")
print("</style>")
print("</head>")

print("<body>")
for x in range(256):
  print(f'<hr style="color:rgb({x},0,0)">')
print("</body>")

print("</html>")
