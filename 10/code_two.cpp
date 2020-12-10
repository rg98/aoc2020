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

inline int64_t ipower(int64_t b, int64_t e) {
    int64_t p{1LL};
    for (auto i{0}; i < e; i++)
        p *= b;
    return p;
}

int64_t count_comninations(const std::vector<int64_t>& numbers) {
    auto nums = numbers;
    nums.push_back(0);
    std::sort(nums.begin(), nums.end());
    nums.push_back(nums.back() + 3);

    std::map<int64_t, int64_t> cc_count = {{1, 0}, {2, 0}, {3, 0}, {4, 0}, {5, 0}};
    std::map<int64_t, int64_t> cc_factor = {{1, 1}, {2, 2}, {3, 4}, {4, 7}, {5, 12}};

    int64_t count{0};
    auto last = nums.front();
    std::for_each(std::next(nums.begin()), nums.end(), [&](auto n) {
        if (n - last == 1)
            count += 1;
        else {
            if (count > 0)
                cc_count[count]++;
            count = 0;
        }
        last = n;
    });

    int64_t combinations = 1LL;
    for (auto& e : cc_count) {
        combinations *= ipower(cc_factor[e.first], e.second);
    }
    return combinations;
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

    auto comninations = count_comninations(numbers);
    std::cout << comninations << '\n';

    return 0;
}
