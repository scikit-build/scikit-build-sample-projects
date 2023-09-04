
int my_c_func(int* int32_array, int num_items){
    int result = 0;
    for (int i = 0; i < num_items; i++){
        result += int32_array[i];
    }
    return result;
}
