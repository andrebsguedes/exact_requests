from random import shuffle

def selection_sort(list_values):
  list_length = len(list_values)
  i, j = 0, 0

  while i < list_length:
    j = i

    while j < list_length:
      if list_values[j] < list_values[i]:
        list_values[j], list_values[i] = list_values[i], list_values[j]

      j += 1

    i += 1

  return list_values
  
def get_possible_position(value, list_range):
    inferior = 0
    superior = len(list_range)-1
    return inferior + (superior - inferior) * ((value-list_range[inferior])/(list_range[superior]-list_range[inferior]))

def interpolation_search(value, list_values):
    inferior = 0
    superior = len(list_values)-1
    print(inferior)
    possible_position = get_possible_position(value,list_values[inferior:superior])+inferior
    print(possible_position)
    if(value < list_values[possible_position]):
        superior = possible_position-1
    elif(value >= list_values[possible_position]):
        inferior = possible_position
    possible_position = interpolation_search(value, list_values[inferior:superior])+inferior
    return possible_position


values = range(10)
print values
print(interpolation_search(9,values))

