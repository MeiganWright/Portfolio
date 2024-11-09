//Name: Meigan Wright 
//ID#: 96871
//Assignment 3 Question 2
//This program is meant to read agent's IDs and Monthly sales, 
//and provide their commissions based on percentages
//According to a formula.

#include<stdio.h>
#include <math.h>

void main()
{
	int ID[12];
	int i;
	int flag = 0;
	double SalesList[12], PercentList[12], Commission[12];
	double SalesSum = 0, CommissionSum = 0, PercentSum = 0;
	double temp = 0, temp1 = 0, temp2 = 0, temp3 = 0;

	for (i = 0; i <= 11; i++)
	{
		printf_s("Please enter your ID number. \n");
		scanf_s("%d", &ID[i]);
		printf_s("Please enter your Sales for the Month. \n");
		scanf_s("%lf", &SalesList[i]);
		SalesSum = SalesSum + SalesList[i];
	}

	for (i = 0; i <= 11; i++) 
	{
		PercentList[i] = (SalesList[i] / SalesSum) * 100;

		if ((PercentList[i] >= 0.0) && (PercentList[i] <= 24.99))
			Commission[i] = SalesList[i] * 0.02;
		else if ((PercentList[i] >= 25.00) && (PercentList[i] <= 74.99))
			Commission[i] = SalesList[i] * 0.04;
		else if ((PercentList[i] >= 75.00) && (PercentList[i] <= 100.0))
			Commission[i] = SalesList[i] * 0.06;

		CommissionSum = CommissionSum + Commission[i];
		PercentSum = PercentSum + PercentList[i];
	}

	while (flag == 0) 
	{
		flag = 1; 
		for (i = 0; i <= 10; i++)
		{
			if (SalesList[i] < SalesList[i + 1])
			{
				temp = SalesList[i];
				SalesList[i] = SalesList[i + 1];
				SalesList[i + 1] = temp;

				temp1 = ID[i];
				ID[i] = ID[i + 1];
				ID[i + 1] = temp1;

				temp2 = PercentList[i];
				PercentList[i] = PercentList[i + 1];
				PercentList[i + 1] = temp2;

				temp3 = Commission[i];
				Commission[i] = Commission[i + 1];
				Commission[i + 1] = temp3;

				flag = 0;

			}
		}
	}

	printf_s("	   MONTHLY SALES REPORT\n\n");
	printf_s("ID       SALES       PERCENT       COMMISSION\n\n");

	for (i = 0; i < 11; i++)
		printf_s("%2d       %8.2f      %8.2f      %8.2f\n", ID[i], SalesList[i], PercentList[i], Commission[i]);

	printf_s("\n");
	printf_s("TOTALS      %8.2f     %8.2f       %8.2f", SalesSum, PercentSum, CommissionSum);
}



