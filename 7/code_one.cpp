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

int count_questions(const std::string& group) {
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
    return questions.size();
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

    // Read input file into maze
    std::vector<std::string> groups = {""};
    std::string line;
    while (std::getline(in, line)) {
        if (line.size() > 0)
            groups.back() += line;
        else
            groups.push_back("");
    }

    auto count{0};
    for (auto& group : groups) {
        count += count_questions(group);
    }

    std::cout << "Sum of all groups: " << count << std::endl;

    return 0;
}
