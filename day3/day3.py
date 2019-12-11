def main():
	# first_wire_directions = ["R75","D30","R83","U83","L12","D49","R71","U7","L72"]
	# second_wire_directions = ["U62","R66","U55","R34","D71","R55","D58","R83"]

	first_wire_directions = []
	second_wire_directions = []

	with open('day3_1.txt', 'r') as f:
		for line in f:
			linelist = line.split(",")
			for c in linelist: 
				first_wire_directions.append(c)

	with open('day3_2.txt', 'r') as f:
		for line in f:
			linelist = line.split(",")
			for c in linelist: 
				second_wire_directions.append(c)

	first_wire_path = []
	second_wire_path = []

	intersections = []

	def get_path(command: str, position: tuple) ->tuple:
		direction = command[0]
		command = int(command[1:])
		positions = []
		if direction == 'R':
			for i in range(command):
				position =(position[0], position[1] + 1)
				positions.append(position)

		if direction == 'L':
			for i in range(command):
				position = (position[0], position[1] - 1)
				positions.append(position)

		if direction == 'U':
			for i in range(command):
				position =(position[0]+1, position[1])
				positions.append(position)


		if direction == 'D':
			for i in range(command):
				position =(position[0]-1, position[1])
				positions.append(position)


		return position, positions



	position = [0,0]
	position_2 = [0,0]


	positions_to_compare_1 = []
	positions_to_compare_2 = []
	
	for direction in first_wire_directions:
		position, tmp_positions = get_path(direction,position)
		positions_to_compare_1.extend(tmp_positions)

	for direction in second_wire_directions:
		position_2, tmp_positions = get_path(direction,position_2)
		positions_to_compare_2.extend(tmp_positions)

	intersections = set(positions_to_compare_1).intersection(set(positions_to_compare_2))

	intersections = []
	for p in positions_to_compare_1:
		if p in positions_to_compare_2:
			intersections.append(p)

	dist = -1

	for intersection in list(intersections):
		t_dist = abs(intersection[0]) + abs(intersection[1])
		if t_dist < dist or dist == -1:
			 print(t_dist, intersection)
			 dist=t_dist

	print(dist)



main()