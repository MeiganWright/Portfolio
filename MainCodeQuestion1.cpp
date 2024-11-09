//Name:  Meigan Wright 
//ID#: 96871
// Assignment 2 Question 1
//This program provides a percentage tally based on the responses to a survey.
#include<stdio.h>
#include<ctype.h>

void main()
{
	char answer;
	int walkers=0;
	int drivers=0;
	int OnCampus=0;
	double WalkPercent=0;
	double DrivePercent=0;
	double CampusPercent=0;
	double NumOfAnswers = 0;
	
	printf_s("Do you walk, drive or live on campus? Use: \n" 
		"W - if you walk \n"
		"D- if you drive \n"
		"L-if you live on campus\n");

	while (NumOfAnswers <= 24)
	{
		printf_s("Please Enter your Response. \n");
		scanf_s(" %c", & answer);
		answer = toupper(answer);

		switch (answer)
		{
		case 'W':
			walkers = walkers + 1;
			NumOfAnswers = NumOfAnswers + 1;
			break;
		case 'D':
			drivers = drivers + 1;
			NumOfAnswers = NumOfAnswers + 1;
			break;
		case 'L':
			OnCampus = OnCampus + 1;
			NumOfAnswers = NumOfAnswers + 1;
			break;
		default:
			printf_s("Please Enter W, D or L \n");
			break;

		}
	
	}
	
	WalkPercent = (walkers / NumOfAnswers) * 100;
	DrivePercent = (drivers / NumOfAnswers) * 100;
	CampusPercent = (OnCampus / NumOfAnswers) * 100;

	printf_s("%3.2f%% of students walk to campus.", WalkPercent);
	printf_s("%3.2f%% of students drive to campus.", DrivePercent);
	printf_s("%3.2f%% of students live on campus.", CampusPercent);

}