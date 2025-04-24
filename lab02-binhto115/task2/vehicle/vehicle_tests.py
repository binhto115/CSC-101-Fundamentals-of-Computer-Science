import unittest
import vehicle
class VehicleTests(unittest.TestCase):
   def test_vehicle(self):
        # Add code here.
        # 1) Create a Vehicle with values of your choice.
        # 2) Use assertEqual or assertAlmostEqual on each field in
        #    the new Vehicle to verify that it holds the expected value.
      vehiclecheck = vehicle.Vehicle(4, "12 gallons", 4, "roof")
      self.assertEqual(vehiclecheck.wheels, 4)
      self.assertEqual(vehiclecheck.fuelremaining, "12 gallons")
      self.assertEqual(vehiclecheck.doors, 4)
      self.assertEqual(vehiclecheck.roof, "roof")
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

