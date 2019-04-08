#include <iostream>
#include <vector>
#include <stdio.h>      /* printf, fgets */
#include <stdlib.h>     /* atoi */
#include <string>

#include "utils.h"
#include "wrapper.h"
#include "container.h"
#include "item.h"


int main(int argc, char **argv) {
//    // Test 1
//    int a = 1;
//    int b = 2;
//    std::cout << "Dummy sum: " << std::to_string(dummy_sum(a, b)) << "\n" << std::endl;
//
//    int c;
//    c = a+ b;
//
//    // Test 2
//    float arr_v[] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0};
//    int arr_d[] = {3, 2};
//    int size_dim = 2;
//    float sum = array_sum(arr_v, arr_d, size_dim);
//    float sum2 = array_sum_p(arr_v, arr_d, size_dim);
//    std::cout << "Array sum: " << std::to_string(sum) << std::endl;
//    std::cout << "Array sum (v2): " << std::to_string(sum2) << std::endl;
//
//    // Test 3
//    std::cout << "Args sum: " << fast_sum(arr_v, 6) << std::endl;
//
//    // Test 3
//    std::cout << "Sum of two vectors bit-wise: " << fast_sum(arr_v, 6) << std::endl;
//    int size = 3;
//    auto *v = new float[size]{1, 2, 3};
//    auto *w = new float[size]{4, 5, 6};
//    float *bw_sum = sum_vector_bw(v, w, 3);
//    for(int i = 0; i<size; ++i){
//        std::cout << bw_sum[i] << std::endl;
//    }

//    Container c;

//    Item* item1 = new Item(10, std::string("Item 10X"));
//    Item* item2 = new Item(2, std::string("Item 2"));
//    Item* item3 = new Item(3, std::string("Item 3"));
//    Item* item4 = new Item(4, std::string("Item 4"));
//
//    std::cout << "New item: " << c.addItem(item1) << std::endl;
//    std::cout << "New item: " << c.addItem(item2) << std::endl;
//    std::cout << "New item: " << c.addItem(item4) << std::endl;
//    std::cout << "New item: " << c.addItem(item3) << std::endl;
//
//    std::cout << "Get item: " << c.getItem(10)->getName() << std::endl;
//    std::cout << "Get item: " << c.getItem(2)->getName() << std::endl;
//    std::cout << "Get item: " << c.getItem(3)->getName() << std::endl;
//    std::cout << "Get item: " << c.getItem(4)->getName() << std::endl;


//    const char* name_item_w1 = "My special item";
//    std::string str_name_w1(name_item_w1);
//    std::cout << "Wrapper item: " << str_name_w1 << std::endl;

    Item* item_w1 = Item_init(1, "My funny item 1");
    const char* name_item1 = Item_getName(item_w1);
    std::cout << "Wrapper item: " << name_item1 << std::endl;

    Item* item_w2 = Item_init(2, "My funny item 2");
    const char* name_item2 = Item_getName(item_w2);
    std::cout << "Wrapper item: " << name_item2 << std::endl;

    Container* c = Container_init();
    Container_addItem(c, item_w1);
    Container_addItem(c, item_w2);

    Item* ic_1 = c->getItem(1);
    Item* ic_2 = c->getItem(2);

    std::cout << "Wrapper container item 1: " << ic_1->getName() << std::endl;
    std::cout << "Wrapper container item 2: " << ic_2->getName() << std::endl;
    return 0;
}