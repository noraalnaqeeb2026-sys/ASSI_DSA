# HW3 - 2D Array Operations

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# إضافة صف
matrix.append([10,11,12])

# إضافة عمود
extra = [13,14,15,16]
for i in range(len(matrix)):
    matrix[i].append(extra[i])

# تعديل عنصر
matrix[0][1] = 99

# البحث عن عنصر
target = 7
found = False
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] == target:
            print(f"{target} found at row {r+1}, col {c+1}")
            found = True
            break

if not found:
    print("Not found")

# حذف عمود
for row in matrix:
    del row[2]   # حذف العمود الثالث

print("\nFinal Matrix:")
for row in matrix:
    print(row)
