class BubbleSort:
    @staticmethod
    def given(list):
        index = 0
        temp = 0
        # print("The list is: ", list)

        for index in range(len(list)-1):
            if list[index] > list[index + 1]:
                temp = list[index]
                list[index] = list[index+1]
                list[index+1] = temp
                # print("The list is: ", list)
        # print("\n")

        return list
