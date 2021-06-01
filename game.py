#!/usr/bin/env python3

from helper import show_room
from commands import commands as list_of_commands
import states


def parse(context, line):
    for cmd in context['commands']:
        for alias in cmd['aliases']:
            if line.startswith(alias):
                context['params'] = line.replace(alias, '').strip()
                return cmd

    return None


def main():
    # game initialization
    context = {
        'state': states.STATE_PLAYING,
        'inventory': [],
        'inventory_capacity': 2,
        'room': None
    }

    context['inventory'].append({
        'name': 'ZAPALKY',
        'description': 'No zápalky. 4 kusy. Nepoužité. Krbové.',
        'features': ['movable', 'usable']
    })

    line = None
    context['room'] = 'zahradka'

    context['world'] = {
        'zahradka': {
            'name': 'zahradka',
            'description': 'Znacne zanedbana a rozsiahla zahradka.',
            'exits': {
                'north': 'tmava miestnost',
            },
            'items': [
                {
                    'name': 'MOTYKA',
                    'description': 'Bezny pracovny nastroj, v nespravnych rukach zabija.',
                    'features': ['movable']
                }
            ]
        },

        'zachod': {
            'name': 'zachod',
            'description': 'Smradlava a nehygienicka miestnost, do ktorej sa bojis vstupit.',
            'exits': {
                'west': 'tmava miestnost',
            },
            'items': [
                {
                    'name': 'ZVON',
                    'description': 'Vhodny na cistenie zachoda, pravdepodobne nikdy nebol pouzity.',
                    'features': ['movable']
                }
            ]
        },

        'diera': {
            'name': 'diera',
            'description': 'Necakana jama ako z Mlcania jahniat. Spadol do nej a kosti pod tvojimi nohami ti napovedaju, ze z nej niet uniku.',
            'exits': {},
            'items': [
                {
                    'name': 'KOSTI',
                    'description': 'Uplne zbytocne pozostatky nestastnika s rovnakym osudom, ako je ten tvoj, ale mozes s nimi vyskriabat svoje meno na stenu diery.',
                    'features': ['movable']
                }
            ]
        },

        'tmava miestnost': {
            'name': 'tmava miestnost',
            'description': 'Stojíš v tmavej miestnosti. Zrejme sa tu už dlho neupratovalo, lebo do nosa sa ti ftiera zepeklitý zápach niečoho zdochnutého. Ani len svetlo nepreniká cez zadebnené okná. I have a bad feeling about this place, ako by klasik povedal.',
            'exits': {
                'south': 'zahradka',
                'east': 'zachod',
                'west': 'diera'
            },
            'items': [
                {
                    'name': 'DVERE',
                    'description': 'Velke masivne drevene dvere. Okrem toho su aj zamknute',
                    'features': []
                },
                {
                    'name': 'KYBEL',
                    'description': 'Hrdzavý kýbel s obsahom bližšie nešpecifikovaným, ale zrejme to bude len voda.',
                    'features': ['usable', 'movable']
                },
                {
                    'name': 'NOVINY',
                    'description': 'Staré suché Nové tajmsy z roku pána 1998. Z titulky rozpoznávaš len Vladimíra. To je teda veľký kus h... histórie.',
                    'features': ['usable', 'movable']
                },
                {
                    'name': 'NOZIK',
                    'description': 'Síce zhrdzavený, ale stará klasika - nožík rybka.',
                    'features': ['movable']
                },
            ]
        }
    }
    context['commands'] = list_of_commands


    # welcome
    print(' _____                            ____                       ')
    print('| ____|___  ___ __ _ _ __   ___  |  _ \ ___   ___  _ __ ___  ')
    print("|  _| / __|/ __/ _` | '_ \ / _ \ | |_) / _ \ / _ \| '_ ` _ \ ")
    print('| |___\__ \ (_| (_| | |_) |  __/ |  _ < (_) | (_) | | | | | |')
    print('|_____|___/\___\__,_| .__/ \___| |_| \_\___/ \___/|_| |_| |_|')
    print('                    |_|                     (c) mirek 2021   ')
    print()

    name = context['room']
    room = context['world'][name]
    show_room(room)

    # game loop
    while context['state'] == states.STATE_PLAYING:
        # parsovanie vstupu
        line = input('> ').upper().strip()

        cmd = parse(context, line)
        if cmd is None:
            print('Taký príkaz nepoznám.')
        else:
            cmd['exec'](context)

    print('Created by (c)2021 mirek')


if __name__ == '__main__':
    main()
