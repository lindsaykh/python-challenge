Goal: The main_pypoll.py program takes a csv file in the Resources folder (one directory up)
	with vote counts for specific candidates (Khan, O'Tooley, Correy, and Li). Election results
	are printed in the terminal and to a new .txt file called election_results.

Requirements: A csv file with columns specifying voter ID (or any representation of a single vote) in the first
	column and the name of the candidate for whom the voter voted is written in column 3. This program only works 
	for the candidates listed in the "Goal" portion of this README and assumes all capitalization and spelling of 
	candidate names is correct. A folder named "Analysis" must be in the directory of the program so that a .txt file
	with the results can be created. Finally, the data that is analyzed must be located in the "Resources" folder
	up one directory.

Directions: Run the program. You will be prompted to enter the filename (without extension) that contains the election
	data. Election results will be printed in the terminal and in a .txt file.


References:
Used to count based on specific items in a row
https://thispointer.com/python-count-elements-in-a-list-that-satisfy-certain-conditions/
explanation of the function used to count specific items in a row
https://www.geeksforgeeks.org/python-map-function/
how to find a maximum value in a python dictionary
https://stackoverflow.com/questions/42044090/return-the-maximum-value-from-a-dictionary/42044202
how to get the corresponding key based on the dictionary value (i.e. corresponding name for max vote count)
https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary