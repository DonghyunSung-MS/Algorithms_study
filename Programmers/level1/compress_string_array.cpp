//https://programmers.co.kr/learn/courses/30/lessons/60057
#include <string>
#include <iostream>
using namespace std;
#define MAX 987654321
string compress(string s, size_t unit)
{
	//substr(pos,len)
	size_t cnt = 0;
	string total = "";
	string sub_unit = s.substr(0, unit);
	for (size_t i = 0; i < s.size(); i = i + unit)
	{
		string tmp = s.substr(i, unit);//current substring
		if (sub_unit == tmp) {
			cnt++;
		}
		else {
			if (cnt > 1) {
				string cnt2 = to_string(cnt);
				total.append(cnt2 + sub_unit);
			}
			else
				total.append(sub_unit);
			cnt = 1;
			sub_unit = s.substr(i, unit);
		}
		
		cout << total << endl;
	}
	if (cnt > 1) {
		string cnt2 = to_string(cnt);
		total.append(cnt2 + sub_unit);
	}
	else
		total.append(sub_unit);
	cnt = 1;
	cout << total << endl;
	return total;

}
int solution(string s)
{
	//length of s
	size_t len = s.size();
	int answer = MAX;
	for (size_t i = 1; i <= len; i++) {
		//getlength when it compreeses to i unit
		string tmp = compress(s, i);
		if (tmp.size() < answer)
			answer = tmp.size();
	}
	return answer;
}
int main() {
	string s;
	getline(cin, s);
	cout << solution(s) << endl;
	

	return 0;
}
