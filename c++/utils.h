#ifndef UTILS_H
#define UTILS_H

#include <vector>

#ifdef __cplusplus
extern "C"
{
#endif

int dummy_sum(int a, int b);
float array_sum(float arr[], int dim[], int size_dim);
int fast_sum(std::vector<int> arr, int size);

#ifdef __cplusplus
}
#endif

#endif // UTILS_H