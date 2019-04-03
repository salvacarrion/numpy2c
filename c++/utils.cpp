//
// Created by Salva Carrión on 02/04/2019.
//

#include "utils.h"

//#include <iostream>
//#include <string>

int dummy_sum(int a, int b){
    return a + b;
}

float array_sum(float arr[], int dim[], int size_dim){
    float s = 0;
    int arr_size=1;
//    std::cout << "Size dim: " << size_dim << std::endl;

//    std::string str_dim = "{";
    for(int i = 0; i < size_dim; ++i){
//        str_dim += std::to_string(dim[i]);
        arr_size *= dim[i];
//        if (i+1 == size_dim) { str_dim += "}";}
//        else {str_dim += ", "; }
    }
    //std::cout << "Dim: " << str_dim << std::endl;


//    std::string str_arr = "{";
    for(int i = 0; i < arr_size; ++i){
        s += arr[i];
//        str_arr += std::to_string(arr[i]);
//        if (i+1 == arr_size) { str_arr += "}";}
//        else {str_arr += ", "; }
    }
//    std::cout << "Arr: " << str_arr << std::endl;

    return s;
}

int fast_sum(const std::vector<int> arr, int size){
    int s = 0;
    for (int i : arr) {
        s += i;
    }
    return s;
}
