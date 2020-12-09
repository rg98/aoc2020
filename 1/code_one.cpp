//
// Advent of Code 2020
//       Day 1
//
// © Ralph Ganszky
//

#include <filesystem>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int find_match(const std::vector<int32_t>& numbers) {
    for (auto i{0}; i < numbers.size() - 1; i++) {
        for (auto j{i + 1}; j < numbers.size(); j++) {
            if (numbers[i] + numbers[j] == 2020) {
                return numbers[i] * numbers[j];
            }
        }
    }
    return -1;
}

int main(int argc, char* argv[]) {
    std::vector<int32_t> numbers;

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

    // Read input file into numbers
    std::vector<std::string> in_str;
    std::string line;
    while (std::getline(in, line)) {
        numbers.push_back(std::stoi(line));
    }

    std::cout << "Product of the matching numbers: " << find_match(numbers) << std::endl;

    return 0;
}
