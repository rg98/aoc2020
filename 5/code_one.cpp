//
// Advent of Code 2020
//       Day 5
//
// © Ralph Ganszky
//

#include <filesystem>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

// decode seat decodes the bits of the resulting number by using the fact,
// that the third bit has the inverse value of the resulting bit in the
// seat id:
// 'F' = 1000(1)10
// 'B' = 1000(0)10
// 'L' = 1001(1)00
// 'R' = 1010(0)10

int32_t decode_seat(const std::string& code) {
    int32_t seat =
        std::accumulate(code.cbegin(), code.cend(), 0, [&](int32_t a, const char b) -> int32_t {
            return (a << 1) | ((~b & 0x4) >> 2);
        });
    return seat;
}

int main(int argc, char* argv[]) {
    std::vector<int32_t> occupied;

    // Determine input filename - default in.txt
    std::string in_name = "in.txt";
    if (argc > 1) {
        if (std::filesystem::exists(argv[1])) {
            in_name = argv[1];
        }
    }
    std::filesystem::path input_path(in_name);
    std::ifstream in(input_path);
    if (!in.is_open())
        throw std::runtime_error(std::string("Can't open ") + input_path.string() +
                                 " for reading!");

    // Read input file into occupied - last line always empty
    std::vector<std::string> in_str;
    while (!in.eof()) {
        std::string line;
        std::getline(in, line);
        auto seat = decode_seat(line);
        occupied.push_back(seat);
    }
    occupied.pop_back();

    // Return max element of occupied
    std::cout << "Highest Seat ID: " << *std::max_element(occupied.begin(), occupied.end())
              << std::endl;

    return 0;
}
