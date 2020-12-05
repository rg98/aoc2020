#
# Makefile for aoc2020
#
# © Ralph Ganszky 12/2020
#

CXX           = clang++

CXXFLAGS      = -g -Os -fno-omit-frame-pointer -fno-optimize-sibling-calls \
                -std=c++17 -Wall 

LDFLAGS       = 

SRCS          = $(wildcard *.cpp)

DEPENDFILE    = .depend

OBJS          = $(SRCS:.cpp=.o)

all:    code_one code_two

code_one: code_one.o
	@echo "Building ... code_one"
	@$(CXX) $(CXXFLAGS) code_one.o -o code_one $(LDFLAGS)

code_two: code_two.o
	@echo "Building ... code_two"
	@$(CXX) $(CXXFLAGS) code_two.o -o code_two $(LDFLAGS)

depend: $(SRCS)
	$(CXX) $(CXXFLAGS) -MM $(SRCS) > $(DEPENDFILE)

clean:
	rm -f code_one code_two  $(OBJS) core perf.data*

-include $(DEPENDFILE)

