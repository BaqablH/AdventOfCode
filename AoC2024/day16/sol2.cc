#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <limits>
#include <queue>
#include <set>
#include <tuple>
#include <vector>

struct State {
    int x, y, dir, cost;
    std::vector<const State*> parents{};
};

typedef std::pair<int, int> Move;
typedef std::pair<int, int> Position;

constexpr int PENALTY_FORWARD = 1;
constexpr int PENALTY_TURN = 1000;
constexpr int N_DIRS = 4;

constexpr std::array<Move, N_DIRS> dirs{{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}};

int main() {
    std::vector<std::string> map;
    std::string s;
    while (std::cin >> s)
        map.push_back(s);
    int n = map.size();
    int m = map.front().size();

    std::vector<std::vector<std::vector<State>>> states(n, std::vector<std::vector<State>>(m, std::vector<State>(N_DIRS, {
        .cost = std::numeric_limits<int>::max()})));

    std::vector<std::queue<const State*>> Q(1);
    states[n - 2][1][0] = {.x = n - 2, .y = 1, .dir = 0, .cost = 0};
    Q.front().push(&states[n - 2][1][0]);

    // Decide whether to add to the queue
    auto try_add_elem = [&](int level, State S, const State* parent) -> void {
        if (map[S.x][S.y] == '#')
            return;

        if (S.cost < states[S.x][S.y][S.dir].cost) {
            states[S.x][S.y][S.dir] = S;
            if (Q.size() == level)
                Q.push_back({});
            assert(S.cost % 1000 < 900);
            Q[level].push(&states[S.x][S.y][S.dir]);
        }

        if (S.cost == states[S.x][S.y][S.dir].cost) {
            states[S.x][S.y][S.dir].parents.push_back(parent);
        }
    };

    // BFS
    for (int level = 0; level != Q.size(); ++level) {
        while (!Q[level].empty()) {
            const State* S = Q[level].front();
            Q[level].pop();

            // Add rotations
            for (int i = 0; i < N_DIRS; ++i) {
                if ((S->dir & i & 1) == 0) {
                    try_add_elem(level + 1, State{S->x, S->y, i, S->cost + PENALTY_TURN}, S);
                }
            }

            // Add state after moving forward
            const auto [dx, dy] = dirs[S->dir];
            try_add_elem(level, State{S->x + dx, S->y + dy, S->dir, S->cost + PENALTY_FORWARD}, S);
        }
    }

    // Print answer
    const auto& final_cell = states[1][m - 2];
    auto shortest_full_path_cost{std::numeric_limits<int>::max()};
    for (const auto& last_cell_state : final_cell) {
        shortest_full_path_cost = std::min(shortest_full_path_cost, last_cell_state.cost);
    }

    std::set<const State*> visited_states;
    std::queue<const State*> finder;
    auto enqueue = [&](const State* s) {
        if (visited_states.insert(s).second) {
            finder.push(s);
        }
    };

    for (const auto& last_cell_state : final_cell) {
        if (last_cell_state.cost == shortest_full_path_cost) {
            enqueue(&last_cell_state);
        }
    }
    
    while (!finder.empty()) {
        const State* state = finder.front();
        finder.pop();

        for (const State* next : state->parents) {
            enqueue(next);
        } 
    }

    std::set<Position> answer_positions;
    for (const State* state : visited_states) {
        answer_positions.insert({state->x, state->y});
    }

    std::cout << answer_positions.size() << std::endl;
}