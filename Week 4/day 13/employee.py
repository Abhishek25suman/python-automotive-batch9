#---- EMPLOYEE-MANAGER REPORT PROGRAM ----

# there are 3 managers and 12 employees who should report to those managers.
# no duplicate mapping
# use the advanced python features like map, filter, lambda, reduce, zip etc to implement the same


from functools import reduce

# managers list
managers = ["M1", "M2", "M3"]

# employees list
employees = [f"E{i}" for i in range(1, 13)]

def distribute(result, indexed_employee):
    index = indexed_employee[0]      # position of employee
    employee = indexed_employee[1]   # employee name

    manager1_emps = result[0]
    manager2_emps = result[1]
    manager3_emps = result[2]

    if index % len(managers) == 0:
        manager1_emps = manager1_emps + [employee]
    elif index % len(managers) == 1:
        manager2_emps = manager2_emps + [employee]
    else:
        manager3_emps = manager3_emps + [employee]

    # returns updated result
    return (manager1_emps, manager2_emps, manager3_emps)

assignments = reduce(
    distribute,
    enumerate(employees),
    ([], [], [])
)

#create final reporting map
reporting_map = {
    managers[0]: assignments[0],
    managers[1]: assignments[1],
    managers[2]: assignments[2]
}

# print output
list(map(lambda item: print(f"{item[0]} -> {item[1]}"), reporting_map.items()))