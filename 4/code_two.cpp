//
// Advent of Code 2020
//       Day 4
//
// © Ralph Ganszky
//

#include <filesystem>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <regex>
#include <string>
#include <vector>

// Check password
//

int check_password(const std::string& password, const std::vector<std::string>& keys) {
    const std::regex sep(":| ");
    auto it = std::sregex_token_iterator(password.begin(), password.end(), sep, -1);
    std::map<std::string, std::string> fields;
    it++;
    while (it != std::sregex_token_iterator()) {
        std::string key = *it++;
        std::string value = *it++;
        fields.emplace(std::make_pair(key, value));
    }
    std::regex byr("^\d{4}$");
    std::regex iyr("^\d{4}$");
    std::regex eyr("^\d{4}$");
    std::regex hgt("^\d{2,3}(cm|in)$");
    std::regex hcl("^#[0-9a-f]{6}$");
    std::regex ecl("^(amb|blu|brn|gry|grn|hzl|oth)$");
    std::regex pid("^\d{9}$");
    for (auto& check : keys) {
        if (fields.find(check) == fields.end())
            return 0;
    }
    return 1;
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
    std::vector<std::string> passwords = {""};
    std::string line;
    while (std::getline(in, line)) {
        if (line.size() > 0)
            passwords.back() += " " + line;
        else
            passwords.push_back("");
    }

    std::vector<std::string> keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"};
    auto count{0};
    for (auto& password : passwords) {
        count += check_password(password, keys);
    }

    std::cout << "Checked " << count << " valid passwords." << std::endl;

    return 0;
}
