import random

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
  

def get_possible_position(value, list_values, inferior, superior):
    print  inferior,superior
    possible_position = inferior + (superior - inferior) * ((value-list_values[inferior])/(list_values[superior]-list_values[inferior]))
    print possible_position
    return possible_position

def interpolation_search(value, list_values, inferior, superior):
    possible_position = int(inferior + (superior - inferior) * (float((value-list_values[inferior]))/float((list_values[superior]-list_values[inferior]))))
    if(value < list_values[possible_position]):
        superior = possible_position-1
    elif(value >= list_values[possible_position]):
        inferior = possible_position
    if(value != possible_position):
        interpolation_search(value, list_values, inferior, superior)
    return possible_position
    
values = range(1000000)
print values
print(interpolation_search(37,values,0,len(values)-1))
