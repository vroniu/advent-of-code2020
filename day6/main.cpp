#include <iostream>
#include <fstream>
#include <string>

const unsigned int NUM_OF_QUESTIONS = 26;

using namespace std;

int main(){

    ifstream input("data.txt");

    unsigned int questions_answered_sum = 0;
    unsigned int questions_all_answered_sum = 0;
    unsigned int people_in_group = 0;
    unsigned int * questions_answered_group = new unsigned int[NUM_OF_QUESTIONS];
    for(int i = 0; i<NUM_OF_QUESTIONS; i++){
        questions_answered_group[i] = 0;
    }

    if(input.is_open()){
        string line;
        while(getline(input, line)){
            if(line.empty()){
                for(int i = 0; i<NUM_OF_QUESTIONS; i++){
                    //If at least one person answered yes, add to the first result
                    if(questions_answered_group[i]>0){
                        questions_answered_sum++;
                    }
                    //If all the people answered yes, add to the second result
                    if(questions_answered_group[i]==people_in_group){
                        questions_all_answered_sum++;
                    }
                    //Reset the array
                    questions_answered_group[i] = 0;
                }
                //Reset the number of people
                people_in_group = 0;
            } else {
                for(int i = 0; i<line.size(); i++){
                    questions_answered_group[line.at(i) - 97]++;
                }
                people_in_group++;
            }
        }
        //Add the last group to sum
        for(int i = 0; i<NUM_OF_QUESTIONS; i++){
            //If at least one person answered yes, add to the first result
            if(questions_answered_group[i]>0){
                questions_answered_sum++;
            }
            //If all the people answered yes, add to the second result
            if(questions_answered_group[i]==people_in_group){
                questions_all_answered_sum++;
            }
        }
    }

    input.close();
    cout<<"Here are the results!"<<endl;
    cout<<questions_answered_sum<<endl;
    cout<<questions_all_answered_sum;

    return 0;
}