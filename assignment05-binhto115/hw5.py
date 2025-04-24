# Name: Binh To
# Date: 11/07/2022
# Github: 113943258

import sys
import build_data
import hw4

file_input = 0
file = 0
field = 0

try:
    file = sys.argv[1]
    file_input = open(file, "r")
except FileNotFoundError:
    print("The file does not exist")
except IndexError:
    print("The index of the inputted file is out of range")

try:
    print(str(len(build_data.getData())) + " records loaded")
except IndexError:
    print("Missing a value in the text file")
except ValueError:
    print("A string could not be converted to float")

for line in file_input:
    # Split each line into strings
    replacements = (":", ".")
    for i in replacements:
        line = line.replace(i, " ")
    replaced_line_split = line.split()
    field = " ".join(replaced_line_split[2:])

    try:
        # This is pop.ops
        if file == "inputs/pop.ops":
            if "population-total" in replaced_line_split:
                print("2014 population: " + str(hw4.populationTotal(build_data.getData())))
        # This is pop_field.ops
        elif file == "inputs/pop_field.ops":
            if "population" in replaced_line_split:
                if "Education" in replaced_line_split:
                    print("2014 " + f"{line[11:20]}" + "." + f"{line[21:]}" + "population: " +
                          str(hw4.populationByEducation(build_data.getData(), field)))
                elif "Ethnicities" in replaced_line_split:
                    print("2014 " + f"{line[11:22]}" + "." f"{line[23:]}" + "population: " +
                          str(hw4.populationByEthnicity(build_data.getData(), field)))
                elif "Income" in replaced_line_split:
                    print("2014 " + f"{line[11:17]}" + "." f"{line[18:]}" + "population: " +
                          str(hw4.populationBelowPovertyLevel(build_data.getData())))
        # This is percent_fields.ops
        elif file == "inputs/percent_fields.ops":
            if "percent" in replaced_line_split:
                if "Education" in replaced_line_split:
                    print("2014 " + f"{line[8:17]}" + "." + f"{line[18:]}" + "percentage: " +
                          str(hw4.percentByEducation(build_data.getData(), field)))
                elif "Ethnicities" in replaced_line_split:
                    print("2014 " + f"{line[8:19]}" + "." + f"{line[20:]}" + "percentage: " +
                          str(hw4.percentByEthnicity(build_data.getData(), field)))
                elif "Income" in replaced_line_split:
                    print("2014 " + f"{line[8:14]}" + "." + f"{line[15:]}" + "percentage: " +
                          str(hw4.percentBelowPovertyLevel(build_data.getData())))
        # This is filter_state.ops
        elif file == "inputs/filter_state.ops":
            if "filter-state" in replaced_line_split:
                print("Filter: state == " + str(replaced_line_split[1]) + " (" +
                      str(len(hw4.filterByState(build_data.getData(), replaced_line_split[1]))) + " entries" + ")")
        # This is ca.ops
        elif file == "inputs/ca.ops":
            if "filter-state" in replaced_line_split:
                print("Filter: state == " + str(replaced_line_split[1]) + " (" +
                      str(len(hw4.filterByState(build_data.getData(), replaced_line_split[1]))) + " entries" + ")")
            elif "population-total" in replaced_line_split:
                print("2014 Population: " + str(hw4.populationState(build_data.getData(), "CA")))
            elif "percent" in replaced_line_split:
                if "Education" in replaced_line_split:
                    print("2014 " + f"{line[8:17]}" + "." + f"{line[18:]}" + "percentage: " + str(
                        hw4.percentByEducationState(build_data.getData(), field, "CA")))
                elif "Ethnicities" in replaced_line_split:
                    print("2014 " + f"{line[8:19]}" + "." + f"{line[20:]}" + "percentage: " + str(
                        hw4.percentByEthnicityState(build_data.getData(), field, "CA")))
                elif "Income" in replaced_line_split:
                    print("2014 " + f"{line[8:14]}" + "." + f"{line[15:]}" + "percentage: " +
                          str(hw4.percentBelowPovertyLevelState(build_data.getData(), "CA")))
        # This is high_school_lt_60.ops
        elif file == "inputs/high_school_lt_60.ops":
            if "filter-lt" in replaced_line_split:
                if "Education" in replaced_line_split:
                    print("Filter: " + replaced_line_split[1] + "." + field[:21] + f" {replaced_line_split[6]}" +
                          " lt" + " (" +
                          str(len(hw4.educationLessThan(build_data.getData(), "High School or Higher", 60))) +
                          " entries" + ")")
            elif "display" in replaced_line_split:
                print(hw4.printIt(hw4.displayLt(build_data.getData(), "High School or Higher", 60)))
        # This is bachelors_gt_60.ops
        elif file == "inputs/bachelors_gt_60.ops":
            if "filter-gt" in replaced_line_split:
                if "Education" in replaced_line_split:
                    print("Filter: " + replaced_line_split[1] + "." + field[:21] + f" {replaced_line_split[6]}" +
                          " gt" + " (" + str(
                        len(hw4.educationGreaterThan(build_data.getData(), "Bachelor's Degree or Higher",
                                                     60))) + " entries" + ")")
            elif "display" in replaced_line_split:
                print(hw4.printIt(hw4.displayGt(build_data.getData(), "Bachelor's Degree or Higher", 60.0)))
        # This is some_errors.ops:
        elif file == "inputs/some_errors.ops":
            if "filter-gt" in replaced_line_split:
                if replaced_line_split[6] in replaced_line_split:
                    print("Error: The input value is not a number!")
            elif "filter-lt" in replaced_line_split:
                if "Education" in replaced_line_split and len(replaced_line_split) == 6:
                    print("Error Message: the input education does not exist")
                elif "Education" in replaced_line_split and len(replaced_line_split) == 8:
                    print("Error Message: multiple values founded")
            elif "invalid" in replaced_line_split:
                print("Error Message: operation is not defined!")
            elif "percent" in replaced_line_split:
                if "Ethnicities" in replaced_line_split:
                    print("2014 " + f"{line[8:19]}" + "." + f"{line[20:]}" + "percentage: " +
                          str(hw4.percentByEthnicity(build_data.getData(), "")))
                    print("Error Message: missing a value in the text file!")
            elif "display" in replaced_line_split:
                print("Error Message: uncertain operation!")
        # This is task2_a.ops:
        elif file == "inputs/task2_a.ops":
            if "percentage" in replaced_line_split:
                if "BelowPovertyLevelLessThan" in replaced_line_split:
                    print("2014 " + f"{line[11:36]}" + "." + f"{line[37:59]}" + "percentage: " +
                          str(hw4.belowPovertyLevelLessThanEducation(build_data.getData(), 80)))
        # This is task2_b.ops:
        elif file == "inputs/task2_b.ops":
            if "percentage" in replaced_line_split:
                if "BelowPovertyLevelGreaterThan" in replaced_line_split:
                    print("2014 " + f"{line[11:39]}" + "." + f"{line[40:68]}" + "percentage: " +
                          str(hw4.belowPovertyLevelGreaterThanEducation(build_data.getData(), 40)))
        # This is task2_c.ops:
        elif file == "inputs/task2_c.ops":
            if "percentage" in replaced_line_split:
                if "BelowPovertyLevelGreaterThan" in replaced_line_split:
                    print("2014 " + f"{line[11:39]}" + "." + f"{line[40:50]}" + "percentage: " +
                          str(hw4.belowPovertyLevelGreaterThanEthnicity(build_data.getData(), 40)))
        # This is task2_d.ops:
        elif file == "inputs/task2_d.ops":
            if "percentage" in replaced_line_split:
                if "BelowPovertyLevelLessThan" in replaced_line_split:
                    print("2014 " + f"{line[11:36]}" + "." + f"{line[37:49]}" + "percentage: " +
                          str(hw4.belowPovertyLevelLessThanEthnicity(build_data.getData(), 40)))
    except IndexError:
        print("IndexError: missing a value in the text file")
    except ValueError:
        print("A string could not be converted to float")
file_input.close()

