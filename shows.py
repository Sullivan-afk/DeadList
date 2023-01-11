
import yaml

class Shows:
  """A collection of Grateful Dead shows"""

  dates = []
  venues = []
  cities = []
  states = []
  countries = []

  def __init__(self, show_files):
    """
    Parameters
    ----------
    show_files : list
        A list of Grateful Dead YAML file names
    """

    show_count = len(show_files)

    # Loop through all supplied YAML files
    for index in range(show_count):
      with open(show_files[index], 'r') as yaml_file:
        shows = yaml.safe_load(yaml_file) # Dictionary of shows

        while True: # Loop through all shows in the YAML file
          try:
            showTuple = shows.popitem() # Tuple of a single show
            showDate = showTuple[0]
            showData = showTuple[1]

            # Add shows to list in synchronized way
            self.dates.append(showDate)
            self.venues.append(showData[':venue'])
            self.cities.append(showData[':city'])
            self.states.append(showData[':state'])
            self.countries.append(showData[':country'])
          except KeyError:
            break

  def count(self):
    """A function that counts the number of shows"""
    return len(self.dates)

  def add(self, date, venue, city, state, country):
    """Adds a new Grateful Dead show
    
    Parameters
    ----------
    date : str
        A show's date
    venue : str
        A show's venue
    city : str
        A show's city
    state : str
        A show's state
    country : str
        A show's country
    """
    
    count = self.dates.count(date)

    # Check that not more than one show for a date exists
    if count > 1:
      raise Exception("More than one show on date '{0}' exists".format(date))
    # If one show exists, remove it before adding new one
    elif count == 1:
      self.remove(date)

    # Add new show information
    self.dates.append(date)
    self.venues.append(venue)
    self.cities.append(city)
    self.states.append(state)
    self.countries.append(country)

  # Remove show for the supplied date
  def remove(self, date):
    """Removes Grateful Dead show for the supplied date
    
    Parameters
    ----------
    date : str
        A date of a show to remove
    """

    # Find index of supplied date
    index = self.dates.index(date)

    # Remove values for supplied date's show
    self.dates.pop(index)
    self.venues.pop(index)
    self.cities.pop(index)
    self.states.pop(index)
    self.countries.pop(index)

  def to_list(self):
    list = [] # TODO
    return list

  def __str__(self):
    """Returns a string version of the Shows object"""

    show_count = len(self.dates)
    display = ''

    for index in range(show_count):
      date = self.dates[index]
      venue = self.venues[index]
      city = self.cities[index]
      state = self.states[index]
      country = self.countries[index]

      display += f"{date} [ {venue}, {city}, {state}, {country} ]\n"

    return display.strip()
