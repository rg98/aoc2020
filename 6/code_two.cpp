//
// Advent of Code 2020
//       Day 6
//
// © Ralph Ganszky
//

#include <cctype>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <vector>

// Check password
//

int count_questions(const std::string& group, const int size) {
    std::map<char, int> questions;
    for (auto c : group)
        if (std::islower(c)) {
            if (questions.find(c) != questions.end())
                questions[c]++;
            else
                questions[c] = 1;
        } else {
            throw std::runtime_error("wrong format in count_question!");
        }
    auto n =
        std::accumulate(questions.begin(), questions.end(), 0, [&](int a, auto& it) -> int {
            return a + ((it.second == size) ? 1 : 0);
        });
    return n;
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

    // Read input file into groups
    std::vector<std::pair<std::string, int>> groups = {std::make_pair("", 0)};
    std::string line;
    while (std::getline(in, line)) {
        if (line.size() > 0)
            groups.back() = std::make_pair(std::get<0>(groups.back()) + line,
                                           std::get<1>(groups.back()) + 1);
        else
            groups.emplace_back(std::make_pair("", 0));
    }

    auto count{0};
    for (auto& group : groups) {
        count += count_questions(std::get<0>(group), std::get<1>(group));
    }

    std::cout << "Sum of all groups: " << count << std::endl;

    return 0;
}
