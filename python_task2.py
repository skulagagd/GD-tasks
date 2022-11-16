list_of_numbers = [3, 5, 2, 3, 5, 2, 3, 5, 2, 4, 4, 7, 7] 

#Below is a commented solution which is probably most direct to the task, but also worst in terms how it looks/number of lines
'''
def create_tuple_from_list(list_of_numbers):
    output = []
    for number in list_of_numbers:
            if number not in output:
                output.append(number)
    return tuple(output)

tuple_of_numbers = create_tuple_from_list(list_of_numbers)
'''

tuple_of_numbers = tuple(set(list_of_numbers)) #You cannot store duplicate values in set so it "cleans" list of it

print(list_of_numbers)
print(tuple_of_numbers)
print(min(tuple_of_numbers))
print(max(tuple_of_numbers))



