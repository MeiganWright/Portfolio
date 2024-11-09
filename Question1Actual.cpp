//Name: Meigan Wright
// ID#: 96871
// Assignment 3 Question 1
//This program simulates an ATM machine in which one can enter their ID and balance, 
//have their information calculated and displayed to them.

#include <stdio.h>
#include <math.h>
#include <ctype.h>
void main () 
{
	int AcctNum;
	double F_Balance, W_Balance;          //Final Balance ansd Working Balance
	double tempWithdrawal, tempDeposit;    //Values user enters
	double W_Amnt, D_Amnt;                 //Final amount to be displayed
	char T_Response, C_Response, Cont_Response;            // Transaction response and Continuation response
	char Trans_Type;

	C_Response = 'Y';                                 //Initially set to yes to continue on start up

	while (C_Response == 'Y')                  
	{
		printf_s("Please Enter Your ID. \n");
		scanf_s("%d", &AcctNum);
		printf_s("Enter your current balance. \n");
		scanf_s("%lf", &W_Balance);

		F_Balance = 0;          //no values overlap
		W_Amnt = 0;
		D_Amnt = 0;
		T_Response= 'Y';

		while (T_Response == 'Y')
		{
			printf_s("What type of transaction would you like to do? W for Withdrawal, or D for Deposit. \n");
			scanf_s(" %c", &Trans_Type);
			Trans_Type = toupper(Trans_Type);

			while (!(Trans_Type == 'W' || Trans_Type == 'D'))
			{
				printf_s("Invalid. Please enter W for Withdrawals and D for deposits. \n");
				scanf_s(" %c", &Trans_Type);
				Trans_Type = toupper(Trans_Type);
			}

			switch (Trans_Type)
			{
			case 'W':
				printf_s("How much money would you like to withdraw? \n");
				scanf_s("%lf", &tempWithdrawal);
				W_Balance = W_Balance - tempWithdrawal; 
				F_Balance = W_Balance;
				W_Amnt = W_Amnt + tempWithdrawal;
				printf_s("You have Withdrawn %8.2f \n", tempWithdrawal);
				break;

			case 'D':
				printf_s("How much money would you like to deposit? \n");
				scanf_s("%lf", &tempDeposit);
				W_Balance = W_Balance + tempDeposit;
				F_Balance = W_Balance;
				D_Amnt = D_Amnt + tempDeposit;
				printf_s("You have deposited %8.2f \n", tempDeposit);
				break;

			default: 
				break;
			}
			printf_s("Any more transactions? Y for Yes and N for No. \n");
			scanf_s(" %c", &T_Response);
			T_Response = toupper(T_Response);
			
			while (T_Response != 'Y' && T_Response != 'N')
			{
				printf_s("Please enter Y for Yes and N for No. \n");
				scanf_s(" %c", &T_Response);
				T_Response = toupper(T_Response);
			}

		}
		
		printf_s("You have withdrawn %8.2f \n", W_Amnt);
		printf_s("You have deposited %8.2f \n", D_Amnt);
		printf_s("The ID# %d has a  Final Balance of %8.2f \n",AcctNum, F_Balance);

		printf_s("Are there any more clients? Y for Yes and N for No. \n");
		scanf_s(" %c", &C_Response);
		C_Response = toupper(C_Response);

		while (C_Response != 'Y' && C_Response != 'N')
		{
			printf_s("Please enter Y for Yes and N for No. \n");
			scanf_s(" %c", &C_Response);
			C_Response = toupper(C_Response);
		}

	}
}