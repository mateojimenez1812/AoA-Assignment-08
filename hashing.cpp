/*
 * Analysis of Algorithms - Assignment 08
 * Exercise 4: Hash table with closed hashing (open addressing, linear probing)
 * No dictionaries or containers are used: only plain arrays.
 * <iostream> is used only to print the results.
 */
#include <iostream>

const int TABLE_SIZE = 13;      // a prime number works best
const int MAX_KEY_LEN = 32;

enum CellState { EMPTY, OCCUPIED, DELETED };

struct Cell {
    char key[MAX_KEY_LEN];
    CellState state;
};

// ---- small helpers (instead of library functions) ----
int myStrlen(const char* s) {
    int n = 0;
    while (s[n] != '\0') n++;
    return n;
}

bool myStrEqual(const char* a, const char* b) {
    int i = 0;
    while (a[i] != '\0' && b[i] != '\0') {
        if (a[i] != b[i]) return false;
        i++;
    }
    return a[i] == b[i];
}

void myStrCopy(char* dest, const char* src) {
    int i = 0;
    while (src[i] != '\0' && i < MAX_KEY_LEN - 1) {
        dest[i] = src[i];
        i++;
    }
    dest[i] = '\0';
}

// ---- hash table ----
class HashTable {
private:
    Cell table[TABLE_SIZE];
    int count;
    int lastProbes;   // number of cells visited in the last operation

    // Hash function: h(K) = (sum of the letter positions) mod m, with A = 1, ..., Z = 26
    int hash(const char* key) const {
        int sum = 0;
        for (int i = 0; key[i] != '\0'; i++) {
            char c = key[i];
            if (c >= 'a' && c <= 'z') c = c - 'a' + 'A';
            if (c >= 'A' && c <= 'Z') sum += c - 'A' + 1;
        }
        return sum % TABLE_SIZE;
    }

public:
    HashTable() : count(0), lastProbes(0) {
        for (int i = 0; i < TABLE_SIZE; i++) {
            table[i].state = EMPTY;
            table[i].key[0] = '\0';
        }
    }

    int getHash(const char* key) const { return hash(key); }
    int getLastProbes() const { return lastProbes; }
    int size() const { return count; }

    // Insert: if the home cell is taken, try the next cell (linear probing)
    bool insert(const char* key) {
        if (contains(key)) return false;              // no duplicates
        if (count == TABLE_SIZE) return false;        // table full
        int index = hash(key);
        lastProbes = 1;
        while (table[index].state == OCCUPIED) {
            index = (index + 1) % TABLE_SIZE;
            lastProbes++;
        }
        myStrCopy(table[index].key, key);
        table[index].state = OCCUPIED;
        count++;
        return true;
    }

    // Search: follow the same probe sequence until the key or an EMPTY cell is found
    int search(const char* key) {
        int index = hash(key);
        lastProbes = 0;
        for (int i = 0; i < TABLE_SIZE; i++) {
            lastProbes++;
            if (table[index].state == EMPTY) return -1;
            if (table[index].state == OCCUPIED && myStrEqual(table[index].key, key)) return index;
            index = (index + 1) % TABLE_SIZE;
        }
        return -1;
    }

    bool contains(const char* key) {
        int saved = lastProbes;
        bool found = search(key) != -1;
        lastProbes = saved;
        return found;
    }

    // Delete: mark the cell as DELETED (lazy deletion) so later searches keep probing
    bool remove(const char* key) {
        int index = search(key);
        if (index == -1) return false;
        table[index].state = DELETED;
        count--;
        return true;
    }

    void print() const {
        std::cout << "   index | key\n";
        for (int i = 0; i < TABLE_SIZE; i++) {
            std::cout << "   " << (i < 10 ? " " : "") << i << "    | ";
            if (table[i].state == OCCUPIED) std::cout << table[i].key;
            else if (table[i].state == DELETED) std::cout << "(deleted)";
            else std::cout << "-";
            std::cout << "\n";
        }
    }
};

int main() {
    std::cout << "EXERCISE 4: Hashing with closed hashing (linear probing)\n";
    std::cout << "Table size m = " << TABLE_SIZE
              << ",  h(K) = (sum of letter positions, A=1..Z=26) mod m\n\n";

    const char* words[] = {"A", "FOOL", "AND", "HIS", "MONEY", "ARE", "SOON", "PARTED"};
    int n = 8;

    std::cout << "Inserting keys:\n";
    HashTable ht;
    for (int i = 0; i < n; i++) {
        int h = ht.getHash(words[i]);
        ht.insert(words[i]);
        int pos = ht.search(words[i]);
        std::cout << "   " << words[i];
        for (int s = myStrlen(words[i]); s < 8; s++) std::cout << " ";
        std::cout << "h = " << (h < 10 ? " " : "") << h << "  -> stored at index "
                  << pos;
        if (pos != h) std::cout << "   (collision, moved by linear probing)";
        std::cout << "\n";
    }

    std::cout << "\nHash table:\n";
    ht.print();

    std::cout << "\nSearching keys:\n";
    const char* queries[] = {"MONEY", "PARTED", "KID", "SOON"};
    for (int i = 0; i < 4; i++) {
        int pos = ht.search(queries[i]);
        std::cout << "   search(" << queries[i] << ") -> ";
        if (pos == -1) std::cout << "not found";
        else std::cout << "found at index " << pos;
        std::cout << "  [" << ht.getLastProbes() << " probe(s)]\n";
    }

    std::cout << "\nDeleting \"ARE\" and searching again:\n";
    ht.remove("ARE");
    int pos = ht.search("SOON");
    std::cout << "   search(SOON) -> found at index " << pos
              << "  (still found thanks to the DELETED mark)\n";
    pos = ht.search("ARE");
    std::cout << "   search(ARE)  -> " << (pos == -1 ? "not found" : "found") << "\n";

    std::cout << "\nFinal table (" << ht.size() << " keys):\n";
    ht.print();
    return 0;
}
