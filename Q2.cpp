//Name: Meigan	Wright	
//ID#: 96871
//Assignment 4-Question 2


//Determines GPA and displays Honours' List or Academic Status based on txt files provided.


#include <string.h>
#include <stdio.h>

typedef struct
{
	char fName[50], lName[50];
	int ID;
	double GPA;
	char status;
}student;

FILE* inf, * outf;

void main()
{
	int i;
	student s[10];

	fopen_s(&inf, "C:/Programming/YearOneICT.txt", "r");
	fopen_s(&outf, "C:/Programming/ClassSummary.txt", "w");

	for (i = 0; i < 10; i++)
	{
		fscanf_s(inf, "%s%s", s[i].fName, sizeof(s[i].fName), s[i].lName, sizeof(s[i].lName));
		fscanf_s(inf, "%d%lf", &s[i].ID, &s[i].GPA);

		if (s[i].GPA < 2.0)
			s[i].status = 'P';
		else if ((s[i].GPA >= 2.0) && (s[i].GPA <= 3.8))
			s[i].status = 'N';
		else if (s[i].GPA > 3.8)
			s[i].status = 'H';
	}

	printf_s("Honours List: \n");
	fprintf_s(outf, "Honours List \n");
	for (i = 0; i < 10; i++) 
	{
		if (s[i].status == 'H')
		{
			printf_s("%s %s\t%d\t%.2f\n", s[i].fName, s[i].lName, s[i].ID, s[i].GPA);
			fprintf_s(outf, "%s %s\t%d\t%.2f\n", s[i].fName, s[i].lName, s[i].ID, s[i].GPA);
		}
	}
	printf_s("Progressing Normally: \n");
	fprintf_s(outf, "Progressing Normally: \n");
	for (i = 0; i < 10; i++)
	{
		if (s[i].status == 'N')
		{
			printf_s("%s %s\t%d\t%.2f\n", s[i].fName, s[i].lName, s[i].ID, s[i].GPA);
			fprintf_s(outf, "%s %s\t%d\t%.2f\n", s[i].fName, s[i].lName, s[i].ID, s[i].GPA);
		}
	}
	printf_s("Academic Probation: \n");
	fprintf_s(outf, "Academic Probation: \n");
	for (i = 0; i < 10; i++)
	{
		if (s[i].status == 'P')
		{
			printf_s("%s %s\t%d\t%.2f\n", s[i].fName, s[i].lName, s[i].ID, s[i].GPA);
			fprintf_s(outf, "%s %s\t%d\t%.2f\n", s[i].fName, s[i].lName, s[i].ID, s[i].GPA);
		}
	}
	fclose(inf);
	fclose(outf);

}