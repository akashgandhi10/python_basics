import StringIO

message = "this is just a normal string"

f =  StringIO.StringIO(message)

print f.read()
print f.read()
f.write(", this is just a second line")
f.seek(0)
print f.read()
