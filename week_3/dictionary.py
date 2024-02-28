



laptop = {"make":"lenovo","colour":"grey","weight":"1.6","year":"2012"}

print(laptop["make"])
print(laptop["colour"])
print(laptop["year"])

laptop["colour"] = "red"
laptop["year"] = "2017"

print(laptop)


laptop["size"] = "1200mm x 600mm"
print(laptop)

del laptop["colour"]
print(laptop)

""""

for key,value in laptop.items():
    print(key)
    print("\n")
    print(value)

    """

