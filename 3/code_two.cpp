//
// Advent of Code 2020
//       Day 3
//
// © Ralph Ganszky
//

#include <filesystem>
#include <fstream>
#include <iostream>
#include <numeric>
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

    auto algorithms = {std::make_pair(1, 1), std::make_pair(3, 1), std::make_pair(5, 1),
                       std::make_pair(7, 1), std::make_pair(1, 2)};
    std::vector<int64_t> trees;
    for (auto& algorithm : algorithms) {
        trees.push_back(walk_maze(algorithm, maze));
        std::cout << "Found " << trees.back() << " trees for (" << std::get<0>(algorithm)
                  << ", " << std::get<1>(algorithm) << ")\n";
    }

    std::cout << "Result "
              << std::accumulate(trees.begin(), trees.end(), 1LL,
                                 [&](int64_t a, int64_t b) -> int64_t { return a * b; })
              << std::endl;

    return 0;
}
