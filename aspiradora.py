from random import randint

def generate_random_number():
  return randint(0, 1)

def generate_random_rooms():
  rooms = ["A", "B"]
  return rooms[generate_random_number()]

asociative_list = []
history = []

for i in range(10):
  asociative_list.append([generate_random_rooms(), generate_random_number()])

def is_room_a(letter):
  return letter == 'A'

def is_room_b(letter):
  return letter == 'B'

def analyze_room(rooms, index):
  room_letter = rooms[index][0]
  is_room_cleaned = rooms[index][1]

  if is_room_cleaned:
    return [room_letter, 'Limpia']
  else:
    if is_room_a(room_letter):
      return [room_letter, 'Limpiando y a la habitación de la derecha']
    else:
      return [room_letter, 'Limpiando y a la habitación de la izquierda']

for i in range(len(asociative_list)):
  history.append(analyze_room(asociative_list, i))

def print_array(array):
  for i in range(len(array)):
    print(f'Caso {i + 1}. {array[i][0]} - {array[i][1]}')

print_array(asociative_list)

print('-----------------------')

print_array(history)
