"""
This is the people module and supports all the ReST actions for the
PEOPLE collection
"""

# Import datetime module - SYSTEM moule
from datetime import datetime

# Function returning a string of current time
def get_timestamp(): 
  return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
PEOPLE = {
  "Farrell": {
    "fname": "Doug",
    "lname": "Farrell",
    "timestamp": get_timestamp()
  },
  "Brockman": {
    "fname": "Kent",
    "lname": "Brockman",
    "timestamp": get_timestamp()
  },
  "Easter": {
    "fname": "Bunny",
    "lname": "Easter",
    "timestamp": get_timestamp()
  }
}

# A handler for our readAll (GET) people
def read_all():
  """
  This function responds to a request for /api/people with the complete lists of people
  :return:        json string of list of people
  """

  # Create the list of people from our data
  return [PEOPLE[key] for key in sorted(PEOPLE.keys())]