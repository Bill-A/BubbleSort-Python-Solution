class BubbleSort:
    @staticmethod
    def given(list):
        index = 0
        temp = 0
        # print("The list is: ", list)

        while True:
            is_all_sorted = True
            for index in range(len(list)-1):
                if list[index] > list[index + 1]:
                    temp = list[index]
                    list[index] = list[index+1]
                    list[index+1] = temp
                    is_all_sorted = False
                    # print("The list is: ", list)
            # print("\n")
            if is_all_sorted:
                break
        return list
