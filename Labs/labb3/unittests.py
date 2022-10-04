import unittest
from Tests import TestGeometry, TestCircle, TestCube, TestRectangle, TestSphere


def main() -> None:
    """
    Main function for running all tests in the project and printing the results.
    """
    print(" --- TestGeometry --- ")
    # run unittests in TestGeometri.py
    unittest.main(module=TestGeometry, exit=False)

    print(" --- TestCircle --- ")

    # run unittests in TestCircle.py
    unittest.main(module=TestCircle, exit=False)

    print(" --- TestCube --- ")

    # run unittests in TestCube.py
    unittest.main(module=TestCube, exit=False)

    print(" --- TestRectangle --- ")

    # run unittests in TestRectangle.py
    unittest.main(module=TestRectangle, exit=False)

    print(" --- TestSphere --- ")

    # run unittests in TestSphere.py
    unittest.main(module=TestSphere, exit=False)


if __name__ == "__main__":
    main()
