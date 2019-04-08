//
// Created by Salva Carrión on 2019-04-05.
//

#ifndef NUMPY2C_WRAPPER_H
#define NUMPY2C_WRAPPER_H

#include "item.h"
#include "container.h"

#ifdef __cplusplus
extern "C"
{
#endif

// Item object
Item* Item_init(int id, const char* name);
const char* Item_getName(Item* item);

// Container object
Container* Container_init();
int Container_addItem(Container* container, Item* item);
Item* Container_getItem(Container* container, int id);

#ifdef __cplusplus
}
#endif

#endif //NUMPY2C_WRAPPER_H
