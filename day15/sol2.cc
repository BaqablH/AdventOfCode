#include <iostream>
#include <vector>
#include <utility>
#include <memory>
#include <array>
#include <algorithm>
#include <queue>
#include <exception>

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
    virtual void move(Direction) {};
    virtual int score() { return 0; };
    virtual void try_move(int, Direction) {
        throw std::runtime_error("try_move() not implemented");
    }
    bool is_box() { return c == '['; };
    bool is_obstacle() { return c == '#'; }
    int x, y;
    int last_enqueued;
    char c;
    Cell(int x, int y, char c) : x(x), y(y), c(c), last_enqueued(-1) {}
};

std::shared_ptr<Cell> factory_cell(int x, int y, char c);

struct Game {
    std::vector<std::vector<std::shared_ptr<Cell>>> map;

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

                if (s[j] == ']')
                    map.back().emplace_back(map.back().back());
                else
                    map.back().emplace_back(factory_cell(i, j, s[j]));

                if (s[j] == '@') robot = get(i, j);
            }
            if (all_obstacles && i > 0) break;
        }
    }

    void swap(int x, int y, int X, int Y) {
        bool change_values = (map[x][y]->x == x && map[x][y]->y);
        if (change_values) {
            std::swap(map[x][y]->x, map[X][Y]->x);
            std::swap(map[x][y]->y, map[X][Y]->y);
        }

        map[x][y].swap(map[X][Y]);
    }

    void swap(int x, int y, Direction d) {
        const auto [dx, dy] = moves[static_cast<int>(d)];
        if (d == Direction::RIGHT) {
            ++map[x][y]->y;
            map[x][y + 2]->y -= 2;
            map[x][y + 1].swap(map[x][y + 2]);
            map[x][y].swap(map[x][y + 1]);
        }
        else if (d == Direction::LEFT) {
            --map[x][y]->y;
            map[x][y - 1]->y += 2;
            std::swap(map[x][y - 1], map[x][y]);
            std::swap(map[x][y], map[x][y + 1]);
        }
        else {
            map[x][y]->x += dx;
            map[x + dx][y]->x -= dx;
            map[x + dx][y + 1]->x -= dx;
            std::swap(map[x][y], map[x + dx][y]);
            std::swap(map[x][y + 1], map[x + dx][y + 1]);
        }
    }

    Cell* get(int x, int y) {
        return map[x][y].get();
    }

    void print() {
        for (int i = 0; i < map.size(); ++i) {
            for (int j = 0; j < map[i].size(); ++j) {
                if (map[i][j]->x == i) {
                    if (map[i][j]->y == j) {
                        std::cerr << map[i][j]->c;
                    }
                    else if (map[i][j]->y == j - 1) {
                        std::cerr << ']';
                    }
                    else {
                        throw std::runtime_error("Fail");
                    }
                }
                else {
                    throw std::runtime_error("Fail");
                }
            }
            std::cerr << std::endl;
        }
    }

    Cell* robot = nullptr;
} G;

struct Empty : Cell {
    using Cell::Cell;
};


struct Movable : Cell {
    using Cell::Cell;
};

struct Robot : Movable {
    using Movable::Movable;

    void try_move(int round, Direction d) {
        const auto [dx, dy] = moves[static_cast<int>(d)];
        std::vector<Position> Q;
        Q.push_back({x, y});
        for (int queue_ptr = 0; queue_ptr < Q.size(); ++queue_ptr) {
            const auto [X, Y] = Q[queue_ptr];
            auto l = G.get(X + dx, Y + dy);
            auto r = G.get(X + dx, Y + 1 + dy);
            for (const auto& ptr : {l, r}) {
                // First iteration should not look at the second option
                if (queue_ptr == 0 && ptr != l) break;

                // Nothing to do if obstacle was found
                if (ptr->is_obstacle()) return;

                // Only take boxes into account
                if (!ptr->is_box()) continue;

                // Add elements in front
                if (ptr->last_enqueued < round) {
                    ptr->last_enqueued = round;
                    Q.push_back({ptr->x, ptr->y});
                }
            }
        }

        for (int queue_ptr = Q.size() - 1; queue_ptr >= 0; --queue_ptr) {
            auto [x, y] = Q[queue_ptr];
            G.get(x, y)->move(d);
        }
    }

    void move(Direction d) override final {
        auto [dx, dy] = moves[static_cast<int>(d)];
        G.swap(x, y, x + dx, y + dy);
    }
};

struct Box : Movable {
    using Movable::Movable;
    
    void move(Direction d) override final {
        G.swap(x, y, d);
    }

    int score() override final {
        return 100*x + y;
    }
};

struct Obstacle : Cell {
    using Cell::Cell;
};

std::shared_ptr<Cell> factory_cell(int x, int y, char c) {
    if (c == '.') return std::make_shared<Empty>(x, y, c);
    if (c == '#') return std::make_shared<Obstacle>(x, y, c);
    if (c == '@') return std::make_shared<Robot>(x, y, c);
    if (c == '[') return std::make_shared<Box>(x, y, c);
    return nullptr; // Should not get here
}

int main() {
    char c;
    for (int round = 0; std::cin >> c; ++round) {
        G.robot->try_move(round, get_direction(c));
    }

    std::cout << G.score()/2 << std::endl;
}