class Vector:
    def __init__(self, dimensions, intervals):
        self.dimensions = dimensions
        self.intervals = intervals
        self.data = self.generate_vector()

    def generate_vector(self):
        vector = []
        for i in range(self.dimensions[0]):
            row = []
            for j in range(self.dimensions[1]):
                element = self.calculate_element(i, j)
                row.append(element)
            vector.append(row)
        return vector

    def calculate_element(self, i, j):
       
        return i * self.intervals[1] + j * self.intervals[0]

    def direct_access(self, i, j):
        return self.data[i][j]

    def interleaved_access(self, i, j):
        return self.data[j][i]

    def determine_vectors(self):
        row_vectors = []
        column_vectors = []

        for i in range(self.dimensions[0]):
            row_vector = self.data[i]
            row_vectors.append(row_vector)

        for j in range(self.dimensions[1]):
            column_vector = [self.data[i][j] for i in range(self.dimensions[0])]
            column_vectors.append(column_vector)

        return row_vectors, column_vectors



dimensions = (4, 5)
intervals = (2, 3)

vector = Vector(dimensions, intervals)

# Прямой доступ к элементам вектора
print("Прямой доступ:")
for i in range(dimensions[0]):
    for j in range(dimensions[1]):
        print(vector.direct_access(i, j), end=" ")
    print()

# Доступ посредством векторов Айлиффа
print("\nДоступ посредством векторов Айлиффа:")
for i in range(dimensions[1]):
    for j in range(dimensions[0]):
        print(vector.interleaved_access(i, j), end=" ")
    print()

# Определение векторов
row_vectors, column_vectors = vector.determine_vectors()
print("\nВекторы по строкам:")
for row_vector in row_vectors:
    print(row_vector)

print("\nВекторы по столбцам:")
for column_vector in column_vectors:
    print(column_vector)
