#include<stdio.h>


void main()
{

	int idNum[12], i;
	double msales[12], percentSales[12], commiss[12];
	double temp1 = 0;
	double temp = 0;
	double temp2 = 0;
	double temp3 = 0;
	double totSales = 0;
	int flag = 0;
	double totpercent = 0;
	double totcommiss = 0;


	//populate id and monthly sales arrays
	for (i = 0; i <= 11; i++)
	{
		printf_s("Enter ID num \n");
		scanf_s("%d", &idNum[i]);
		printf_s("Enter monthly sales\n");
		scanf_s("%lf", &msales[i]);
		totSales = totSales + msales[i];
	}



	//calculate percentage sales and commissions for each employee
	for (i = 0; i <= 11; i++)
	{
		percentSales[i] = (msales[i] / totSales) * 100;
		if ((percentSales[i] >= 0.00) && (percentSales[i] <= 24.99))
			commiss[i] = msales[i] * 0.02;
		else if ((percentSales[i] >= 25.00) && (percentSales[i] <= 74.99))
			commiss[i] = msales[i] * 0.04;
		else
			commiss[i] = msales[i] * 0.06;
		//accumulate totals
		totcommiss = totcommiss + commiss[i];
		totpercent = totpercent + percentSales[i];
	}




	//sort all arrays according to descending monthly sales
	while (flag == 0)
	{
		flag = 1;
		for (i = 0; i <= 10; i++)
		{
			if (msales[i] < msales[i + 1])
			{
				temp = msales[i];
				msales[i] = msales[i + 1];
				msales[i + 1] = temp;

				temp1 = idNum[i];
				idNum[i] = idNum[i + 1];
				idNum[i + 1] = temp1;

				temp2 = percentSales[i];
				percentSales[i] = percentSales[i + 1];
				percentSales[i + 1] = temp2;

				temp3 = commiss[i];
				commiss[i] = commiss[i + 1];
				commiss[i + 1] = temp3;

				flag = 0;

			}
		}
	}



	//print report
	printf_s("			MONTHLY SALES REPORT\n\n");
	printf_s("ID       SALES       PERCENT       COMMISSION\n\n");

	for (i = 0; i <= 11; i++)
		printf_s("%2d       %8.2f      %8.2f      %8.2f\n", idNum[i], msales[i], percentSales[i], commiss[i]);
	printf_s("\n");
	printf_s("TOTALS      %8.2f     %8.2f       %8.2f", totSales, totpercent, totcommiss);

}
