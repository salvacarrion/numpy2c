//
// Created by Salva Carrión on 02/04/2019.
//

#include "utils.h"

#include <iostream>
//#include <string>

int dummy_sum(int a, int b){
    return a + b;
}

float array_sum(float arr[], int dim[], int size_dim){
    float s = 0;
    int arr_size=1;

    // Get dimension
    for(int i = 0; i < size_dim; ++i){
        arr_size *= dim[i];
    }


    // Sum array
    for(int i = 0; i < arr_size; ++i){
        s += arr[i];
    }

    return s;
}

float array_sum_p(float *arr, int *dim, int size_dim){
    float s = 0;
    int arr_size=1;

    // Get dimension
    for(int i = 0; i < size_dim; ++i){
        arr_size *= dim[i];
    }

    // Sum array
    for(int i = 0; i < arr_size; ++i){
        s += arr[i];
    }

    return s;
}

int fast_sum(float *arr, int size){
    int s = 0;
    for(int i = 0; i < size; ++i){
        s += i;
    }
    return s;
}

float* sum_vector_bw(float *a, float *b, int size){
    float* c = new float[size];
    for (int i = 0; i < size; ++i){
        c[i] = a[i] + b[i];
    }
    return c;
}