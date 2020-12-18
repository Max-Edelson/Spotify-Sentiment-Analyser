#include <iostream>
#include <fstream>
using namespace std;

void modifiedNumberOfStreamsWeeks();
void modifiedNumberOfStreamsMonths();

int main() {
	//ifstream fileStreams;
	//int streams;
	//ifstream fileValenceMean;
	//double valenceMean;
	char choice;

	cout << "Evaluate for weeks or months?\na:weeks\nb:months" << endl;
	cin >> choice;
	while (choice != 'a' && choice != 'b') {
		cout << "Evaluate for weeks or months?\na:weeks\nb:months" << endl;
		cin >> choice;
	}
	
	if (choice == 'a') {
		modifiedNumberOfStreamsWeeks();
	}

	else {
		modifiedNumberOfStreamsMonths();
	}
}

	void modifiedNumberOfStreamsWeeks() {
		ifstream fileStreams;
		int streams;
		ifstream fileValenceMean;
		double valenceMean;

		fileStreams.open("streams_weeks.txt");
		fileValenceMean.open("valence_mean_weeks.txt");


		if (!fileStreams.is_open()) {
			cout << "Can't open streams_weeks file" << endl;
			system("pause");
			exit(0);
		}

		if (!fileValenceMean.is_open()) {
			cout << "Can't open valence_mean_weeks file" << endl;
			system("pause");
			exit(0);
		}

		int result;

		while (fileStreams.good() && fileValenceMean.good()) {
			fileStreams >> streams;
			fileValenceMean >> valenceMean;

			result = streams / (valenceMean + 1);
			cout << result << endl;

		}
	}

	void modifiedNumberOfStreamsMonths() {
		ifstream fileStreams;
		int streams;
		ifstream fileValenceMean;
		double valenceMean;

		fileStreams.open("streams_months.txt");
		fileValenceMean.open("valence_mean_months.txt");


		if (!fileStreams.is_open()) {
			cout << "Can't open streams_months file" << endl;
			system("pause");
			exit(0);
		}

		if (!fileValenceMean.is_open()) {
			cout << "Can't open valence_mean_months file" << endl;
			system("pause");
			exit(0);
		}

		int result;

		while (fileStreams.good() && fileValenceMean.good()) {
			fileStreams >> streams;
			fileValenceMean >> valenceMean;

			result = streams / (valenceMean + 1);
			cout << result << endl;

		}
	}
