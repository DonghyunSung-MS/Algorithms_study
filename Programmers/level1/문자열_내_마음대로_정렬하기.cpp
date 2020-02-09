#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int idx = 0;
bool cmp(string a,string b){
    //return a[idx]<b[idx] ? true:false;
    if(a[idx]<b[idx]) return true;
    else if (a[idx]==b[idx]){
        if(a<b) return true;
        else return false;
    }
    else return false;
}

vector<string> solution(vector<string> strings, int n) {
    //index 
    idx = n;
    int len = strings.size();
    vector<string> answer;
    answer.reserve(len);
    answer = strings;
    sort(answer.begin(),answer.end(),cmp);
    return answer;
}
