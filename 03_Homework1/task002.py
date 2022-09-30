# Напишите программу для проверки истинности 
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат

# закон деМоргана?

bool_ar = [True, False]
for x in bool_ar:
    for y in bool_ar:
        for z in bool_ar:
            print(f'x={x}, y={y}, z={z} => {not(x or y or z) == ((not x) and (not y) and (not z))}')