#include "hello.h"
#include <iostream>

namespace hello {
void hello() {
    std::cout << "Hello, World!" << std::endl;
}
int return_two() {
    return 2;
}
} // end ns hello
