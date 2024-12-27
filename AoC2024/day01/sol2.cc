#include <iostream>
#include <vector>
#include <unordered_map>
#include <utility> // for std::pair
#include <ranges>
#include <range/v3/all.hpp>
#include <range/v3/numeric/accumulate.hpp>

struct Line : std::pair<int, int> {
    friend std::istream& operator>>(std::istream& is, Line& l) {
        return is >> l.first >> l.second;
    }
};

int main() {
    // Use ranges to read input pairs directly
    auto input = ranges::istream_range<Line>(std::cin)
               | ranges::to<std::vector<Line>>(); 
    
    // Counting occurrences of the second integer in each pair using ranges
    std::unordered_map<int, int> r_counter;
    for (const auto& [_, r] : input) ++r_counter[r];

    // Calculating the weighted sum using ranges
    int weighted_sum = ranges::accumulate(
        input
            | std::views::transform([](const Line& l) { return l.first; })
            | std::views::transform([&r_counter](int x) { return x * r_counter[x]; })
        ,
        0  // Initial value
    );
    
    // Output the result
    std::cout << weighted_sum << '\n';
}