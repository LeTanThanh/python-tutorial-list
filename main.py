if __name__ == "__main__":
  # What is a List

  empty_list = []
  print(empty_list)

  todo_list = ["Learn Python List", "How to manage List elements"]
  print(todo_list)

  numbers = [1, 3, 2, 7, 9, 4]
  print(numbers)

  colors = ["red", "green", "blue"]
  print(colors)

  coordinates = [[0, 0], [100, 100], [200, 200]]
  print(coordinates)

  # Accessing elements in a list

  """
  list[index]
  """

  numbers = [1, 3, 2, 7, 9, 4]
  print(numbers)
  print(numbers[0])
  print(numbers[-1])
  print(numbers[-1])
  print(numbers[-2])

  # Modifying elements in a list

  """
  list[index] = new_value
  """

  numbers = [1, 3, 2, 7, 9, 4]
  print(numbers)
  numbers[0] = 10
  print(numbers)

  numbers = [1, 3, 2, 7, 9, 4]
  print(numbers)
  numbers[1] = numbers[1] * 10
  print(numbers)

  numbers = [1, 3, 2, 7, 9, 4]
  print(numbers)
  numbers[2] = numbers[2] / 2
  print(numbers)

  # Adding elements to the list

  numbers = [1, 3, 2, 7, 9, 4]
  print(numbers)
  numbers.append(100)
  print(numbers)

  numbers = [1, 3, 2, 7, 9, 4]
  print(numbers)
  numbers.insert(2, 100)
  print(numbers)
