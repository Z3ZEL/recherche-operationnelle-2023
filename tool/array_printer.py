class TwoDimArray:
    def __init__(self, array, column_names):
        self.array = array
        self.column_names = column_names

        # Verify that the array is 2D (checking if the first element is a list)
        if not isinstance(self.array[0], list):
            raise ValueError("The array must be 2D")
    
    def __fill_with_blanks(self, str, length):
        while len(str) < length:
            str += " "
        return str

    def __str__(self) -> str:
        '''Returns a string representation of the array printing the column names, a separator and the array itself, all aligned to its columns names'''
        #CONVERT ALL ELEMENTS TO STRINGS
        for row in self.array:
            for index, element in enumerate(row):
                row[index] = str(element)
        
        # Get the length of the longest column name
        longest_column_name = max(self.column_names, key=len)
        longest_column_name_length = len(str(longest_column_name))

        # Get the length of the longest element in the array 2D 
        longest_element = max([max(row, key=len) for row in self.array], key=len)
        longest_element_length = len(str(longest_element))

        longest = max(longest_column_name_length, longest_element_length)

        final_string = ""

        # Print the column names
        for column_name in self.column_names:
            final_string += self.__fill_with_blanks(column_name, longest + 1)
            
        final_string += "\n"

        # Print the separator
        for column_name in self.column_names:
            final_string += "-" * (longest + 1)
        final_string += "\n"

        # Print the array
        for row in self.array:
            for element in row:
                final_string += self.__fill_with_blanks(element, longest + 1)
                
            final_string += "\n"

        return final_string
        
    