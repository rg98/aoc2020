//
// Advent of Code 2020
//       Day 9
//
// © Ralph Ganszky
//

#include <filesystem>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

template <typename T>
std::ostream& operator<<(std::ostream& os, const std::vector<T>& v) {
    static_assert(std::is_integral<T>::value, "Integral type required");
    os << '{'
       << std::accumulate(
              std::next(v.begin()), v.end(), std::to_string(v.front()),
              [](std::string a, T b) { return std::move(a) + ", " + std::to_string(b); })
       << '}';
    return os;
}

bool check_sum(int64_t num, const std::vector<int64_t>& numbers) {
    auto nums = numbers;
    std::sort(nums.begin(), nums.end());
    auto left = nums.begin();
    auto right = std::prev(nums.end());
    while (left != right && (*left + *right) != num) {
        if (*left + *right > num)
            right--;
        else
            left++;
    }
    return left != right;
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

    // Read program
    std::vector<int64_t> numbers;
    std::string line;
    while (std::getline(in, line)) {
        auto num = std::stoll(line);
        if (numbers.size() == 25) {
            if (!check_sum(num, numbers)) {
                std::cout << num << '\n';
                break;
            }
            numbers.erase(numbers.begin());
        }
        numbers.push_back(num);
    }

    return 0;
}
