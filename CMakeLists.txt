CMAKE_MINIMUM_REQUIRED(VERSION 2.8.3)
PROJECT(deploy_tvm)

SET(CMAKE_BUILD_TYPE Release)
set(CMAKE_C_COMPILER "/usr/bin/gcc")
SET(CMAKE_C_FLAGS ${CMAKE_C_FLAGS} "-std=c99")
SET(CMAKE_CXX_FLAGS ${CMAKE_CXX_FLAGS} "-std=c++0x")

FIND_PACKAGE(OpenCV 3 REQUIRED)


# include and libs path
SET(HOME /home/pzq)
SET(OpenCV_INCLUDE_DIRS ${OpenCV_INCLUDE_DIRS} /home/pzq/local/include)
SET(OpenCV_LIBRARY_DIRS ${OpenCV_LIBRARY_DIRS} /home/pzq/local/lib)

SET(INCLUDE_PATH ./include /usr/include /usr/local/include  
                ${OpenCV_INCLUDE_DIRS} ${OpenCV_INCLUDE_DIRS}/opencv)
SET(LINK_PATH ./lib /usr/local/lib 
                ${OpenCV_LIBRARY_DIRS})

INCLUDE_DIRECTORIES(${INCLUDE_PATH})
LINK_DIRECTORIES(${LINK_PATH})


# get executable file
ADD_EXECUTABLE(patchmatchs ./src/main.cpp ./src/inpaint.cpp ./src/maskedimage.cpp ./src/nearestneighborfield.cpp ./src/qualitymesures.cpp)
TARGET_LINK_LIBRARIES(patchmatchs opencv_core opencv_imgproc opencv_highgui)
ADD_EXECUTABLE(patchmatch ./src/main_simple.cpp ./src/inpaint.cpp ./src/maskedimage.cpp ./src/nearestneighborfield.cpp ./src/qualitymesures.cpp)
TARGET_LINK_LIBRARIES(patchmatch opencv_core opencv_imgproc opencv_highgui)