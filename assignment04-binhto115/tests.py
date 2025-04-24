# Name: Binh To
# Date: 11/07/2022
# Github: 113943258

import build_data
import unittest
import hw4

full_data = build_data.getData()

reduced_data = [
    build_data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
    build_data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR'),
    build_data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    build_data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
    build_data.CountyDemographics(
        {'Percent 65 and Older': 19.6,
         'Percent Under 18 Years': 25.6,
         'Percent Under 5 Years': 4.9},
        'Butte County',
        {"Bachelor's Degree or Higher": 17.9,
         'High School or Higher': 89.2},
        {'American Indian and Alaska Native Alone': 1.0,
         'Asian Alone': 0.3,
         'Black Alone': 0.2,
         'Hispanic or Latino': 5.8,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 2.3,
         'White Alone': 96.1,
         'White Alone, not Hispanic or Latino': 90.6},
        {'Per Capita Income': 20995,
         'Persons Below Poverty Level': 15.7,
         'Median Household Income': 41131},
        {'2010 Population': 2891,
         '2014 Population': 2622,
         'Population Percent Change': -9.4,
         'Population per Square Mile': 1.3},
        'ID'),
    build_data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO'),
    build_data.CountyDemographics(
        {'Percent 65 and Older': 18.1,
         'Percent Under 18 Years': 21.6,
         'Percent Under 5 Years': 6.5},
        'Weston County',
        {"Bachelor's Degree or Higher": 17.2,
         'High School or Higher': 90.2},
        {'American Indian and Alaska Native Alone': 1.7,
         'Asian Alone': 0.4,
         'Black Alone': 0.7,
         'Hispanic or Latino': 4.2,
         'Native Hawaiian and Other Pacific Islander Alone': 0.0,
         'Two or More Races': 2.2,
         'White Alone': 95.0,
         'White Alone, not Hispanic or Latino': 91.5},
        {'Per Capita Income': 28764,
         'Persons Below Poverty Level': 11.2,
         'Median Household Income': 55461},
        {'2010 Population': 7208,
         '2014 Population': 7201,
         'Population Percent Change': -0.1,
         'Population per Square Mile': 3.0},
        'WY')
    ]


class TestCases(unittest.TestCase):

    # Part 1
    # test populationTotal
    def test_populationTotal(self):
        list = build_data.getData()
        self.assertEqual(hw4.populationTotal(list), 318857056)

    def test_populationTotal_2(self):
        self.assertEqual(hw4.populationTotal(build_data.getData()), 318857056)

    # Part 2
    # test filterByState
    def test_filterByState_1(self):
        list = build_data.getData()
        length_of_filtered_list = len(hw4.filterByState(list, "CA"))
        self.assertEqual(length_of_filtered_list, 58)

    def test_filterByState_2(self):
        list = build_data.getData()
        length_of_filtered_list = len(hw4.filterByState(list, "MT"))
        self.assertEqual(length_of_filtered_list, 56)

    def test_filterByState_3(self):
        list = build_data.getData()
        length_of_filtered_list = len(hw4.filterByState(list, ""))
        self.assertEqual(length_of_filtered_list, 0)

    # Part 3
    # test populationByEducation
    def test_populationByEducation_1(self):
        list = build_data.getData()
        self.assertEqual(hw4.populationByEducation(list, "Bachelor's Degree or Higher"), 92216021.02199993)

    def test_populationByEducation_2(self):
        list = build_data.getData()
        self.assertEqual(hw4.populationByEducation(list, "High School or Higher"), 274026015.6330008)

    def test_populationByEducation_3(self):
        list = build_data.getData()
        self.assertEqual(hw4.populationByEducation(list, ""), 0)

    # test populationByEthnicity
    def test_populationByEthnicity_1(self):
        list = build_data.getData()
        self.assertEqual(hw4.populationByEthnicity(list, "Black Alone"), 42163174.60799995)

    def test_populationByEthnicity_2(self):
        list = build_data.getData()
        self.assertEqual(hw4.populationByEthnicity(list, "Asian Alone"), 17346856.558999952)

    def test_populationByEthnicity_3(self):
        list = build_data.getData()
        self.assertEqual(hw4.populationByEthnicity(list, "Vietnamese"), 0)

    # test populationBelowPovertyLevel
    def test_populationBelowPovertyLevel_1(self):
        list = build_data.getData()
        self.assertEqual(hw4.populationBelowPovertyLevel(list), 48996488.47399998)

    # Part 4
    # test percenByEducation
    def test_percentByEducation_1(self):
        list = build_data.getData()
        self.assertEqual(hw4.percentByEducation(list, "Bachelor's Degree or Higher"), 28.92)

    def test_percentByEducation_2(self):
        list = build_data.getData()
        self.assertEqual(hw4.percentByEducation(list, "High School or Higher"), 85.94)

    def test_percentByEducation_3(self):
        list = build_data.getData()
        self.assertEqual(hw4.percentByEducation(list, "Middle School or Higher"), 0)

    # test percentByEthnicity
    def test_percentByEthnicity_1(self):
        list = build_data.getData()
        self.assertEqual(hw4.percentByEthnicity(list, "Asian Alone"), 5.44)

    def test_percentByEthnicity_2(self):
        list = build_data.getData()
        self.assertEqual(hw4.percentByEthnicity(list, "White Alone"), 77.36)

    def test_percentByEthnicity_3(self):
        list = build_data.getData()
        self.assertEqual(hw4.percentByEthnicity(list, ""), 0)

    # test percentBelowPovertyLevel
    def test_percentBelowPovertyLevel(self):
        list = build_data.getData()
        self.assertEqual(hw4.percentBelowPovertyLevel(list), 15.37)

    # Part 5
    # test educationGreaterThan
    def test_educationGreaterThan_1(self):
        list = build_data.getData()
        length_list = len(hw4.educationGreaterThan(list, "Bachelor's Degree or Higher", 80))
        self.assertEqual(length_list, 0)

    def test_educationGreaterThan_2(self):
        list = build_data.getData()
        length_list = len(hw4.educationGreaterThan(list, "Bachelor's Degree or Higher", 60))
        self.assertEqual(length_list, 4)

    def test_educationGreaterThan_3(self):
        list = build_data.getData()
        length_list = len(hw4.educationGreaterThan(list, "High School or Higher", 10))
        self.assertEqual(length_list, 3143)

    def test_educationGreaterThan_4(self):
        list = build_data.getData()
        length_list = len(hw4.educationGreaterThan(list, "Middle SChool", 10))
        self.assertEqual(length_list, 0)

    # test educationLessThan
    def test_educationLessThan_1(self):
        list = build_data.getData()
        length_list = len(hw4.educationLessThan(list, "Bachelor's Degree or Higher", 80))
        self.assertEqual(length_list, 3143)

    def test_educationLessThan_2(self):
        list = build_data.getData()
        length_list = len(hw4.educationLessThan(list, "Bachelor's Degree or higher", 5))
        self.assertEqual(length_list, 0)

    def test_educationLessThan_3(self):
        list = build_data.getData()
        length_list = len(hw4.educationLessThan(list, "High School or Higher", 55))
        self.assertEqual(length_list, 5)

    def test_educationLessThan_4(self):
        list = build_data.getData()
        length_list = len(hw4.educationLessThan(list, "Middle School", 0))
        self.assertEqual(length_list, 0)

    # test ethnicityGreaterThan
    def test_ethnicityGreaterThan_1(self):
        list = build_data.getData()
        length_list = len(hw4.ethnicityGreaterThan(list, "Black Alone", 2))
        self.assertEqual(length_list, 1660)

    def test_ethnicityGreaterThan_2(self):
        list = build_data.getData()
        length_list = len(hw4.ethnicityGreaterThan(list, "Two or More Races", 2))
        self.assertEqual(length_list, 889)

    def test_ethnicityGreaterThan_3(self):
        list = build_data.getData()
        length_list = len(hw4.ethnicityGreaterThan(list, "White Alone", 80))
        self.assertEqual(length_list, 2364)

    def test_ethnicityGreaterThan_4(self):
        list = build_data.getData()
        length_list = len(hw4.ethnicityGreaterThan(list, "Chinese", 0))
        self.assertEqual(length_list, 0)

    # test ethnicityLessThan
    def test_ethnicityLessThan_1(self):
        list = build_data.getData()
        length_list = len(hw4.ethnicityLessThan(list, "Hispanic or Latino", 22))
        self.assertEqual(length_list, 2810)

    def test_ethnicityLessThan_2(self):
        list = build_data.getData()
        length_list = len(hw4.ethnicityLessThan(list, "Native Hawaiian and Other Pacific Islander Alone", 5))
        self.assertEqual(length_list, 3138)

    def test_ethnicityLessThan_3(self):
        list = build_data.getData()
        length_list = len(hw4.ethnicityLessThan(list, "Asian Alone", 1))
        self.assertEqual(length_list, 2088)

    def test_ethnicityLessThan_4(self):
        list = build_data.getData()
        length_list = len(hw4.ethnicityLessThan(list, "White", 0))
        self.assertEqual(length_list, 0)

    # test belowPovertyLevelGreaterThan
    def test_belowPovertyGreaterThan_1(self):
        list = build_data.getData()
        length_list = len(hw4.belowPovertyLevelGreaterThan(list, 50))
        self.assertEqual(length_list, 1)

    def test_belowPovertyGreaterThan_2(self):
        list = build_data.getData()
        length_list = len(hw4.belowPovertyLevelGreaterThan(list, 0.5))
        self.assertEqual(length_list, 3143)

    def test_belowPovertyGreaterThan_3(self):
        list = build_data.getData()
        length_list = len(hw4.belowPovertyLevelGreaterThan(list, 20))
        self.assertEqual(length_list, 820)

    def test_belowPovertyGreaterThan_4(self):
        list = build_data.getData()
        length_list = len(hw4.belowPovertyLevelGreaterThan(list, 30))
        self.assertEqual(length_list, 114)

    # test belowPovertyLevelLessThan
    def test_belowPovertyLessThan_1(self):
        list = build_data.getData()
        length_list = len(hw4.belowPovertyLevelLessThan(list, 30))
        self.assertEqual(length_list, 3027)

    def test_belowPovertyLessThan_2(self):
        list = build_data.getData()
        length_list = len(hw4.belowPovertyLevelLessThan(list, 10))
        self.assertEqual(length_list, 427)

    def test_belowPovertyLessThan_3(self):
        list = build_data.getData()
        length_list = len(hw4.belowPovertyLevelLessThan(list, 20.6))
        self.assertEqual(length_list, 2390)

    def test_belowPovertyLessThan_4(self):
        list = build_data.getData()
        length_list = len(hw4.belowPovertyLevelLessThan(list, 2))
        self.assertEqual(length_list, 1)


if __name__ == '__main__':
    unittest.main()
