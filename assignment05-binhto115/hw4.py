# Name: Binh To
# Date: 11/07/2022
# Github: 113943258


from typing import List
import build_data

# Part 1:
CountyDemographics = build_data.CountyDemographics


def populationTotal(p: List[CountyDemographics]) -> int:
    """This function takes in the list of county demographics
    and return the total population of all 2014 populations of all
    the counties in the list """
    year_2014_population = []
    for i in p:
        population = i.population
        if "2014 Population" in population:
            population_num = population["2014 Population"]
            year_2014_population.append(population_num)
    sum_up = sum(year_2014_population)
    return sum_up


# Part 2:
def filterByState(p1: List[CountyDemographics], p2: str) -> List[CountyDemographics]:
    """This function filters the county demographics list by state
     and return a list of county demographics of the inputted state"""
    filtered_population_list = []
    for i in p1:
        state_name = i.state
        if state_name == p2:
            filtered_population_list.append(i)
        elif state_name == "":
            return []
    return filtered_population_list


# Part 3:
def populationByEducation(p1: List[CountyDemographics], p2: str) -> float:
    """This function return the total number of 2014 population based on education.
    It will return zero if the provided education level isn't in the provided data"""
    list_of_results = []
    for i in p1:
        year_2014_populations = i.population
        education = i.education
        if "2014 Population" in year_2014_populations and p2 in education:
            population_num = year_2014_populations["2014 Population"]
            education_num = education[p2]
            result = population_num * (education_num / 100)
            list_of_results.append(result)
        elif "2014 Population" in year_2014_populations and p2 not in education:
            return 0
    total_results = sum(list_of_results)
    return total_results


def populationByEthnicity(p1: List[CountyDemographics], p2: str) -> float:
    """This function will return the total number of 2014 populations of all counties based on the ethnicity.
     It will return 0 if the ethnicity you input is not in the provided data"""
    list_of_results = []
    for i in p1:
        year_2014_population = i.population
        ethnicities = i.ethnicities
        if "2014 Population" in year_2014_population and p2 in ethnicities:
            population_2014_num = year_2014_population["2014 Population"]
            ethnicities_num = ethnicities[p2]
            result = population_2014_num * (ethnicities_num / 100)
            list_of_results.append(result)
        elif "2014 Population"  in year_2014_population and p2 not in ethnicities:
            return 0
    sum_of_results = sum(list_of_results)
    return sum_of_results


def populationBelowPovertyLevel(p: List[CountyDemographics]) -> float:
    """This function returns the total population of all counties
     below the poverty level"""
    filtered_list_of_poverty_population = []
    for i in p:
        year_2014_population = i.population
        poverty_level = i.income
        if "2014 Population" in year_2014_population:
            population_Below_Poverty = year_2014_population["2014 Population"]
            poverty_percentage = poverty_level["Persons Below Poverty Level"]
            percentage_of_poverty_2014_population = population_Below_Poverty * (poverty_percentage / 100)
            filtered_list_of_poverty_population.append(percentage_of_poverty_2014_population)
    total_poverty = sum(filtered_list_of_poverty_population)
    return total_poverty


# Part 4:
def percentByEducation(p1: List[CountyDemographics], p2: str) -> float:
    """This function returns the total 2014 subpopulation as a percentage
     of the total 2014 population of the provided data based on the education level"""
    total_2014_population = []
    list_of_result = []
    for i in p1:
        year_2014_population = i.population
        education = i.education
        if "2014 Population" in year_2014_population and p2 in education:
            population_num = year_2014_population["2014 Population"]
            education_num = education[p2]
            result = population_num * (education_num / 100)
            total_2014_population.append(population_num)
            list_of_result.append(result)
        elif "2014 Population" in year_2014_population and p2 not in education:
            return 0
    sum_of_2014_population = sum(total_2014_population)
    sum_of_result = sum(list_of_result)
    population_as_percentage = (sum_of_result / sum_of_2014_population) * 100
    return population_as_percentage


def percentByEthnicity(p1: List[CountyDemographics], p2: str) -> float:
    """This function returns the 2014 subpopulation as a percentage
    of the total 2014 population based on ethnicity"""
    total_2014_population_list = []
    total_2014_ethnicity_list = []
    for i in p1:
        year_2014_population = i.population
        ethnicity = i.ethnicities
        if "2014 Population" in year_2014_population and p2 in ethnicity:
            population_num = year_2014_population["2014 Population"]
            ethnicity_num = ethnicity[p2]
            result = population_num * (ethnicity_num / 100)
            total_2014_population_list.append(population_num)
            total_2014_ethnicity_list.append(result)
        elif "2014 Population" in year_2014_population and p2 not in ethnicity:
            return 0
    total_2014_population = sum(total_2014_population_list)
    total_2014_ethnicity = sum(total_2014_ethnicity_list)
    ethnicity_as_percentage = (total_2014_ethnicity / total_2014_population) * 100
    return ethnicity_as_percentage


def percentBelowPovertyLevel(p1: List[CountyDemographics]) -> float:
    """This function returns the 2014 subpopulation under poverty level as a percentage
     of the total 2014 population of the provided data"""
    total_2014_population_list = []
    total_2014_poverty_list = []
    for i in p1:
        year_2014_population = i.population
        poverty_level = i.income
        if "2014 Population" in year_2014_population:
            population = year_2014_population["2014 Population"]
            poverty = poverty_level["Persons Below Poverty Level"]
            total_2014_population_list.append(population)
            result = population * (poverty / 100)
            total_2014_poverty_list.append(result)
    total_2014_population = sum(total_2014_population_list)
    total_2014_poverty = sum(total_2014_poverty_list)
    poverty_as_percentage = (total_2014_poverty / total_2014_population) * 100
    return poverty_as_percentage


# Part 5:
def educationGreaterThan(p1: List[CountyDemographics], p2: str, p3: float) -> List[CountyDemographics]:
    """This functions returns a list of county demographics that contains higher threshold value
    than inputted threshold value"""
    education_greater_than_list = []
    for i in p1:
        age = i.age
        county = i.county
        education = i.education
        ethnicity = i.ethnicities
        income = i.income
        year_2014_population = i.population
        state = i.state
        if p2 in education and education[p2] > p3:
            var_county_demographics = CountyDemographics(age, county, education, ethnicity,
                                                         income, year_2014_population, state)
            education_greater_than_list.append(var_county_demographics)
        elif p2 not in education:
            return []
    return education_greater_than_list


def educationLessThan(p1: List[CountyDemographics], p2: str, p3: float) -> List[CountyDemographics]:
    """This functions returns a list of county demographics that contains higher threshold value
    of education than the inputted threshold value"""
    education_less_than_list = []
    for i in p1:
        age = i.age
        county = i.county
        education = i.education
        ethnicity = i.ethnicities
        income = i.income
        population = i.population
        state = i.state
        if p2 in education and education[p2] < p3:
            var_county_demographics = CountyDemographics(age, county, education,
                                                         ethnicity, income,
                                                         population,
                                                         state)
            education_less_than_list.append(var_county_demographics)
        elif p2 not in education:
            return []
    return education_less_than_list


def ethnicityGreaterThan(p1: List[CountyDemographics], p2: str, p3: float) -> List[CountyDemographics]:
    """This function returns a list of county demographics in which the threshold
    value of ethnicity is greater than the inputted threshold value"""
    ethnicity_greater_than_list = []
    for i in p1:
        age = i.age
        county = i.county
        education = i.education
        ethnicity = i.ethnicities
        income =i.income
        population = i.population
        state = i.state
        if p2 in ethnicity and ethnicity[p2] > p3:
            var_county_demographics = CountyDemographics(age, county, education,
                                                         ethnicity, income, population,
                                                         state)
            ethnicity_greater_than_list.append(var_county_demographics)
        elif p2 not in ethnicity:
            return []
    return ethnicity_greater_than_list


def ethnicityLessThan(p1: List[CountyDemographics], p2: str, p3: float) -> List[CountyDemographics]:
    """This function returns a list of county demographics in which the threshold
    value of ethnicity is less than the inputted threshold value"""
    ethnicity_less_than_list = []
    for i in p1:
        age = i.age
        county = i.county
        education = i.education
        ethnicity = i.ethnicities
        income = i.income
        population = i.population
        state = i.state
        if p2 in ethnicity and ethnicity[p2] < p3:
            var_county_demographics = CountyDemographics(age, county, education,
                                                         ethnicity, income, population,
                                                         state)
            ethnicity_less_than_list.append(var_county_demographics)
        elif p2 not in ethnicity:
            return []
    return ethnicity_less_than_list


def belowPovertyLevelGreaterThan(p1: List[CountyDemographics], p2: float) -> List[CountyDemographics]:
    """This function returns a list of county demographics in which the threshold value of income
    is greater than the inputted threshold value"""
    below_poverty_level_greater_than_list = []
    for i in p1:
        age = i.age
        county = i.county
        education = i.education
        ethnicity = i.ethnicities
        income = i.income
        population = i.population
        state = i.state
        if "Persons Below Poverty Level" in income and income["Persons Below Poverty Level"] > p2:
            var_county_demographics = CountyDemographics(age, county, education,
                                                         ethnicity, income, population,
                                                         state)
            below_poverty_level_greater_than_list.append(var_county_demographics)
    return below_poverty_level_greater_than_list


def belowPovertyLevelLessThan(p1: List[CountyDemographics], p2: float) -> List[CountyDemographics]:
    """This function returns a list of country demographics in which the threshold value
    of income is less than the inputted threshold value"""
    below_poverty_level_less_than_list = []
    for i in p1:
        age = i.age
        county = i.county
        education = i.education
        ethnicity = i.ethnicities
        income = i.income
        population = i.population
        state = i.state
        if "Persons Below Poverty Level" in income and income["Persons Below Poverty Level"] < p2:
            var_county_demographics = CountyDemographics(age, county, education, ethnicity,
                                                         income, population, state)
            below_poverty_level_less_than_list.append(var_county_demographics)
    return below_poverty_level_less_than_list


# Population of a state function:
def populationState(p1: List[CountyDemographics], p2: str) -> int:
    """This function takes in the list of county demographics
    and return the total population of a state's 2014 population of all
    the counties in the list """
    year_2014_population = []
    for i in p1:
        population = i.population
        state = i.state
        if "2014 Population" in population and p2 in state:
            population_num = population["2014 Population"]
            year_2014_population.append(population_num)
    sum_up = sum(year_2014_population)
    return sum_up


# Population of a state based on education
def percentByEducationState(p1: List[CountyDemographics], p2: str, p3: str) -> float:
    """This function returns the total 2014 subpopulation as a percentage
     of the total 2014 population of a state based on the education level"""
    total_2014_population = []
    list_of_result = []
    for i in p1:
        year_2014_population = i.population
        education = i.education
        state = i.state
        if "2014 Population" in year_2014_population and p2 in education and p3 in state:
            population_num = year_2014_population["2014 Population"]
            education_num = education[p2]
            result = population_num * (education_num / 100)
            total_2014_population.append(population_num)
            list_of_result.append(result)
        elif "2014 Population" in year_2014_population and p2 not in education and p3 not in state:
            return 0
    sum_of_2014_population = sum(total_2014_population)
    sum_of_result = sum(list_of_result)
    population_as_percentage = (sum_of_result / sum_of_2014_population) * 100
    return population_as_percentage


# Population as a percentage based on ethnicities of a state
def percentByEthnicityState(p1: List[CountyDemographics], p2: str, p3: str) -> float:
    """This function returns the 2014 subpopulation as a percentage
    of the total 2014 population of a state based on ethnicity"""
    total_2014_population_list = []
    total_2014_ethnicity_list = []
    for i in p1:
        year_2014_population = i.population
        ethnicity = i.ethnicities
        state = i.state
        if "2014 Population" in year_2014_population and p2 in ethnicity and p3 in state:
            population_num = year_2014_population["2014 Population"]
            ethnicity_num = ethnicity[p2]
            result = population_num * (ethnicity_num / 100)
            total_2014_population_list.append(population_num)
            total_2014_ethnicity_list.append(result)
        elif "2014 Population" in year_2014_population and p2 not in ethnicity and p3 not in state:
            return 0
    total_2014_population = sum(total_2014_population_list)
    total_2014_ethnicity = sum(total_2014_ethnicity_list)
    ethnicity_as_percentage = (total_2014_ethnicity / total_2014_population) * 100
    return ethnicity_as_percentage


# Population as percentage based on income of a state:
def percentBelowPovertyLevelState(p1: List[CountyDemographics], p2: str) -> float:
    """This function returns the 2014 subpopulation under poverty level as a percentage
     of the total 2014 population of the provided data"""
    total_2014_population_list = []
    total_2014_poverty_list = []
    for i in p1:
        state = i.state
        year_2014_population = i.population
        poverty_level = i.income
        if "2014 Population" in year_2014_population and p2 in state:
            population = year_2014_population["2014 Population"]
            poverty = poverty_level["Persons Below Poverty Level"]
            total_2014_population_list.append(population)
            result = population * (poverty / 100)
            total_2014_poverty_list.append(result)
    total_2014_population = sum(total_2014_population_list)
    total_2014_poverty = sum(total_2014_poverty_list)
    poverty_as_percentage = (total_2014_poverty / total_2014_population) * 100
    return poverty_as_percentage


def displayLt(p1: List[CountyDemographics], p2: str, p3: float) -> List[str]:
    """This functions displays data accordingly"""
    display = []
    for i in p1:
        age = i.age
        county = i.county
        education = i.education
        ethnicity = i.ethnicities
        income = i.income
        population = i.population
        state = i.state
        if p2 in education and education[p2] < p3:
            var_county_demographics = f"{county}, {state} \n     Population: {population} \n     Age: {age} \n " \
                                      f"    Education: {education} \n     Ethnicity: {ethnicity} \n     " \
                                      f"Income: {income} \n"
            display.append(var_county_demographics)
    return display


def displayGt(p1: List[CountyDemographics], p2: str, p3: float) -> List[str]:
    """This functions displays data accordingly"""
    display = []
    for i in p1:
        age = i.age
        county = i.county
        education = i.education
        ethnicity = i.ethnicities
        income = i.income
        population = i.population
        state = i.state
        if p2 in education and education[p2] > p3:
            var_county_demographics = f"{county}, {state} \n     Population: {population} \n     Age: {age} \n " \
                                      f"    Education: {education} \n     Ethnicity: {ethnicity} \n     " \
                                      f"Income: {income} \n"
            display.append(var_county_demographics)
    return display


def fact(i):
    pass


def printIt(c):
    for i in c:
        print(i)
    return ""



def belowPovertyLevelLessThanEducation(p1: List[CountyDemographics], p2: int) -> float:
    """This function returns the percentage of the population below poverty level in the counties for which the
    high school or above completion percentage is < 80 percent"""
    below_poverty_level_less_than_list = []
    for i in p1:
        education = i.education
        income = i.income
        if "Persons Below Poverty Level" in income and education["High School or Higher"] < p2:
            percentage_of_poverty = income["Persons Below Poverty Level"]
            below_poverty_level_less_than_list.append(percentage_of_poverty)
    sum_up = sum(below_poverty_level_less_than_list)
    return sum_up

def belowPovertyLevelGreaterThanEducation(p1: List[CountyDemographics], p2: int) -> float:
    """This function returns the percentage of the population below poverty level in the counties for which the
    high school or above completion percentage is < 80 percent"""
    below_poverty_level_greater_than_list = []
    for i in p1:
        education = i.education
        income = i.income
        if "Persons Below Poverty Level" in income and education["Bachelor's Degree or Higher"] > p2:
            percentage_of_poverty = income["Persons Below Poverty Level"]
            below_poverty_level_greater_than_list.append(percentage_of_poverty)
    sum_up = sum(below_poverty_level_greater_than_list)
    return sum_up


def belowPovertyLevelGreaterThanEthnicity(p1: List[CountyDemographics], p2: int) -> float:
    """This function returns the percentage of the population below poverty level in the counties for which the
   selected ethnicity is > 40 percent"""
    below_poverty_level_greater_than_list = []
    for i in p1:
        ethnicity = i.ethnicities
        income = i.income
        if "Persons Below Poverty Level" in income and ethnicity["White Alone"] > p2:
            percentage_of_poverty = income["Persons Below Poverty Level"]
            below_poverty_level_greater_than_list.append(percentage_of_poverty)
    sum_up = sum(below_poverty_level_greater_than_list)
    return sum_up


def belowPovertyLevelLessThanEthnicity(p1: List[CountyDemographics], p2: int) -> float:
    """This function returns the percentage of the population below poverty level in the counties for which the
   selected ethnicity is < 40 percent"""
    below_poverty_level_less_than_list = []
    for i in p1:
        ethnicity = i.ethnicities
        income = i.income
        if "Persons Below Poverty Level" in income and ethnicity["White Alone"] < p2:
            percentage_of_poverty = income["Persons Below Poverty Level"]
            below_poverty_level_less_than_list.append(percentage_of_poverty)
    sum_up = sum(below_poverty_level_less_than_list)
    return sum_up


if __name__ == "__main__":
    print(belowPovertyLevelGreaterThanEthnicity(build_data.getData(), 40))
    print(len(ethnicityGreaterThan(build_data.getData(), "White Alone", 40)))
    print(belowPovertyLevelLessThanEthnicity(build_data.getData(), 40))
    print(len(ethnicityLessThan(build_data.getData(), "White Alone", 40)))