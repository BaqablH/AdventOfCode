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
    
    // A lambda to sort and return the member values
    auto sorted_by_nth = [&input = std::as_const(input)](int Line::* member) {
        return input
            | std::views::transform([member](const Line& l) { return l.*member; })
            | ranges::to<std::vector<int>>()
            | ranges::actions::sort;
    };

    // Sort both the first and second members of the Line objects
    auto sorted_first = sorted_by_nth(&Line::first);
    auto sorted_second = sorted_by_nth(&Line::second);

    // Compute the sum of the absolute differences between the sorted pairs
    int sum = ranges::accumulate(
        ranges::view::zip(sorted_first, sorted_second)
        | std::views::transform([](const auto& pair) { return std::abs(pair.first - pair.second); }),
        0  // Initial value for accumulation
    );

    // Output the result
    std::cout << sum << '\n';
}
