#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

struct operation{
    string opcode;
    int arg;
    bool run;

    operation(string opcode, string signedArg){
        this->opcode = opcode;
        this->arg = stoi(signedArg.substr(1));
        if (signedArg.at(0)=='-') arg *= -1;
        run = false;
    }

};

int runOperations(vector<operation> ops, unsigned int &PC, unsigned int &ACC){
    while(1){
        //Return 0 if terminated correctly
        if (PC >= ops.size()) return 0;
        //Return 0 if looping
        else if(ops.at(PC).run==true) return 1;
        else {
            ops.at(PC).run = true;
            operation currOp = ops.at(PC);
            if(currOp.opcode=="nop"){
                PC++;
            }
            else if (currOp.opcode=="acc"){
                ACC += currOp.arg;
                PC++;
            } else if (currOp.opcode=="jmp"){
                PC += currOp.arg;
            }
        }
    }
}

vector<operation> vecCopy(vector<operation> src){
    vector<operation> newVec;
    for(int i = 0; i< src.size(); i++){
        newVec.push_back( src.at(i) );
    }
    return newVec;
}


int main(){

    //Input
    ifstream input("data.txt");

    vector<operation> ops;
    
    if(input.is_open()){
        while(!input.eof()){
            string opcode, arg;
            input>>opcode>>arg;
            ops.push_back(operation(opcode, arg));
        }
    }

    input.close();

    //Part one - run the file and show the ACC register
    unsigned int PC = 0, ACC = 0;
    runOperations(ops, PC, ACC);

    cout<<"Here are the results!\n";
    cout<<ACC<<endl;

    //Part two
    //Check every nop and jmp line
    for(int i = 0; i< ops.size(); i++){
        if (ops.at(i).opcode == "nop"){
            //Create a new list of operations with replaced opcode
            vector<operation> opsReplaced = vecCopy(ops);
            opsReplaced.at(i).opcode = "jmp";
            PC = 0; ACC = 0;
            //if runOperations returns 0, the instructions are valid - stop the search
            if(runOperations(opsReplaced, PC, ACC)==0)
                break;
        } else if(ops.at(i).opcode == "jmp"){
            //Create a new list of operations with replaced opcode
            vector<operation> opsReplaced = vecCopy(ops);
            opsReplaced.at(i).opcode = "nop";
            PC = 0; ACC = 0;
            //if runOperations returns 0, the instructions are valid - stop the search
            if(runOperations(opsReplaced, PC, ACC)==0)
                break;
        }
    }

    cout<<ACC;

    return 0;
}