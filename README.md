# Project Title
This program works with the metro transit api system and provides data about the next bus for a particular route stop and direction

## Getting Started
Clone this project on to your own machine
From the root directory, from the command line run 

Macs
python3 -m venv env
source env/bin/activate

Windows PC
python -m venv env
env\script\activate

Than to install the requirements run
pip install -r requirements.txt

Now the program is ready to be ran
It is designed to be run from the command prompt given 3 arguments
For example 
python main.py "6 - U of M - Hennipen - Xerxes - France -Southdale" "Southdale Transit Center" "south"
Will return something like "5 minutes until next bus/rail"

## Testing
To run the tests run
python testBus.py from the command prompt
The tests test the get route, get direction and get stop by passing in data
and comparing it's return to a correct response.
There is also a test for the time difference where a date object that emulates a now time
and an example time response from the api is passed in, it confirms it produces the right difference in times.

Here is a link to the metro transit api help page
https://svc.metrotransit.org/NexTrip/help

## Author
Anthony Covin
https://github.com/tonyspicervovin




