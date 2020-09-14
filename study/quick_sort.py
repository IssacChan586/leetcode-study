from typing import List


class Sort:
    def quick_sort(self, value: List[int]) -> None:
        def sort(value: List[int], l: int, r: int):
            if l >= r:
                return
            i, j, x = l, r, value[l]
            while i < j:
                while i < j and x <= value[j]:
                    j -= 1
                if i < j:
                    value[i] = value[j]
                    i += 1
                while i < j and x > value[i]:
                    i += 1
                if i < j:
                    value[j] = value[i]
                    j -= 1

            value[i] = x
            sort(value, l, i - 1)
            sort(value, i + 1, r)

        sort(value, 0, len(value) - 1)
        print(value)


if __name__ == '__main__':
    value = [0, -2, 1, 9, -99, 22]
    Sort().quick_sort(value)
    assert [-99, -2, 0, 1, 9, 22] == value
