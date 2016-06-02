import unittest
import if97

class testPT( unittest.TestCase):
    def setUp(self):
        self.tab1=[[3, 300, 0.0010021516796866943, 115.3312730214384, 112.32481798237833, 0.39229479240262427, 4.173012184067783, 1507.7392096690312],
                      [80, 300, 0.0009711808940216297, 184.14282773425438, 106.44835621252402,
                       0.36856385239848066, 4.010089869646331, 1634.6905431116586],
                      [3, 500, 0.001202418003378339, 975.5422390972251, 971.9349850870901, 2.58041912005181, 4.6558068221112086, 1240.7133731017252]]
    def test_SpecificVolume(self):
        for item in self.tab1:
            self.assertAlmostEqual(if97.SpecificVolume(item[0], item[1]), item[2])

    def test_SpecificEnthalpy(self):
        for item in self.tab1:
            self.assertAlmostEqual(if97.SpecificEnthalpy(item[0], item[1]), item[3])

    def test_SpecificInternalEnergy(self):
        for item in self.tab1:
            self.assertAlmostEqual(if97.SpecificInternalEnergy(item[0], item[1]), item[4])

    def test_SpecificEntropy(self):
        for item in self.tab1:
            self.assertAlmostEqual(if97.SpecificEntropy(item[0], item[1]), item[5])

    def test_SpecificIsochoricHeatCapacity(self):
        for item in self.tab1:
            self.assertAlmostEqual(if97.SpecificIsobaricHeatCapacity(item[0], item[1]), item[6])

    def test_SpeedOfSound(self):
        for item in self.tab1:
            self.assertAlmostEqual(if97.SpeedOfSound(item[0], item[1]), item[7])


class testphs3(unittest.TestCase):
    def setUp(self):
        self.tab2=[[1700,3.8,2.555703246e1],[2000,4.2,4.540873468e1],[2100,4.3,6.078123340e1]]
    def test_Pressure(self):
        for item in self.tab2:
            self.assertAlmostEqual(if97.supplement_phs_3a(item[0], item[1]),item[2])
 
def test_suite():
    def toSuite(testClass):
        return unittest.makeSuite(testClass)
    suite = unittest.TestSuite()
    suite.addTest((toSuite(testPT), toSuite(testphs3)))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')