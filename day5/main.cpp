#include <iostream>
#include <fstream>
#include <string>
#include <vector>

struct charQueue{
    string data;
    unsigned int id;

    charQueue(string line){
        id = 0;
        this->data = line;
    }

    char pop(){
        return this->data.at(id++);
    }
};

using namespace std;

int main(){

    ifstream input("example.txt");

    vector<charQueue> * data = new vector<charQueue>();

    if (input.is_open()){
        string line;
        while(getline(input, line)){
            data->push_back(charQueue(line));
        }
    }

    input.close();
}