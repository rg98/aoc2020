//
// Advent of Code 2020
//       Day 13
//
// © Ralph Ganszky
//

#include <algorithm>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

class WordDelimitedByComma : public std::string {};

static std::istream& operator>>(std::istream& is, WordDelimitedByComma& out) {
    std::getline(is, out, ',');
    return is;
};

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
    std::vector<std::tuple<int64_t, int64_t>> schedule;
    for (auto& n : busses) {
        if (n > 0) {
            schedule.push_back(std::make_tuple(n * ((depart_time / n) + 1), n));
        }
    }
    std::nth_element(
        schedule.begin(), schedule.begin(), schedule.end(),
        [](std::tuple<int64_t, int64_t> a, std::tuple<int64_t, int64_t> b) -> bool {
            return std::get<0>(a) < std::get<0>(b);
        });
    std::cout << std::get<1>(schedule.front()) * (std::get<0>(schedule.front()) - depart_time)
              << '\n';
    return 0;
}
