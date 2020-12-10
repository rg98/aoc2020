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

std::tuple<std::vector<int64_t>::iterator, std::vector<int64_t>::iterator>
search_n(int64_t num, std::vector<int64_t>& numbers) {
    std::vector<int64_t>::iterator begin = numbers.begin();
    std::vector<int64_t>::iterator end = std::next(std::next(begin));
    while (std::accumulate(begin, end, 0) != num) {
        if (std::accumulate(begin, end, 0) < num)
            end++;
        else
            begin++;
    }
    return std::make_tuple(begin, end);
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

    // Read code
    std::vector<int64_t> numbers;
    std::string line;
    int64_t sum_of_nums{144381670};
    while (std::getline(in, line)) {
        auto num = std::stoll(line);
        if (num >= sum_of_nums)
            break;
        numbers.push_back(num);
    }

    auto res = search_n(sum_of_nums, numbers);
    auto minmax = std::minmax_element(std::get<0>(res), std::get<1>(res));
    std::cout << *std::get<0>(minmax) + *std::get<1>(minmax) << '\n';

    return 0;
}
