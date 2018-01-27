import plane
import unittest

class TestLand(unittest.TestCase):
    """
    Test the land function from the plane library
    """

    def test_status(self):
        """
        It returns the current status ('flying' by default)
        """
        my_plane = plane.Plane()
        result = my_plane.status
        self.assertEqual(result, 'flying')


    def test_land(self):
        """
        It changes the plane status to 'landed'
        """
        my_plane = plane.Plane()
        my_plane.land()
        result = my_plane.status
        self.assertEqual(result, 'landed')

if __name__ == '__main__':
    unittest.main()
