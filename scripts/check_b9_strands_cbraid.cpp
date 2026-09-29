// Exact standard-parabolic membership using deletion and CBraid normal forms.
// CBraid dependency: jeanluct/cbraid, pinned separately in the run metadata.
// Input lines: record-id, ambient rank, word length, signed Artin generators.
// Output JSON lines: smallest standard strand number and a word there.
#include "braiding.h"
#include <cstdlib>
#include <iostream>
#include <list>
#include <vector>

using Word = std::vector<int>;

CBraid::ArtinBraid braid(const Word& w, int n) {
    std::list<CBraid::sint16> letters;
    for (int x : w) {
        if (x == 0 || std::abs(x) >= n) std::abort();
        letters.push_back(x);
    }
    auto b = Braiding::WordToBraid(letters, n);
    b.MakeLCF();
    return b;
}

bool delete_last(const Word& w, int n, Word& out) {
    int position = n;
    out.clear();
    for (int x : w) {
        int i = std::abs(x);
        if (position == i) position = i + 1;
        else if (position == i + 1) position = i;
        else {
            int y = i - (position < i ? 1 : 0);
            out.push_back(x > 0 ? y : -y);
        }
    }
    return position == n;
}

int main() {
    int id, n, length;
    while (std::cin >> id >> n >> length) {
        if (n < 2 || n > 20 || length < 0 || length > 100000) return 2;
        Word w(length);
        for (int& x : w) if (!(std::cin >> x)) return 3;
        const int initial = n;
        Word smaller;
        while (n > 1) {
            if (!delete_last(w, n, smaller)) break;
            auto b = braid(w, n);
            auto d = braid(smaller, n);
            if (!(b == d)) break;
            w = smaller;
            --n;
        }
        std::cout << "{\"index\":" << id << ",\"ambient_rank\":" << initial
                  << ",\"minimum_strands\":" << n << ",\"word\":[";
        for (size_t i = 0; i < w.size(); ++i) {
            if (i) std::cout << ',';
            std::cout << w[i];
        }
        std::cout << "]}" << std::endl;
    }
    return 0;
}
