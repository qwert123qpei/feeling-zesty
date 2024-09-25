import random, colorama
colorama.init()

def create_matrix(size):
  matrix = []
  num_list = list(range(1,size**2+1))
  strSize = len(str(num_list[-1]))
  x_vals, y_vals = list(range(size)), list(range(size))

  for x in x_vals:
    mx = []
    for y in y_vals:
      choice = str(random.choice(num_list))
      while True:
        if len(choice) == strSize:
          break
        choice = " " + str(choice)
      mx.append(choice)
      num_list.remove(int(choice))
    matrix += [mx] 
  return matrix

def rotate_x(matrix, direction, x):#direction: 0 for forward, -1 for backwards
  x_matrix = matrix[x]
  n = x_matrix[direction]
  x_matrix.remove(n)

  if direction == 0:
    x_matrix.append(n)
  elif direction == -1:
    x_matrix.insert(0,n)
  return x_matrix

def rotate_y(matrix, direction, y):#direction: -1 for downward, 0 for upwards
  y_values = []
  for i in matrix:
    y_values.append(i[y])

  y_matrix = y_values
  n = y_matrix[direction]
  y_matrix.remove(n)

  if direction == 0:
    y_matrix.append(n)
  elif direction == -1:
    y_matrix.insert(0,n)

  for i in matrix:
    i[y] = y_matrix[0]
    y_matrix.remove(y_matrix[0])

  return y_matrix

def out_matrix(matrix, size):
  s = f"{' '*size} "
  for n in range(len(matrix)):
    f = str(n)
    while True:
      if len(f) == size:
        break
      f = f"{Back.RED} " + str(f) +{Style.RESET_ALL}
    s += f + " "
  s += "\n"
  for i in matrix:  
    for j in i:
      s += j + " "
    s += "\n"
  return s

def main():
  matrix_size = int(input())
  matrix = create_matrix(matrix_size)#creates the matrix
  print(out_matrix(matrix,len(str(matrix_size))))
main()