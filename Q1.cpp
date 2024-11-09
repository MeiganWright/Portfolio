//Name: Meigan	Wright	
//ID#: 96871
//Assignment 4-Question 1

//Calculates total general Business costs for individuals using provided txt files including each employee's relevant info
//such as months total sales, commissions earned and the determined commission percentage based on earnings.


#include <string.h>
#include <stdio.h>

typedef struct
{
	int id;
	double monthSales;
	double commission;
	double percentage;
}Sales;

FILE* inf, * outf;

void main()
{
	int i;
	double totalSales=0;  
	double percentTotal = 0 , commissionTotal=0;
	Sales s[12];

	fopen_s(&inf, "C:/Programming/employeeSales.txt", "r");
	fopen_s(&outf, "C:/Programming/MonthlySales.txt", "w");

	for (i = 0; i < 12; i++)
	{
		fscanf_s(inf, "%d%lf", &s[i].id, &s[i].monthSales);                 
		totalSales = totalSales + s[i].monthSales;
	}
	
	for (i = 0; i < 12; i++)
	{
		s[i].percentage = (s[i].monthSales / totalSales) * 100;

		if (s[i].percentage <= 24.99)
			s[i].commission = s[i].monthSales * 0.02;
		else if (s[i].percentage <= 74.99 && s[i].percentage >= 25.00)
			s[i].commission = s[i].monthSales * 0.04;
		else if (s[i].percentage <= 100 && s[i].percentage >= 75.00)
			s[i].commission = s[i].monthSales * 0.06;

		percentTotal = percentTotal + s[i].percentage;
		commissionTotal = commissionTotal + s[i].commission;

	}
	fprintf_s(outf, "\t\t\tMONTHLY SALES REPORT\n\n");
	printf_s("\t\t\tMONTHLY SALES REPORT\n\n");
	fprintf_s(outf, "ID\t\tSALES\t\t\tPERCENT\t\tCOMMISSION\n");
	printf_s("ID\t\tSALES\t\t\tPERCENT\t\tCOMMISSION\n");
	
	for (i = 0; i < 12; i++) 
	{
		printf_s("%d\t\t%8.2f\t\t%3.2f\t\t%.2f \n", s[i].id, s[i].monthSales, s[i].percentage, s[i].commission);
		fprintf_s(outf, "%d\t\t%8.2f\t\t%3.2f\t\t%.2f \n", s[i].id, s[i].monthSales, s[i].percentage, s[i].commission);
	}
	printf_s("\nTOTALS\t\t%8.2f\t\t%.2f\t\t%.2f", totalSales, percentTotal, commissionTotal);
	fprintf_s(outf, "\nTOTALS\t\t%8.2f\t\t%.2f\t\t%.2f", totalSales, percentTotal, commissionTotal);

	fclose(inf);
	fclose(outf);
}