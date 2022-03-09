import unittest
from TestingWithPython import eat,nap

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        self.assertEqual(
            eat("brocolli",ishealthy=True),
            "I am true and healthy"
        )
    def test_eat_unhealthy(self):
        self.assertEqual(
            eat("pizza",ishealthy=False),
            "I am not true"
        )
    
    def test_short_nap(self):
    	self.assertEqual(
    		nap(1),
    		"I'm feeling refreshed after my 1 hour nap"
    	)
    
    def test_long_nap(self):
    	self.assertEqual(
    		nap(3),
    		"nah nah 3hour sleep is not good"
    	)

if __name__ == '__main__':
    unittest.main()