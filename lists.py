def remove_elements(list_to_remove_elements):
	if len(list_to_remove_elements) >= 1:
		del list_to_remove_elements[0]
		del list_to_remove_elements[3:5]
	return list_to_remove_elements

def add_elements(list_to_add_elements):
	list_to_add_elements.insert(0, 'Pink')
	list_to_add_elements.append('Yellow')
	lista = list_to_add_elements
	return lista

def is_empty(list_to_check):
	largo = len(list_to_check)
	return largo == 0

def check_lists(list_to_compare1, list_to_compare2):
	if len(list_to_compare1) > 2 and len(list_to_compare2) > 2:
		return list_to_compare1[2] == list_to_compare2[2]
	else:
		return False

def list_of_lists(list_of_lists_to_modify):
	list_of_sliced_list = [list_of_lists_to_modify [0] [:2], list_of_lists_to_modify [1] [1:4], list_of_lists_to_modify [2] [-2:]]
	return list_of_sliced_list
