#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    for(int iter=0;iter<commands.size();iter++){
        int i = commands[iter][0];
        int j = commands[iter][1];
        int k = commands[iter][2];
        vector<int> tmp;
        for(int s=i-1;s<j;s++){
            tmp.push_back(array[s]);
        }
        sort(tmp.begin(),tmp.end());
        answer.push_back(tmp[k-1]);
        
    }
    
    return answer;
}
