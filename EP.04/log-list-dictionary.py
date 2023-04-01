box = []
box.append('ปากกา')
box.append('ดินสอ')
box.append('ยางลบ')
brand = {'pen':['Lamy','Pentel','Fiber-castel'],'pencil':['hourse','staedtler'],'eraser':'ยางลบไทย'}

print(box)
print(box[1])
print(box[-1])

print(brand['pen'])
print(brand['pen'][2])

#print(brand['eraser'][1]) ใส่ index [1] ไม่ได้ เพราะ eraser ไม่มี list/มีเป็น0
print(brand['eraser'])

print(len(box))#หาว่า box มีกี่ values

print(brand.keys())

print(brand.values())

for B in box:
    print(B)

for br in brand.keys():
    print(br)

for br in brand.values():
    print(br)

for br in brand.items():
    print(br)