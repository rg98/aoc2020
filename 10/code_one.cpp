//
// Advent of Code 2020
//       Day 10
//
// © Ralph Ganszky
//

#include <filesystem>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <vector>

std::map<int64_t, int64_t> count_differences(const std::vector<int64_t>& numbers) {
    std::map<int64_t, int64_t> differences = {{1, 0}, {3, 0}};
    auto nums = numbers;
    nums.push_back(0);
    std::sort(nums.begin(), nums.end());
    nums.push_back(nums.back() + 3);
    auto last = nums.front();
    std::for_each(std::next(nums.begin()), nums.end(), [&](auto n) {
        differences[n - last]++;
        last = n;
    });
    return differences;
}

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

    // Read adapters
    std::vector<int64_t> numbers;
    std::string line;
    while (std::getline(in, line)) {
        auto num = std::stoll(line);
        numbers.push_back(num);
    }

    auto differences = count_differences(numbers);
    std::cout << differences[1] * differences[3] << '\n';

    return 0;
}
