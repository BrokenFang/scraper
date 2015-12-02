nicks = ['Pawel', 'Andrzej', 'Chmiel']

def lower_me(nick_arr):
    for (index, nick) in enumerate(nick_arr):
      nick_arr[index] = nick.lower()
      
lower_me(nicks)
print (nicks)
