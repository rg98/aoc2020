//
// Advent of Code 2020
//       Day 14
//
// © Ralph Ganszky
//

#include <algorithm>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <string>
#include <tuple>
#include <vector>

class WordDelimitedByComma : public std::string {};

static std::istream& operator>>(std::istream& is, WordDelimitedByComma& out) {
    std::getline(is, out, ',');
    return is;
};

template <typename T>
std::ostream& operator<<(std::ostream& os, const std::map<T, T>& m) {
    os << '{'
       << std::accumulate(std::next(m.begin()), m.end(),
                          std::string("(") + std::to_string(m.begin()->first) + ", " +
                              std::to_string(m.begin()->second) + ')',
                          [](std::string a, std::pair<T, T> b) {
                              return std::move(a) + ", (" + std::to_string(b.first) + ", " +
                                     std::to_string(b.second) + ')';
                          })
       << '}';
    return os;
}

int64_t insert_number(const int64_t n, const int64_t turn, std::map<int64_t, int64_t>& nums) {
    auto found = nums.find(n);
    if (found == nums.end()) {
        nums[n] = turn;
        return -1;
    } else {
        auto old_turn = found->second;
        nums[n] = turn;
        return old_turn;
    }
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

    // Read numbers
    std::vector<std::string> s_numbers((std::istream_iterator<WordDelimitedByComma>(in)),
                                       std::istream_iterator<WordDelimitedByComma>());
    std::map<int64_t, int64_t> nums;
    auto last{0LL};
    auto last_num{-1LL};
    for (auto i{0LL}; i < s_numbers.size(); i++) {
        last_num = std::stoll(s_numbers[i]);
        last = insert_number(last_num, i, nums);
    }

    for (auto i = s_numbers.size(); i < 30'000'000; i++) {
        if (last == -1) {
            last = insert_number(0, i, nums);
            last_num = 0;
        } else {
            last_num = nums[last_num] - last;
            last = insert_number(last_num, i, nums);
        }
    }

    std::cout << "num: " << last_num << '\n';

    return 0;
}
