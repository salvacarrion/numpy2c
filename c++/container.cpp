//
// Created by Salva Carrión on 2019-04-05.
//

#include "container.h"


int Container::addItem(Item* item){
    this->items.push_back(item);
    return item->getID();
}

Item* Container::getItem(int id){
    for(int i = 0; i < this->items.size(); ++i){
        if(this->items[i]->getID()==id){
            return this->items[i];
        }
    }
    return nullptr;
}


