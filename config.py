#
# Script to create main program's configuration file: deadlist.ini
#
# It takes input from the user and creates a configuration object which
# is stored in a file.
#

import base64
import configparser
import sys
import os

from time import sleep
from subprocess import call


def clear():
  """Clear screen according to our specific operation system"""

  # Call out to operating system's clear command
  exit_code = call('clear' if os.name == 'posix' else 'cls')

  if (exit_code != 0):
    raise Exception("Unexpected clear response code: {0}".format(exit_code))


def create_config_file():
  """Creates a config file for the main program to use"""

  print('This is the first time you have run this program.\n')

  # Get password from user input and encode it
  pw_input = input("Enter what you would like to use as a password: ")
  pw_bytes = pw_input.encode("ascii")
  encoded_pw = base64.b64encode(pw_bytes).decode()  # Store as encoded string

  # Get number of allowed login attempts
  attempts = input("How many login attempts do you want to allow? ")

  # Create configuration
  config = configparser.ConfigParser()
  config['DEFAULT'] = {'password': encoded_pw, 'max_logins': int(attempts)}

  try:
    # Write configuration to a config file
    with open('deadlist.ini', 'w') as config_file:
      config.write(config_file)
      config_file.close()

    # Tell user program has completed successfully
    print('\nYour configuration has been written to a .ini file\n')
    print('Starting the main program in five seconds...')

    # Wait five seconds before clearing the screen
    sleep(5)
    clear()
  except configparser.Error as error:
    sys.exit(error)
