#include <iostream>
#include <vector>
#include <stdio.h>      /* printf, fgets */
#include <stdlib.h>     /* atoi */

#include "utils.h"


int main(int argc, char **argv) {
    // Test 1
    int a = 1;
    int b = 2;
    std::cout << "Dummy sum: " << std::to_string(dummy_sum(a, b)) << "\n" << std::endl;


    // Test 2
    float arr_v[] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0};
    int arr_d[] = {3, 2};
    int size_dim = 2;
    float sum = array_sum(arr_v, arr_d, size_dim);
    std::cout << "Array sum: " << std::to_string(sum)<< "\n" << std::endl;

    // Test 3
    std::vector<int> arr2;
    for(int i = 1; i<argc; ++i){
        int temp = atoi(argv[i]);
        arr2.push_back(temp);
    }
    int size = (int)arr2.size();
    std::cout << "Args sum: " << fast_sum(arr2, size) << std::endl;

    return 0;
}