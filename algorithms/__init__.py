
def leftRightSum(array):

    try:
        if len(array) == 1 or len(array) == 2:
            return {"error": True, "message": "Array with an insufficient length"}

        else:
            left_sum, right_sum, left_pivot, right_pivot = 0, 0, 0, len(array)-1

            while left_pivot <= right_pivot:
                if (left_sum == right_sum) and (left_pivot == right_pivot):
                    return {"error": False, "message": left_pivot}
                    break
                elif (left_sum == right_sum):
                    left_sum += array[left_pivot]
                    right_sum += array[right_pivot]
                    left_pivot += 1
                    right_pivot -= 1
                elif left_sum > right_sum:
                    right_sum += array[right_pivot]
                    right_pivot -= 1
                elif left_sum < right_sum:
                    left_sum += array[left_pivot]
                    left_pivot += 1 
            else:
                return {"error": True, "message": "This array does not have a index where left and right arrays summation is equal"}

    except ValueError:
        return {"error": True, "message": "Input elements must be positive integers"}
    