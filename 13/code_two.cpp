//
// Advent of Code 2020
//       Day 13
//
// © Ralph Ganszky
//
// The idea is from chinese remainder theorem - got implementation from Aetherus from
// exixirforum.com with title "Advent of Code 2020 - Day 13" written in ruby.

#include <algorithm>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <iterator>
#include <numeric>
#include <string>
#include <tuple>
#include <vector>

class WordDelimitedByComma : public std::string {};

static std::istream& operator>>(std::istream& is, WordDelimitedByComma& out) {
    std::getline(is, out, ',');
    return is;
};

std::ostream& operator<<(std::ostream& os, const std::tuple<int64_t, int64_t>& t) {
    os << '(' << std::get<0>(t) << ", " << std::get<1>(t) << ')';
    return os;
}

template <typename T>
std::ostream& operator<<(std::ostream& os, const std::vector<std::tuple<T, T>>& v) {
    os << '{'
       << std::accumulate(std::next(v.begin()), v.end(),
                          std::string("(") + std::to_string(std::get<0>(v.front())) + ", " +
                              std::to_string(std::get<1>(v.front())) + ')',
                          [](std::string a, std::tuple<T, T> b) {
                              return std::move(a) + ", (" + std::to_string(std::get<0>(b)) +
                                     ", " + std::to_string(std::get<1>(b)) + ')';
                          })
       << '}';
    return os;
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

    // Read schedule
    int64_t depart_time;
    std::vector<int64_t> busses;
    std::string line;
    std::getline(in, line);
    depart_time = std::stoll(line);
    std::vector<std::string> s_busses((std::istream_iterator<WordDelimitedByComma>(in)),
                                      std::istream_iterator<WordDelimitedByComma>());
    std::transform(s_busses.begin(), s_busses.end(), std::back_inserter(busses),
                   [](const std::string& s) -> int64_t {
                       int64_t n{0};
                       try {
                           n = std::stoll(s);
                           return n;
                       } catch (std::invalid_argument e) {
                           return -1;
                       } catch (std::out_of_range e) {
                           return -1;
                       }
                   });

    // Use chinese remainder theorem to get the result
    std::vector<std::tuple<int64_t, int64_t>> schedule;
    for (auto i{0}; i < busses.size(); i++) {
        if (busses[i] > 0) {
            if (busses[i] < i) {
                schedule.push_back(std::make_tuple((busses[i] - i) % busses[i], busses[i]));
                std::get<0>(schedule.back()) += busses[i];
            } else
                schedule.push_back(std::make_tuple((busses[i] - i) % busses[i], busses[i]));
        }
    }
    std::sort(schedule.begin(), schedule.end(),
              [](auto& a, auto& b) -> bool { return std::get<0>(a) > std::get<0>(b); });

    std::cout << schedule << '\n';

    auto res = std::accumulate(std::next(schedule.begin()), schedule.end(), schedule.front(),
                               [](auto& a, auto& b) {
                                   auto x = std::get<0>(a);
                                   while (x % std::get<1>(b) != std::get<0>(b))
                                       x += std::get<1>(a);
                                   return std::make_tuple(x, std::get<1>(a) * std::get<1>(b));
                               });
    std::cout << res << '\n';

    return 0;
}
