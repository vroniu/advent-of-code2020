#include <iostream>
#include <fstream>
#include <vector>
#include <string>

#define TREE '#'

using namespace std;

//The algoritm
unsigned long calculate_slope(vector<string>* lines, unsigned int hor, unsigned int ver){
    unsigned int line_lenght = lines->front().length();
    unsigned long result = 0;
    unsigned int coord_h = 0;
    for(int i = 0; i < lines->size(); i += ver){
        if(lines->at(i).at(coord_h) == TREE)result++;
        coord_h = (coord_h + hor) % line_lenght;
    }
    return result;
}

int main(){

    //INPUT
    ifstream input("data.txt");

    vector<string>* lines = new vector<string>();

    if(input.is_open()){
        string line;
        while(getline(input, line)){
            lines->push_back(line);
        }
    }

    //Calculate the slopes
    unsigned int* answers = new unsigned int [5];
    answers[0] = calculate_slope(lines, 1, 1);
    answers[1] = calculate_slope(lines, 3, 1);
    answers[2] = calculate_slope(lines, 5, 1);
    answers[3] = calculate_slope(lines, 7, 1);
    answers[4] = calculate_slope(lines, 1, 2);

    //This result is quite big, needs to be stored in a long long
    unsigned long long result_two = 1;
    for(int i = 0; i<5; i++){
        result_two *= answers[i];
    }

    cout<<"Here are the results!"<<endl<<answers[1]<<endl<<result_two;


}