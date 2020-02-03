#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

/*
simple Idea sort in alphabetical order
if someone is different, his or her name is answer
participant.size()-completion.size() = 1

*/
bool compare(string a, string b) {
	return a < b;
}

string solution(vector<string> participant, vector<string> completion) {
	string answer = "";
	sort(participant.begin(), participant.end(), compare); // using lib's sort
	sort(completion.begin(), completion.end(), compare);
	for (int i = 0; i < participant.size(); i++) {
		if (participant[i] != completion[i]) {
			answer = participant[i];
			break;
		}
	}

	return answer;
}

int main() 
{
	vector<string> part = { "mislav", "stanko", "mislav", "ana" };
	vector<string> com = { "stanko", "ana","mislav" };
	cout << solution(part, com) << endl;
}
