#include <iostream>
#include <vector>
#include <utility>
#include <memory>
#include <array>
#include <algorithm>

enum class Direction { RIGHT = 0, UP = 1, LEFT = 2, DOWN = 3};
typedef std::pair<int, int> Move;
typedef std::pair<int, int> Position;
constexpr std::array<Move, 4> moves{{{0, 1}, {-1, 0}, {0, -1}, {1, 0}}};

constexpr Direction get_direction(char c) {
    switch(c) {
        case '>': return Direction::RIGHT;
        case '^': return Direction::UP;
        case '<': return Direction::LEFT;
        case 'v':
        default: // Should not default
            return Direction::DOWN;
    }
}

struct Cell {
    virtual bool move(Direction) = 0;
    virtual bool is_box() { return false; };
    virtual int score() { return 0; };
    int x, y;
    Cell(int x, int y) : x(x), y(y) {}
};

std::unique_ptr<Cell> factory_cell(int x, int y, char c);

struct Game {
    std::vector<std::vector<std::unique_ptr<Cell>>> map;

    Game() { read(); }

    int score() {
        int sc = 0;
        for (const auto& row : map) for (const auto& cell : row) sc += cell->score();
        return sc;
    }

    void read() {
        std::string s;
        for (int i = 0; std::cin >> s; ++i) {
            map.push_back({});
            bool all_obstacles = true;
            for (int j = 0; j < s.size(); ++j) {
                all_obstacles &= (s[j] == '#');

                map.back().emplace_back(factory_cell(i, j, s[j]));
                if (s[j] == '@') robot = get(i, j);
            }
            if (all_obstacles && i > 0) break;
        }
    }

    void swap(int x, int y, int X, int Y) {
        std::swap(map[x][y]->x, map[X][Y]->x);
        std::swap(map[x][y]->y, map[X][Y]->y);
        map[x][y].swap(map[X][Y]);
    }

    Cell* get(int x, int y) {
        return map[x][y].get();
    }

    Cell* robot = nullptr;
} G;

struct Empty : Cell {
    using Cell::Cell;

    bool move(Direction) override final {
        return true;
    }
};


struct Movable : Cell {
    using Cell::Cell;

    bool move(Direction d) override final {
        auto [dx, dy] = moves[static_cast<int>(d)];
        bool retval = G.get(x + dx, y + dy)->move(d);
        if (retval) {
            G.swap(x, y, x + dx, y + dy);
        }

        return retval;
    }
};

struct Robot : Movable {
    using Movable::Movable;
};

struct Box : Movable {
    using Movable::Movable;
    
    virtual bool is_box() override final { return true; }

    int score() override final {
        return 100*x + y;
    }
};

struct Obstacle : Cell {
    using Cell::Cell;

    bool move(Direction) override final {
        return false;
    }
};

std::unique_ptr<Cell> factory_cell(int x, int y, char c) {
    if (c == '.') return std::make_unique<Empty>(x, y);
    if (c == '#') return std::make_unique<Obstacle>(x, y);
    if (c == '@') return std::make_unique<Robot>(x, y);
    if (c == 'O') return std::make_unique<Box>(x, y);
    return nullptr; // Should not get here
}

int main() {
    char c;
    while (std::cin >> c) {
        G.robot->move(get_direction(c));
    }

    std::cout << G.score() << std::endl;
}