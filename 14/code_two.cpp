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

std::tuple<int64_t, int64_t, int64_t, int8_t> decode_mask(const std::string& mask) {
    int64_t bit{0x800000000LL};
    int64_t and_mask{0x7fffffffffffffffLL}; // 0 bit removes bit
    int64_t or_mask{0LL};                   // 1 bit add bit
    int64_t float_mask{0LL};                // 1 bit for floating bits
    int8_t float_bits{0};                   // number of floating bits
    for (auto c : mask.substr(7)) {
        switch (c) {
        case '0':
            break;
        case '1':
            or_mask |= bit;
            break;
        case 'X':
            float_mask |= bit;
            float_bits++;
            break;
        }
        bit >>= 1;
    }
    return std::make_tuple(and_mask, or_mask, float_mask, float_bits);
}

void update_mem(const std::string& cmd, std::tuple<int64_t, int64_t, int64_t, int8_t> mask,
                std::map<int64_t, int64_t>& mem) {
    std::size_t pos{4};
    int64_t addr{0};
    int64_t value{0};
    addr = std::stoll(cmd.substr(4), &pos);
    value = std::stoll(cmd.substr(8 + pos), &pos);
    addr &= std::get<0>(mask);  // Remove 0 bits
    addr |= std::get<1>(mask);  // Add 1 bits
    addr &= ~std::get<2>(mask); // Clear float bits
    auto n = (1LL << std::get<3>(mask));
    for (auto i{0}; i < n; i++) {
        auto f_addr = addr;
        auto f_bit{1LL};
        for (auto b{0}; b < std::get<3>(mask); b++) {
            while ((std::get<2>(mask) & f_bit) != f_bit)
                f_bit <<= 1;
            auto bit = (1LL << b);
            if (i & bit)
                f_addr |= f_bit;
            f_bit <<= 1;
        }
        std::bitset<36> b_addr(f_addr);
        std::bitset<36> b_value(value);
        mem[f_addr] = value;
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

    // Read schedule
    std::tuple<int64_t, int64_t, int64_t, int8_t>
        mask; // Mask for AND and OR (0) and (1) and float and number of float bits
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
