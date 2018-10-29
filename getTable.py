from spreadsheet import user_sheet
def get_data():
	x = {
		'users': user_sheet.col_values(1)[1:],
		'scores': user_sheet.col_values(2)[1:]
	}
	return x
