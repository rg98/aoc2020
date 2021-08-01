//
// Advent of Code 2020
//       Day 11
//
// © Ralph Ganszky
//

#include <filesystem>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

enum class Seat : int8_t { Empty, Free, Occupied };

int main(int argc, char* argv[]) {
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

    // Read layout
    std::vector<std::vector<Seat>> seats;
    std::string line;
    while (std::getline(in, line)) {
        seats.emplace_back(std::vector<Seat>);
        seats.back().reserve(line.size());
        std::transform(
            line.begin(), line.end(), seats.back().begin(), [&](const char a) -> Seat {
                if (a == '.')
                    return Seat::Empty;
                else if (a == 'L')
                    return Seat::Free;
                else if (a == '#')
                    return Seat::Occupied;
                else
                    throw std::runtime_error(std::string("Unknown Seat code ") + a + "!");
            });
    }

    auto count{0LL};

    std::cout << count << " seats are occupied\n";

    return 0;
}
