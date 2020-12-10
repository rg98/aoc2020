//
// Advent of Code 2020
//       Day 8
//
// © Ralph Ganszky
//

#include <filesystem>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

enum class Opcode : int { Nop, Acc, Jmp };

struct Instruction {
    Instruction(const Opcode& _op, int64_t _arg) : op(_op), arg(_arg) {}
    Opcode op;
    int64_t arg;
};

int64_t check(const std::vector<Instruction>& program) {
    int64_t acc{0LL};
    int32_t pc{0LL};
    std::vector<bool> check(program.size());
    while (true) {
        if (check[pc])
            return acc;
        check[pc] = true;
        if (program[pc].op == Opcode::Nop) {
            pc += 1;
        } else if (program[pc].op == Opcode::Acc) {
            acc += program[pc].arg;
            pc += 1;
        } else if (program[pc].op == Opcode::Jmp) {
            pc += program[pc].arg;
        }
    }
    throw std::runtime_error("Unexpected behavior in program check!");
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

    // Read program
    std::vector<Instruction> program;
    std::string line;
    while (std::getline(in, line)) {
        if (line.substr(0, 3).compare("nop") == 0)
            program.emplace_back(Instruction(Opcode::Nop, std::stoll(line.substr(4))));
        else if (line.substr(0, 3).compare("acc") == 0)
            program.emplace_back(Instruction(Opcode::Acc, std::stoll(line.substr(4))));
        else if (line.substr(0, 3).compare("jmp") == 0)
            program.emplace_back(Instruction(Opcode::Jmp, std::stoll(line.substr(4))));
        else
            throw std::runtime_error(std::string("Unknown instruction: ") + line);
    }

    // Run program
    std::cout << "accumulator: " << check(program) << '\n';

    return 0;
}
