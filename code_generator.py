import sys

#get city codes
def get_city_code(city):
	index = 1
	generated_code = code_generator_one(city)
	#keep generating codes until unique one is generated
	while True:	
		#if first 3 letter code already exists then generate a code in the 
		#form of first letter + middle + last; middle keeps increasing until middle is more than length
		if generated_code in stn_names or generated_code in new_codes:
			generated_code = code_generator_two(city,index)
			index += 1
		#if code is unique return the code
		else:
			return generated_code
			
		if index>len(city)-2:
			generated_code = worst_case(city)
			if generated_code == 'false':
				return "invalid city"
			else:
				return generated_code
			

#return first 3 letters as code
def code_generator_one(city):
	return city[0:3]

#return first letter + index + last
def code_generator_two(city,index):
	length = len(city)
	return city[0]+city[index]+city[length-1]
	
#worst case city of consecutive 3 letters
def worst_case(city):
	for index in range(0, len(city)-3):
		temp_code = city[index:index+3]
		if temp_code in stn_names or temp_code in new_codes:
			continue
		else:
			return temp_code
	return 'false'
	


#initialise all existing station names
stn_names = []
stn_name_file = open(sys.argv[1],'r')
for code in stn_name_file:
	stn_names.append(code[:-1])



#open city files and generate codes
cities = open(sys.argv[2],'r')
new_codes = []
city_array = []
for city in cities:
	city_array.append(city[:-1])
	temp_code = get_city_code(city[:-1])
	new_codes.append(temp_code)
	
#save the generated codes along with city name to a file
output_file = open('generated_codes.txt','w')
for i in range(0, len(city_array)):
	temp_str = city_array[i][:-1] + ', ' + new_codes[i] + '\n'
	output_file.write(temp_str)
output_file.close()		


