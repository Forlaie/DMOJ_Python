pieces = input()
missing = False

if "B" not in pieces:
    print("B")
    missing = True
if "F" not in pieces:
    print("F")
    missing = True
if "T" not in pieces:
    print("T")
    missing = True
if "L" not in pieces:
    print("L")
    missing = True
if "C" not in pieces:
    print("C")
    missing = True

if not missing:
    print("NO MISSING PARTS")