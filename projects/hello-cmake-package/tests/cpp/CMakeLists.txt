cmake_minimum_required(VERSION 3.14...3.19)

project(hello-user VERSION 0.1.0)

find_package(hello REQUIRED)

add_executable(hello_user "${PROJECT_SOURCE_DIR}/test.cpp")
target_link_libraries(hello_user PRIVATE hello::hello)

include(CTest)

add_test(NAME hello_test COMMAND hello_user)
