#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream fileStreams;
	int streams;
	ifstream fileValenceMean;
	double valenceMean;


	fileStreams.open("streams.txt");
	fileValenceMean.open("valence_mean.txt");


	if (!fileStreams.is_open()) {
		cout << "Can't open streams file" << endl;
		system("pause");
		exit(0);
	}

	if (!fileValenceMean.is_open()) {
		cout << "Can't open valence_mean file" << endl;
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