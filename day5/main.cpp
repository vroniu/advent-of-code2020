#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

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

int main(){

    ifstream input("data.txt");

    vector<charQueue> * data = new vector<charQueue>();
    bool* taken_seats = new bool[128 * 8];   //the size is kidna overkill but it works

    //INPUT
    if (input.is_open()){
        string line;
        while(getline(input, line)){
            data->push_back(charQueue(line));
        }
    }

    input.close();

    unsigned int max_seat_id = 0;

    //"Binary division" algorithm
    for(auto seatBinData = data->begin(); seatBinData < data->end(); seatBinData++){
        unsigned int down_range = 0, up_range = 127;
        for(int i = 0; i<7; i++){
            if(seatBinData->pop()=='F'){
                up_range = (down_range + up_range) / 2;
            } else {
                //need to add one when calculating down range
                down_range = (down_range + up_range + 1) / 2;
            }
        }

        unsigned int seat_row = up_range;
        
        down_range = 0; up_range = 7;
        for(int i = 0; i<3; i++){
            if(seatBinData->pop()=='R'){
                //need to add one when calculating down range
                down_range = (down_range + up_range + 1) / 2;
            } else {
                up_range = (down_range + up_range) / 2;
            }
        }
        unsigned int seat_col = up_range;

        //Calculate the ID
        unsigned int seat_id = seat_row * 8 + seat_col;
        taken_seats[seat_id] = true;
        if(seat_id>max_seat_id){
            max_seat_id = seat_id;
        }
    }

    //Part two
    unsigned int your_id = 0;
    for(int i = 8; i<max_seat_id; i++){
        //Find a seat that isnt taken, but neighbour seats are taken
        if(taken_seats[i]==false && taken_seats[i-1]==true && taken_seats[i+1]==true){
            your_id = i;
        }
    }

    cout<<"Here are the results!"<<endl;
    cout<<max_seat_id<<endl;
    cout<<your_id;

}