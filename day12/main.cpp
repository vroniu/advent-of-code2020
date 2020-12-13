#include <iostream>
#include <fstream>

using namespace std;

enum Direction{
    N, E, S, W
};

struct Ship{
    //positive is north, negative is south
    int northSouthAxis;
    //positive is west, negative is east
    int westEastAxis;

    Direction direction;

    //positive is north, negative is south
    int waypointNorthSouthAxis;
    //positive is west, negative is east
    int waypointWestEastAxis;

    Ship(){
        this->direction = E;
        this->northSouthAxis = 0;
        this->westEastAxis = 0;
        this->waypointNorthSouthAxis = 1;
        this->waypointWestEastAxis = -10;
    }

    void rotateWaypointRight(){
        int tmp = this->waypointNorthSouthAxis;
        this->waypointNorthSouthAxis = this->waypointWestEastAxis;
        this->waypointWestEastAxis = tmp * (-1);
    }

    void rotateWaypointLeft(){
        int tmp = this->waypointNorthSouthAxis;
        this->waypointNorthSouthAxis = this->waypointWestEastAxis * (-1);
        this->waypointWestEastAxis = tmp;
    }

    void executeOrder(string order){
        char action = order.at(0);
        int units = stoi(order.substr(1));
        switch (action) {
            case 'N':
                this->northSouthAxis += units;
                break;
            case 'S':
                this->northSouthAxis -= units;
                break;
            case 'E':
                this->westEastAxis -= units;
                break;
            case 'W':
                this->westEastAxis += units;
                break;
            case 'L': {
                //Using the fact that enums have indexes i came up with this (looks a little bit messy because there is a possibility of a negative number)
                this->direction = (this->direction - units/90) < 0 ? static_cast<Direction>(4 + (this->direction - units/90)) : static_cast<Direction>(this->direction - units/90);
                break;
            }
            case 'R': {
                //This uses the same method but came out cleaner
                this->direction = static_cast<Direction>((this->direction + units / 90) % 4);
                break;
            }

            case 'F':
                switch (this->direction) {
                    case E:
                        this->westEastAxis -= units;
                        break;
                    case W:
                        this->westEastAxis += units;
                        break;
                    case S:
                        this->northSouthAxis -= units;
                        break;
                    case N:
                        this->northSouthAxis += units;
                        break;
                }
                break;

        }
    }

    void executeOrderWithWaypoint(string order){
        char action = order.at(0);
        int units = stoi(order.substr(1));
        switch (action) {
            case 'N':
                this->waypointNorthSouthAxis += units;
                break;
            case 'S':
                this->waypointNorthSouthAxis -= units;
                break;
            case 'E':
                this->waypointWestEastAxis -= units;
                break;
            case 'W':
                this->waypointWestEastAxis += units;
                break;
            case 'L': {
                for(int i = 0; i<units/90; i++){
                    this->rotateWaypointLeft();
                }
                break;
            }
            case 'R': {
                for(int i = 0; i<units/90; i++){
                    this->rotateWaypointRight();
                }
                break;
            }

            case 'F':
                this->northSouthAxis += this->waypointNorthSouthAxis * units;
                this->westEastAxis += this->waypointWestEastAxis * units;
                break;

        }
    }

};

int main() {

    ifstream input("data.txt");

    Ship ship1, ship2;

    if(input.is_open()){
        string line;
        while(getline(input, line)){
            ship1.executeOrder(line);
            ship2.executeOrderWithWaypoint(line);
        }

    }

    input.close();

    cout<<abs(ship1.westEastAxis) + abs(ship1.northSouthAxis)<<endl;
    cout<<abs(ship2.westEastAxis) + abs(ship2.northSouthAxis)<<endl;

}
