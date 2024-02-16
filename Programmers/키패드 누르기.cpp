#include <string>
#include <vector>
#include <cstdlib>
#include <cmath>

using namespace std;

string solution(vector<int> numbers, string hand) {
    string answer = "";
    
    int rightPos = 11;
    int leftPos = 10;
    
    vector<pair<int, int>> coordinate;
    
    coordinate.push_back(make_pair(0, 1)); //0
    coordinate.push_back(make_pair(3, 0)); //1
    coordinate.push_back(make_pair(3, 1)); //2
    coordinate.push_back(make_pair(3, 2)); //3
    coordinate.push_back(make_pair(2, 0)); //4
    coordinate.push_back(make_pair(2, 1)); //5
    coordinate.push_back(make_pair(2, 2)); //6
    coordinate.push_back(make_pair(1, 0)); //7
    coordinate.push_back(make_pair(1, 1)); //8
    coordinate.push_back(make_pair(1, 2)); //9
    coordinate.push_back(make_pair(0, 0)); //10
    coordinate.push_back(make_pair(0, 2)); //11
    
    
    for(auto number : numbers)
    {
        if((number == 1) || (number == 4) || (number == 7))
        {
            // 왼손으로 누름
            
            // 버튼 누르고 난 후의 왼손 위치 저장
            leftPos = number;
            answer += "L";
        }
        else if((number == 3) || (number == 6) || (number == 9))
        {
            // 오른손으로 누름
            
            // 버튼 누르고 난 후의 오른손 위치 저장
            rightPos = number;
            answer += "R";
        }
        else
        {
            // 거리 게산해야됨
            
            double distanceLeft = 0;
            double distanceRight = 0;
            
//             distanceLeft = sqrt(pow(abs(coordinate[leftPos].first - coordinate[number].first), 2) + 
//                 pow(abs(coordinate[leftPos].second - coordinate[number].second), 2));
            
//             distanceRight = sqrt(pow(abs(coordinate[rightPos].first - coordinate[number].first), 2) + 
//                 pow(abs(coordinate[rightPos].second - coordinate[number].second), 2));
            
            distanceLeft = abs(coordinate[leftPos].first - coordinate[number].first) + 
                abs(coordinate[leftPos].second - coordinate[number].second);
                
            distanceRight = abs(coordinate[rightPos].first - coordinate[number].first) + 
                abs(coordinate[rightPos].second - coordinate[number].second);
            
            if(distanceLeft > distanceRight)
            {
                // 오른손이 더 가까우므로 오른손 클릭
                rightPos = number;
                answer += "R";
            }
            else if(distanceLeft < distanceRight)
            {
                // 왼손이 더 가까우므로 왼손 클릭
                leftPos = number;
                answer += "L";
            }
            else if(distanceLeft == distanceRight)
            {
                // 거리가 같으므로 왼손잡이 오른손잡이에 따라서 클릭
                
                if(hand == "left")
                {
                    leftPos = number;
                    answer += "L";
                }
                else if(hand == "right")
                {
                    rightPos = number;
                    answer += "R";
                }
            }
        }
    }
    
    
    return answer;
}