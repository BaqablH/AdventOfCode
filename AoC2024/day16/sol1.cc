#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <limits>
#include <queue>
#include <tuple>
#include <vector>

struct State {
    int x, y, dir, cost;
};

typedef std::pair<int, int> Move;

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

    std::vector<std::vector<std::vector<int>>> dist(n, std::vector<std::vector<int>>(m, std::vector<int>(N_DIRS, std::numeric_limits<int>::max())));

    std::vector<std::queue<State>> Q(1);
    dist[n - 2][1][0] = 0;
    Q.front().push({n - 2, 1, 0, 0});

    // Decide whether to add to the queue
    auto try_add_elem = [&](int level, State S) -> void {
        if (map[S.x][S.y] == '#')
            return;

        if (S.cost < dist[S.x][S.y][S.dir]) {
            dist[S.x][S.y][S.dir] = S.cost;
            if (Q.size() == level)
                Q.push_back({});
            assert(S.cost % 1000 < 900);
            Q[level].push(S);
        }
    };

    // BFS
    for (int level = 0; level != Q.size(); ++level) {
        while (!Q[level].empty()) {
            State S = Q[level].front();
            Q[level].pop();

            // Add rotations
            for (int i = 0; i < N_DIRS; ++i) {
                if ((S.dir & i & 1) == 0) {
                    try_add_elem(level + 1, State{S.x, S.y, i, S.cost + PENALTY_TURN});
                }
            }

            // Add state after moving forward
            const auto [dx, dy] = dirs[S.dir];
            try_add_elem(level, State{S.x + dx, S.y + dy, S.dir, S.cost + PENALTY_FORWARD});
        }
    }

    // Print answer
    std::cout << *std::min_element(dist[1][m - 2].begin(), dist[1][m - 2].end()) << std::endl;
}