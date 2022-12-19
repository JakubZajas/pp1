class Arrays():

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)

    def same_values(value, key):
        lista = []
        for i in range(value):
            lista.append(key)
        return lista

    def random_values(number, od, do):
        from random import randint
        lista = []
        for i in range(number):
            x = randint(od, do)
            lista.append(x)

        return lista

    def sortttt(array, od, do):
        x = 0
        for i in array:
            if i >= od and i <= do:
                x += 1

        return x


print(Arrays.same_values(10, 4))
print(Arrays.random_values(20, -7, 8))
array = Arrays.random_values(20, -7, 8)
print(Arrays.sortttt(array, -1, 1))
