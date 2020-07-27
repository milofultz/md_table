import pyinputplus as pyip


def get_data(n):
	lst = []
	lst.append(input(f"What is your header for column {n}? "))

	print("Entering data. Type nothing to finish entering data for this column.")
	while True:
		item = input("Input your next piece of data : ")
		if not item:
			break
		lst.append(item)

	print(f"Completed column {n}.")

	return lst

def get_width(lst):
	length = 3 # minimum length for header hyphens
	for i in lst:
		if len(i) > length:
			length = len(i)

	return length

def format_list(lst, width):
	for num, i in enumerate(lst):
		lst[num] = i.center(width)
	
	lst.insert(1, '-'*width)
	return lst

def elongate(lst):
	length = len(max(lst, key=len))

	for sublist in lst:
		while len(sublist) < length:
			sublist.append("")

	return lst, length

def make_table(lst, length):
	table = ""
	beg, end = "| ", " |"
	for i in range(length):
		mid = ' | '.join(sublist[i] for sublist in lst)
		table += beg + mid + end
		if i != length:
			table += "\n"

	return table

def make_file(fp, data):
	with open(fp, 'w') as f:
		f.write(data)


if __name__ == '__main__':
	col = pyip.inputInt("How many columns of data do you have? (e.g. 4) ")
	data = []
	for column in range(col):
		data.append([])
		data[column] = get_data(column+1)

	data, length = elongate(data)

	for n, column in enumerate(data):
		width = get_width(column)
		data[n] = format_list(column, width)

	table = make_table(data, length)

	filename = pyip.inputStr("What do you want to name the file? (No extensions)\n")
	make_file(f"{filename}.md", table)

	print(f"File {filename}.md created!")