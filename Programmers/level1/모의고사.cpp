#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

int score[3] = { 0 };

using namespace std;
bool comp(int a, int b) {
	return score[a - 1] > score[b - 1];
}
vector<int> solution(vector<int> answers) {
	vector<int> cycle[3]; //cycle
	vector<int> answer; //students number

	cycle[0] = { 1, 2, 3, 4, 5 };
	cycle[1] = { 2, 1, 2, 3, 2, 4, 2, 5 };
	cycle[2] = { 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 };

	for (int i = 0; i < answers.size(); i++)//problem
	{
		for (int j = 0; j < 3; j++) {//student
			if (answers[i] == cycle[j][i]) {
				score[j]++;
			}
		}
	}

	vector<int> rank = { 1,2,3 };
	sort(rank.begin(), rank.end(), comp);
	if (score[rank[0]-1] != score[rank[1]-1]) {
		answer = { rank[0] };
	}
	else {
		if (score[rank[1]-1] != score[rank[2]-1]) {
			answer = { rank[0],rank[1] };
		}
		else
			answer = { rank[0],rank[1],rank[2] };
	}

	return answer;
}

int main() {
	vector<int> ans = { 1,2,3,4,5 };
	vector<int> output = solution(ans);
	for (int i = 0; i < output.size(); i++) {
		cout << output[i] <<" ";
	}


}
