import unittest
import metar

class TemperatureTest(unittest.TestCase):
  
  def testDefaults(self):
    self.assertEqual( metar.temperature("32").value(), 32.0 )
    self.assertEqual( metar.temperature("32").value("C"), 32.0 )
    self.assertEqual( metar.temperature("32").string(), "32.0 C" )
    self.assertEqual( metar.temperature("32","F").string(), "32.0 F" )
  
  def testInputs(self):
    self.assertEqual( metar.temperature("32").value(), 32.0 )
    self.assertEqual( metar.temperature(32).value(), 32.0 )
    self.assertEqual( metar.temperature(32.0).value(), 32.0 )
    
    self.assertEqual( metar.temperature("32", "c").value(), 32.0 )
    self.assertEqual( metar.temperature("32", "f").value(), 32.0 )
    self.assertEqual( metar.temperature("32", "k").value(), 32.0 )
    
    self.assertEqual( metar.temperature("50", "F").value("c"), 10.0 )
    self.assertEqual( metar.temperature("50", "f").value("C"), 10.0 )
  
  def testErrorChecking(self):
    self.assertRaises( ValueError, metar.temperature, "32C" )
    self.assertRaises( metar.UnitsError, metar.temperature, "32", "J" )
    self.assertRaises( metar.UnitsError, metar.temperature("32").value, "J" )
    self.assertRaises( metar.UnitsError, metar.temperature("32").string, "J" )
  
  def testConversions(self):
    self.assertEqual( metar.temperature("32","F").value("F"), 32.0 )
    self.assertEqual( metar.temperature("32","F").value("C"), 0.0 )
    self.assertEqual( metar.temperature("50","F").value("C"), 10.0 )
    self.assertEqual( metar.temperature("32","F").value("K"), 273.15 )
    
    self.assertEqual( metar.temperature("20","C").value("C"), 20.0 )
    self.assertEqual( metar.temperature("20","C").value("K"), 293.15 )
    self.assertEqual( metar.temperature("20","C").value("F"), 68.0 )
    self.assertEqual( metar.temperature("30","C").value("F"), 86.0 )

    self.assertEqual( metar.temperature("263.15","K").value("K"), 263.15 )
    self.assertEqual( metar.temperature("263.15","K").value("C"), -10.0 )
    self.assertEqual( metar.temperature("263.15","K").value("F"), 14.0 )
    
    self.assertEqual( metar.temperature("10", "C").string("C"), "10.0 C" )
    self.assertEqual( metar.temperature("10", "C").string("F"), "50.0 F" )
    self.assertEqual( metar.temperature("10", "C").string("K"), "283.1 K" )
    
if __name__=='__main__':
  unittest.main()
  