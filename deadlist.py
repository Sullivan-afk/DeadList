#
# Program to list Grateful Dead shows from the 1960s.
#

import os.path

from shows import Shows
from subprocess import call


def clear():
  """Clear screen according to our specific operation system"""

  # Call out to operating system's clear command
  exit_code = call('clear' if os.name == 'posix' else 'cls')

  if (exit_code != 0):
    raise Exception("Unexpected clear response code: {0}".format(exit_code))


# Login to Grateful Dead 1960s show listing
def login():
  shows = Shows(show_files=[
    '1965.yaml', '1966.yaml', '1967.yaml', '1968.yaml', '1969.yaml'
  ])

  clear()

  # Input loop
  while True:
    print('\nChoose an action by typing a number:\n')
    print('  1 - List shows')
    print('  2 - Remove show')
    print('  3 - Count shows')
    print('  5 - Quit')
    print()

    try:
      action = int(input('> '))
      clear()

      if (action == 1):
        print(shows)
      elif (action == 2):
        date = input("Input a date (like 1967/01/06): ")

        try:
          shows.remove(date)
          print("\nShow for {0} has been removed.".format(date))
        except ValueError as error:
          print()
          print(error)
      elif (action == 3):
        print("\nThere are '{0}' shows.".format(shows.count()))
      elif (action == 5):
        break
      else:
        print("There is no '{0}' as an option; try again.".format(action))
    except ValueError as error:
      clear()
      print(error)
