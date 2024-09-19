def main(array: list):
    partition: list = [[el] for el in array]

    isValid: bool = False
    while (not isValid):
        i = 0
        isValid = True
        while i < len(partition)-1:
            if max(partition[i]) > min(partition[i+1]):
                partition[i].extend(partition[i+1])
                partition.pop(i+1)
                isValid = False

            i += 1
    print(f"{partition=}")
    print(f"{len(partition)=}")


arrays = [[2, 1, 2, 3, 3, 4, 3], [2, 1, 2, 1, 3, 4, 3]]


if __name__ == "__main__":

    print(f"solving array {arrays[0]}")
    main(arrays[0])
    print("-------------")
    print(f"solving array {arrays[1]}")
    main(arrays[1])
