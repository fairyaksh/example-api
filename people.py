"""
This is the people module and supports all the ReST actions for the
PEOPLE collection
"""

# Import datetime module - SYSTEM moule
from datetime import datetime

# 3rd party modules
from flask import make_response, abort

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

def read_one(lname):
  """
  This function responds to a request for /api/people/{lname}
  with one matching person from people

  :param lname:   last name of person to find
  :return:        person matching last name
  """
  # Does this person exist in people?
  if lname in PEOPLE:
    person = PEOPLE.get(lname)

  # Otherwise, nope, not found
  else:
    abort(
      404, "Person with last name {lname} not found".format(lname=lname)
    )
  
  return person

def create(person):
  """
  This function creates a new person in the people structure
  based on the passed in person data

  :param person:    person to create in people structure
  :return:          201 on success, 406 on person exists
  """
  lname = person.get("lname", None)
  fname = person.get("fname", None)

  # Does this person exist already?
  if lname not in PEOPLE and lname is not None:
    PEOPLE[lname] = {
      "lname": lname,
      "fname": fname,
      "timestamp": get_timestamp(),
    }
    return make_response(
      "{lname} successfully created".format(lname = lname), 201
    )

  # Otherwise, they exist, that's an error
  else:
    abort(
      406, 
      "Person with last name {lname} already exists".format(lname = lname)
    )

def update(lname, person):
  """
  This function updates an existing person in the people structure

  :param lname: last name of person to update in the people structure
  :param person: person to update
  :return: updated person structure
  """
  # Does this person exist in people?
  if lname in PEOPLE:
    PEOPLE[lname]["fname"] = person.get("fname")
    PEOPLE[lname]["timestamp"] = get_timestamp()

    return PEOPLE[lname]
  
  # Otherwise, nope, that's an error
  else:
    abort(
      404, "Person with last name {lname} not found".format(lname = lname)
    )

