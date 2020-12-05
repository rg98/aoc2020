//
// Advent of Code 2020
//       Day 5
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

// Walk the maze
//

int walk_maze(std::tuple<int, int> algorithm, const std::vector<std::string>& maze) {
    auto trees{0};
    auto right = std::get<0>(algorithm);
    auto down = std::get<1>(algorithm);
    auto pos = std::make_pair(0, 0);
    auto maze_width = maze[0].size();
    for (auto y{0}; y < maze.size(); y += down) {
        pos = std::make_pair(std::get<0>(pos) + right, std::get<1>(pos) + down);
        if (maze[std::get<1>(pos)][std::get<0>(pos) % maze_width] == '#')
            trees++;
    }
    return trees;
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
    std::vector<std::string> maze;
    std::string line;
    while (std::getline(in, line)) {
        maze.push_back(line);
    }

    std::cout << "Found " << walk_maze(std::make_tuple(3, 1), maze) << " trees." << std::endl;

    return 0;
}
