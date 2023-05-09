def show_magicians(list):
    for name in list:
        print(name)

def make_great(list):
    for i in range(len(list)):
        list[i] += " the Great"

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
show_magicians(magician_names)
make_great(magician_names)
show_magicians(magician_names)
