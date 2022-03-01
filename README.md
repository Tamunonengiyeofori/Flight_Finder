# Flight_Finder
This program crosschecks flights prices from an google excel sheet containing flight locations and finds a cheaper flight.
It makes use of three API's;
A) The Sheety API for editing a google sheet using HTTP CRUD methods 
B) The Tequila flight API from kiwi.com to get the iataCodes for all locations in google sheet and search for flights to different locations worldwide.  
C) The Twilio API to send a customized messages to the user if a cheaper flight is found.

It also uses the SMTP module to send customized emails to all users if a cheaper flight is found.

It is built using OOP with python and has four classes;
A) Flight Search Class: This class gets flight destination codes and searches for flights.
B) Flight Data Class: This class initializes all the flight data/information.
C) Data Manager Class: This class handles all the data from the user i.e fetches all user data, updates destination codes, fetches all customer details.
D) Notification Manager Class: This class sends messages to all users by email and SMS.
