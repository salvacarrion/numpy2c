#include <utility>

//
// Created by Salva Carrión on 2019-04-05.
//

#include "item.h"

#ifdef __cplusplus
extern "C"
{
#endif

Item::Item(int id, std::string name) {
    this->id = id;
    this->name = std::move(name);
}

std::string Item::getName(){
    return this->name;
}

int Item::getID(){
    return this->id;
}

#ifdef __cplusplus
}



#endif