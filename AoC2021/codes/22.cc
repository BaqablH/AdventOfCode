#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <set>
#include <sstream>
#include <vector>

// NOTE: Part 2 runs in around 3 mins with -O3. Compilation requires C++20
// Performance could be improved by storing all (i, j, k) tuples in an unordered_set,
// (x[i] is the i-th ordered x coordinate, same for y[j] and z[k])
// and iterating for last cuboid to first. Every time the cuboid contains the subcuboid defined
// by the tuple, add to the total sum if required and remove from the unordered set

struct Cuboid {
    int64_t x0, x1, y0, y1, z0, z1;
    bool active;

    // Read cuboid. Increment x1, y1, z1 as the extremes are also included
    Cuboid(std::string line) {
        std::string keyword;
        std::stringstream ss(line);
        ss >> keyword >> x0 >> x1 >> y0 >> y1 >> z0 >> z1;
        ++x1, ++y1, ++z1;
        active = (keyword == "on");
    }

    // Used to filter the minicubes
    bool is_mini() {
        constexpr int64_t MINI_THRESHOLD = 50;
        return std::max({std::abs(x0), std::abs(x1), std::abs(y0), std::abs(y1), std::abs(z0), std::abs(z1)}) <= MINI_THRESHOLD;
    }
};

// Return the volume of the first cuboid were the given input is completely included, only if it is active. Return 0 otherwise
uint64_t get_cube_score(std::vector<Cuboid>& cuboids, int64_t x0, int64_t x1, int64_t y0, int64_t y1, int64_t z0, int64_t z1) {
    for (const Cuboid& c : cuboids)
        if (c.x0 <= x0 && x1 <= c.x1 && c.y0 <= y0 && y1 <= c.y1 && c.z0 <= z0 && z1 <= c.z1)
            return (c.active ? (x1 - x0)*(y1 - y0)*(z1 - z0) : 0);
    return 0;
}

uint64_t solve(std::vector<Cuboid> cuboids) {
    // Store list of coordinate values for each direction 
    std::vector<std::set<int64_t>> coord_vecs_set(3);
    for (const Cuboid& cuboid : cuboids) {
        coord_vecs_set[0].insert({cuboid.x0, cuboid.x1});
        coord_vecs_set[1].insert({cuboid.y0, cuboid.y1});
        coord_vecs_set[2].insert({cuboid.z0, cuboid.z1});
    }

    // Turn them into an ordered vector
    std::vector<std::vector<int64_t>> coord_vecs(3);
    for (auto i{0u}; i < 3u; ++i)
        for (int64_t val : coord_vecs_set[i])
            coord_vecs[i].push_back(val);

    // Reverse cuboids for comodity (as the later ones overwrite the previous where they intersect)
    std::reverse(cuboids.begin(), cuboids.end());

    // For each cuboid made after breaking the 3D as given by the input, add the corresponding score
    uint64_t ans{0u};
    for (auto i{1u}; i < coord_vecs[0].size(); ++i) {
        std::cerr << i << std::endl;
        for (auto j{1u}; j < coord_vecs[1].size(); ++j)
            for (auto k{1u}; k < coord_vecs[2].size(); ++k)
                ans += get_cube_score(cuboids, coord_vecs[0][i - 1], coord_vecs[0][i], coord_vecs[1][j - 1], coord_vecs[1][j], coord_vecs[2][k - 1], coord_vecs[2][k]);
    }

    return ans;
}

int main() {
    // Read cuboids
    std::ifstream ifs{"../inputs/22.inp"};
    std::vector<Cuboid> cuboids;
    std::string line;
    while (std::getline(ifs, line)) {
        for (char& c : line)
            if (std::string("0123456789fno-").find(c) == std::string::npos)
                c = ' ';
        cuboids.emplace_back(line);
    }

    // Filter minicuboids
    auto minicuboids = cuboids;
    std::erase_if(minicuboids, [](Cuboid& cuboid) { return !cuboid.is_mini(); });

    // Print solution
    std::cout << solve(minicuboids) << std::endl;
    std::cout << solve(cuboids) << std::endl;
}
