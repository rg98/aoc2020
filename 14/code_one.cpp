//
// Advent of Code 2020
//       Day 14
//
// © Ralph Ganszky
//

#include <filesystem>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <tuple>
#include <vector>

std::tuple<int64_t, int64_t> decode_mask(const std::string& mask) {
    int64_t bit{0x800000000LL};
    int64_t and_mask{0x7fffffffffffffffLL}; // 0 bit removes bit
    int64_t or_mask{0LL};                   // 1 bit add bit
    for (auto c : mask.substr(7)) {
        switch (c) {
        case '0':
            and_mask ^= bit;
            break;
        case '1':
            or_mask |= bit;
            break;
        }
        bit >>= 1;
    }
    return std::make_tuple(and_mask, or_mask);
}

void update_mem(const std::string& cmd, std::tuple<int64_t, int64_t> mask,
                std::map<int64_t, int64_t>& mem) {
    std::size_t pos{4};
    int64_t addr{0};
    int64_t value{0};
    addr = std::stoll(cmd.substr(4), &pos);
    value = std::stoll(cmd.substr(8 + pos), &pos);
    value &= std::get<0>(mask);
    value |= std::get<1>(mask);
    mem[addr] = value;
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
    std::tuple<int64_t, int64_t> mask; // Mask for AND and OR (0) and (1)
    std::map<int64_t, int64_t> mem;
    std::string line;
    while (std::getline(in, line)) {
        if (line.substr(0, 5).compare("mask ") == 0) {
            mask = decode_mask(line);
        } else if (line.substr(0, 4).compare("mem[") == 0) {
            update_mem(line, mask, mem);
        } else
            throw std::runtime_error(std::string("Unknown input: ") + line);
    }

    auto sum = std::accumulate(mem.begin(), mem.end(), 0LL,
                               [&](int64_t a, auto& b) -> int64_t { return a + b.second; });
    std::cout << sum << '\n';

    return 0;
}
