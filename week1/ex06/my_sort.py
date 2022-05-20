d = {
'Hendrix' : '1942',
'Allman' : '1946',
'King' : '1925',
'Clapton' : '1945',
'Johnson' : '1911',
'Berry' : '1926',
'Vaughan' : '1954',
'Cooder' : '1947',
'Page' : '1944',
'Richards' : '1943',
'Hammett' : '1962',
'Cobain' : '1967',
'Garcia' : '1942',
'Beck' : '1944',
'Santana' : '1947',
'Ramone' : '1948',
'White' : '1975',
'Frusciante': '1970',
'Thompson' : '1949',
'Burton' : '1939',
}

yearOrder = sorted(d.items(), key = lambda x:x[1])

for item in yearOrder:
    print(item[0])

flipped = {}
  
for key, value in yearOrder:
    if value not in flipped:
        flipped[value] = [key]
    else:
        flipped[value].append(key)
        flipped[value] = sorted(flipped[value])

for key, value in flipped.items():
    for item in value:
        print(item)