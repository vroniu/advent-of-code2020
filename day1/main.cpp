#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

const int TARGET = 2020;

unsigned int basic_one(vector<int>* l){
    for( int i =0 ; i< l->size(); i++){
        for( int y = i + 1; y < l->size(); y++){
            if (l->at(i) + l->at(y) == TARGET){
                return l->at(i) * l->at(y);
            }
        }
    }
}

unsigned int basic_two(vector<int>* l){
    for( int i =0 ; i< l->size(); i++){
        for( int y = i + 1; y < l->size(); y++){
            for(int x = y + 1; x < l->size(); x++){
                if (l->at(i) + l->at(y) + l->at(x) == TARGET){
                    return (l->at(i) * l->at(y) * l->at(x));
                }
            }
        }
    }
}

int main(){

    ifstream input("data.txt");

    vector<int>* nums = new vector<int>();

    if(input.is_open()){
        string rline;
        while(getline(input, rline)){
            nums->push_back(int(stoi(rline)));
        }
    }

    cout<<basic_one(nums) << endl << basic_two(nums) ;

    return 0;
}