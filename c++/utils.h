#ifndef UTILS_H
#define UTILS_H

#include <vector>

#ifdef __cplusplus
extern "C"
{
#endif

int dummy_sum(int a, int b);
float array_sum(float arr[], int dim[], int size_dim);
float array_sum_p(float *arr, int *dim, int size_dim);
int fast_sum(float *arr, int size);
float* sum_vector_bw(float *a, float *b, int size);

#ifdef __cplusplus
}
#endif

#endif // UTILS_H