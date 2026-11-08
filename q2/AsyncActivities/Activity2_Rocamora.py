# 1. Answer the following questions:
#   a. What is duck typing, as explained in the video?
#         From the video, duck typing is a concept where if an object has properties and methods that 
#        are the same as another, then it can be treated as the same type of object, even if it shouldn't be.
#   b. What did the Car class need to have so it could work inside the same loop as Dog 
#      and Cat, even if it does not inherit from the Animal class?
#       The car needed to have the same methods like .speak instead of .honk so that the for loop could treat it as an animal.
#      When the for loop called .alive, it needed to have a alive status too so whether it was "dead" or "alive" it could be 
#      treated as an part of the animals.

class Car:
    def  move(self):
        print("The car drives on the road.")

class Boat:
    def  move(self):
        print("The boat sails on the water.")

class Drone:
    def  move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
        vehicle.move()

lamborghini = Car()
yacht = Boat()
amazonDrone = Drone()

start_trip(lamborghini)
start_trip(yacht)
start_trip(amazonDrone)