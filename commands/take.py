from commands.command import Command


class Take(Command):
    def __init__(self):
        super().__init__('vezmi', 'vezme predmet z miestnosti a vloží si ho do batohu.')

    def exec(self, context):
        # ak nebol zadany prikaz s nazvom predmetu
        if len(self._params) == 0:
            print('Neviem, aký predmet chceš vziať.')
            return

        # zisti, ci sa predmet nachadza v miestnosti
        for item in context.current_room._items:
            if item._name == self._params:
                context.backpack.append(item)
                context.current_room._items.remove(item)
                print(f'Do batôžku si si vložil {item._name}.')
                break
        else:
            print('Taký predmet tu nikde nevidím.')
