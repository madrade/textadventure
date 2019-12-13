class Room:
    def __init__(self, name: str, description: str):
        self._name = name
        self._description = description
        self._exits = {}
        self._items = []

    def add_exit(self, name, room):
        if isinstance(room, Room):
            self._exits[name] = room
        else:
            raise TypeError('Not a Room object.')

    def __str__(self) -> str:
        # room description first
        output = f'{self._description}\n\n'

        #
        if len(self._exits) == 0:
            output += 'Z tejto miestnosti sa nedá nikam dostať.'
        else:
            # list of exits
            output += 'Možné východy:\n\t'
            output += '\n\t'.join(self._exits.keys())

        output += '\n'

        # list items in room
        if len(self._items) == 0:
            output += 'Nevidíš tu nič zaujímavé.'
        else:
            output += 'Vidíš:\n'
            for item in self._items:
                output += f'\t{item._name}\n'

        return output

    def __repr__(self):
        return f'repr: "{self._name}". {self._description}'


class DeadRoom(Room):
    pass