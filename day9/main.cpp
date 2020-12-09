#include <iostream>
#include <fstream>
#include <vector>
#include <string>

int PREAMBLE_LEN = 25;

using namespace std;

bool validateNumber(vector<long long int> numbersArray, int numberIndex){
    for(int i = numberIndex - 1; i > numberIndex - PREAMBLE_LEN; i--){
        for(int y = i - 1; y >= numberIndex - PREAMBLE_LEN; y--)
            if (numbersArray.at(i) + numbersArray.at(y) == numbersArray.at(numberIndex))return true;
    }
    return false;
}

int main(){

    vector<long long int> numbers;

    ifstream input("data.txt");
    
    if(input.is_open()){
        string inputLine;
        while(getline(input, inputLine)){
            numbers.push_back(stoll(inputLine));
        }
    }

    input.close();

    int f;
    for(f=PREAMBLE_LEN; f<numbers.size(); f++){
        if(!validateNumber(numbers, f))break;
    }

    long long int sum;
    long long int lownum, hinum;
    for(auto i = numbers.begin(); i<numbers.end() - 1; i++){
        sum = lownum = hinum = *i;
        auto y = i+1;
        for(y; y<numbers.end(); y++){
            sum += *y;
            if(*y>hinum)hinum = *y;
            if(*y<lownum)lownum = *y;
            if(sum>=numbers.at(f))break;
        }
        if(sum==numbers.at(f)){
            break;
        }
    }

    cout<<"Here are the results!\n";
    cout<<numbers.at(f)<<endl;
    cout<<lownum<<"+"<<hinum<<"="<<lownum+hinum;

    return 0;
}