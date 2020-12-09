//
// Advent of Code 2020
//       Day 7
//
// © Ralph Ganszky
//

#include <filesystem>
#include <fstream>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <regex>
#include <string>
#include <tuple>
#include <vector>

// Color
//

class Color {
  public:
    Color(const std::string& name) : _name(name) {}
    const std::string& name() const { return _name; }

  private:
    std::string _name;
};

bool operator==(Color lhr, const Color rhr) { return lhr.name().compare(rhr.name()) == 0; }
bool operator<(Color lhr, const Color rhr) { return lhr.name().compare(rhr.name()) < 0; }

std::ostream& operator<<(std::ostream& os, const Color& color) {
    os << color.name();
    return os;
}

// Edge
//

class Edge {
  public:
    Edge(const std::size_t from, const ssize_t bags, const std::size_t to)
        : _from(from), _to(to), _bags(bags) {}
    const auto from() const { return _from; }
    const auto to() const { return _to; }
    const auto bags() const { return _bags; }

  private:
    std::size_t _from;
    std::size_t _to;
    ssize_t _bags;
};

std::ostream& operator<<(std::ostream& os, const Edge& edge) {
    os << edge.from() << " contains " << edge.bags() << " of " << edge.to();
    return os;
}

// get_bags
//

std::vector<std::size_t> get_bags(std::size_t to_color,
                                  std::map<std::size_t, std::vector<Edge>>& edge_by_color) {
    std::vector<std::size_t> bags;
    for (auto& i : edge_by_color[to_color]) {
        if (i.bags() < 0) {
            if (std::find(bags.begin(), bags.end(), i.to()) == bags.end()) {
                bags.push_back(i.to());
                auto _bags = get_bags(i.to(), edge_by_color);
                bags.insert(bags.end(), _bags.begin(), _bags.end());
            }
        }
    }
    return bags;
}

inline std::size_t insert_when_not_found(const std::string& color_name,
                                         std::vector<Color>& nodes) {
    Color color(color_name);
    auto c_it = std::find(nodes.begin(), nodes.end(), color);
    if (c_it == nodes.end()) {
        nodes.push_back(color);
        return std::distance(nodes.begin(), std::prev(nodes.end()));
    }
    return std::distance(nodes.begin(), c_it);
}

inline std::size_t get_color_id(const Color& color, const std::vector<Color>& colors) {
    auto color_it = std::find(colors.begin(), colors.end(), color);
    if (color_it == colors.end())
        throw std::runtime_error(std::string("Can't find color ") + color.name() +
                                 " in colors!");
    return std::distance(colors.begin(), color_it);
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

    // Regular expression
    std::regex sep(" bags contain | bags?(,|\\.) ?");
    std::regex re_edge("(\\d+) (\\w+ \\w+)");

    // Nodes and edges
    std::vector<Color> nodes;
    std::vector<Edge> edges;

    // Read input file into nodes and edges
    std::string line;
    while (std::getline(in, line)) {
        auto it = std::sregex_token_iterator(line.begin(), line.end(), sep, -1);
        auto from_color = insert_when_not_found(*it, nodes);
        for (it++; it != std::sregex_token_iterator(); it++) {
            std::string s_edge(*it);
            auto e_it =
                std::sregex_token_iterator(s_edge.begin(), s_edge.end(), re_edge, {1, 2});
            if (e_it != std::sregex_token_iterator()) {
                auto n = std::stoi(*e_it++);
                auto to_color = insert_when_not_found(*e_it, nodes);
                edges.emplace_back(Edge(from_color, n, to_color));
            } else {
                if (s_edge.compare("no other") != 0)
                    throw std::runtime_error(std::string("Can't analyze edge - ") + s_edge +
                                             "!");
            }
        }
    }
    std::cout << "Found " << nodes.size() << " nodes with " << edges.size() << " edges.\n";

    // std::cout << "Colors:\n";
    // for (auto i{0}; i < nodes.size(); i++)
    //     std::cout << "\t" << i << ": " << nodes[i].name() << '\n';

    // Build graph in edge_by_color
    std::map<std::size_t, std::vector<Edge>> graph_edge_by_color;
    for (auto& edge : edges) {
        // std::cout << "mapping: " << nodes[edge.from()] << " -> " << edge.bags() << " of "
        //           << nodes[edge.to()] << '\n';
        if (graph_edge_by_color.find(edge.from()) == graph_edge_by_color.end()) {
            graph_edge_by_color[edge.from()] = std::vector<Edge>(1, edge);
        } else {
            graph_edge_by_color[edge.from()].push_back(edge);
        }
        if (graph_edge_by_color.find(edge.to()) == graph_edge_by_color.end()) {
            graph_edge_by_color[edge.to()] =
                std::vector<Edge>(1, Edge(edge.to(), -edge.bags(), edge.from()));
        } else {
            graph_edge_by_color[edge.to()].emplace_back(
                Edge(edge.to(), -edge.bags(), edge.from()));
        }
    }

    // std::cout << "Graph:\n";
    // for (auto c : graph_edge_by_color) {
    //     std::cout << "Color " << c.first << " " << nodes[c.first] << ":\n";
    //     for (auto e : c.second) {
    //         if (e.bags() > 0)
    //             std::cout << "\tEdge: " << nodes[e.from()] << " -> " << e.bags() << " of "
    //                       << nodes[e.to()] << '\n';
    //         else
    //             std::cout << "\tEdge: " << nodes[e.from()] << " <- " << e.bags() << " of "
    //                       << nodes[e.to()] << '\n';
    //     }
    // }

    auto bags = get_bags(get_color_id(Color("shiny gold"), nodes), graph_edge_by_color);

    // Remove duplicate colors
    std::sort(bags.begin(), bags.end());
    bags.erase(std::unique(bags.begin(), bags.end()), bags.end());

    std::cout << bags.size() << " can eventually contain at least one shiny gold bag!\n";

    return 0;
}
