//
// Created by Salva Carrión on 2019-04-05.
//

#include "wrapper.h"

// Item
Item* Item_init(int id, const char* name){
    std::string name_str(name);
    return new Item(id, name_str);
}

const char* Item_getName(Item* item){
    char* result = new char[item->getName().length() + 1];
    strcpy(result, item->getName().c_str());

    return result;
}


// Container
Container* Container_init(){
    return new Container();
}

int Container_addItem(Container* container, Item* item){
    return container->addItem(item);
}

Item* Container_getItem(Container* container, int id){
    return container->getItem(id);
}

