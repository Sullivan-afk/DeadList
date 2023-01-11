#
# Program that allows searching Grateful Dead shows from the 1960s.
#

import base64
import config
import os.path
import configparser
import deadlist

# Create configuration file, if needed
if not os.path.isfile('deadlist.ini'):
  config.create_config_file()

# Read configuration file
config = configparser.ConfigParser()
config.read('deadlist.ini')

# Read configuration values
max_attempts = int(config['DEFAULT']['max_logins'])
encoded_pw = config['DEFAULT']['password']
decoded_pw = base64.b64decode(encoded_pw).decode("utf-8")

# Give user several attempts to supply password
for count in range(max_attempts):
  if (count < max_attempts):
    pw_input = input("Enter the password: ")

    if pw_input == decoded_pw:
      deadlist.login() # Login to the DeadList program
      break # Stop the password input loop
    else:
      # Keep looping until the last number in our range of max_attempts
      if (count != max_attempts):
        attempts_left = (max_attempts - 1) - count # -1 because 0-based

        print('Password incorrect! Number of tries left: {0}\n'.format(
          attempts_left))

        if (attempts_left == 0):
          print("Sorry you failed to login")
