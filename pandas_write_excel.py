from sys import argv;
import xlsxwriter;


def Excel_writer(name):

	workbook=xlsxwriter.Workbook(name);

	worksheet=workbook.add_worksheet();

	worksheet.write('A1','Name')
	worksheet.write('B1','College')
	worksheet.write('C1','Email')
	worksheet.write('D1','Subject')
	worksheet.write('E1','Mobile')
	
	workbook.close();

def main():
	print("---------Writting Data Into Excel----------");
	print(argv[0]);
	Excel_writer(argv[1]+".xlsx");



if __name__ == '__main__':
	main()
