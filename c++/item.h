//
// Created by Salva Carrión on 2019-04-05.
//

#ifndef NUMPY2C_ITEM_H
#define NUMPY2C_ITEM_H

#include <string>

class Item {
public:
    Item(int id, std::string name);
    std::string getName();
    int getID();
private:
    std::string name;
    int id;
};


#endif //NUMPY2C_ITEM_H
