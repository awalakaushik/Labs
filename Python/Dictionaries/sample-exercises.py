numbers={1: 2, 3:4}
numbers.pop(3)
print (numbers)

d={"uno":["one",1],"dos":["two",2],3:["tres","three"]}
print (d.pop("dos")) 

numbers={"one": "uno", "two": "dos", "three": "tres"}
print (numbers.get("one","test"))

d={"uno":["one",1],"dos":["two",2],3:["tres","three"]}
print (d.get(3,'cat'))

d={"uno":"one","dos":"two"}
d.setdefault('one', 'dog')
print (d["one"])

d={"uno":["one",1],"dos":["two",2],3:["tres","three"]}
print (d.has_key(3)) 