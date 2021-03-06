//
// Advent of Code 2020
//       Day 2
//
// © Ralph Ganszky
//

#include <filesystem>
#include <fstream>
#include <iostream>
#include <numeric>
#include <regex>
#include <string>
#include <vector>

// Check password
//
// return 1 if valid and 0 if not

int check_password(int low, int high, char c, const std::string& password) {
    auto count = std::accumulate(password.begin(), password.end(), 0,
                                 [&](const int a, const char b) -> int {
                                     if (b == c)
                                         return a + 1;
                                     return a;
                                 });
    if (low <= count && count <= high)
        return 1;
    return 0;
}

int main(int argc, char* argv[]) {
    auto valid_passwords{0};

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

    // Read password with rule and verify it immediately
    std::vector<std::string> in_str;
    std::string line;
    const std::regex sep(" |-");
    while (std::getline(in, line)) {
        auto it = std::sregex_token_iterator(line.begin(), line.end(), sep, -1);
        auto low = std::stoi(*it++);
        auto high = std::stoi(*it++);
        auto c = std::string((*it++))[0];
        auto password = *it;
        valid_passwords += check_password(low, high, c, password);
    }

    std::cout << "Number of valid passwords: " << valid_passwords << std::endl;

    return 0;
}
