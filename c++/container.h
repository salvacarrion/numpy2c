//
// Created by Salva Carrión on 2019-04-05.
//

#ifndef NUMPY2C_CONTAINER_H
#define NUMPY2C_CONTAINER_H

#include <vector>
#include "item.h"

class Container {
public:
    int addItem(Item* item);
    Item* getItem(int id);
private:
    std::vector<Item*> items;
};


#endif //NUMPY2C_CONTAINER_H
