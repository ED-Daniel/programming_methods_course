#include <vector>
#include <list>
#include <iostream>
#include <string>

// Интерфейс реализации
class SetImpl {
public:
    virtual ~SetImpl() = default;
    virtual void add(int value) = 0;
    virtual void remove(int value) = 0;
    virtual bool contains(int value) const = 0;
    virtual size_t size() const = 0;
    virtual int get(size_t index) const = 0; 
    virtual std::string name() const = 0;
};

// Реализация через массив
class ArraySet : public SetImpl {
    int data[100];
    size_t currentSize = 0;

public:
    void add(int value) override {
        if (currentSize < 100 && !contains(value)) {
            data[currentSize++] = value;
        }
    }

    void remove(int value) override {
        for (size_t i = 0; i < currentSize; ++i) {
            if (data[i] == value) {
                data[i] = data[--currentSize];
                return;
            }
        }
    }

    bool contains(int value) const override {
        for (size_t i = 0; i < currentSize; ++i) {
            if (data[i] == value) {
                return true;
            }
        }
        return false;
    }

    size_t size() const override {
        return currentSize;
    }

    int get(size_t index) const override {
        if (index < currentSize) {
            return data[index];
        }
        throw std::out_of_range("Index out of range");
    }

    std::string name() const override {
        return "Array Implementation";
    }
};

// Реализация через std::vector
class VectorSet : public SetImpl {
    std::vector<int> data;

public:
    void add(int value) override {
        if (!contains(value)) {
            data.push_back(value);
        }
    }

    void remove(int value) override {
        auto it = std::find(data.begin(), data.end(), value);
        if (it != data.end()) {
            data.erase(it);
        }
    }

    bool contains(int value) const override {
        return std::find(data.begin(), data.end(), value) != data.end();
    }

    size_t size() const override {
        return data.size();
    }

    int get(size_t index) const override {
        if (index < data.size()) {
            return data[index];
        }
        throw std::out_of_range("Index out of range");
    }

    std::string name() const override {
        return "Vector Implementation";
    }
};

// Реализация через std::list
class ListSet : public SetImpl {
    std::list<int> data;

public:
    void add(int value) override {
        if (!contains(value)) {
            data.push_back(value);
        }
    }

    void remove(int value) override {
        data.remove(value);
    }

    bool contains(int value) const override {
        return std::find(data.begin(), data.end(), value) != data.end();
    }

    size_t size() const override {
        return data.size();
    }

    int get(size_t index) const override {
        if (index >= data.size()) {
            throw std::out_of_range("Index out of range");
        }
        auto it = data.begin();
        std::advance(it, index);
        return *it;
    }

    std::string name() const override {
        return "List Implementation";
    }
};

class Set {
    SetImpl* impl;

    void switchImpl(int element) {
        size_t currentSize = impl->size();
        SetImpl* newImpl = nullptr;

        if (currentSize + element <= 100) {
            newImpl = new ArraySet();
        } else if (currentSize + element <= 1000) {
            newImpl = new VectorSet();
        } else {
            newImpl = new ListSet();
        }

        // Перенос данных
        for (size_t i = 0; i < currentSize; ++i) {
            newImpl->add(impl->get(i));
        }

        delete impl;
        impl = newImpl;
    }

public:
    Set() : impl(new ArraySet()) {}

    ~Set() {
        delete impl;
    }

    void add(int value) {
        impl->add(value);
        switchImpl(1);
    }

    void remove(int value) {
        impl->remove(value);
        switchImpl(-1);
    }

    bool contains(int value) const {
        return impl->contains(value);
    }

    size_t size() const {
        return impl->size();
    }

    std::string name() const {
        return impl->name();
    }
};

int main() {
    Set mySet;
    
    for (int i = 0; i < 150; ++i) {
        mySet.add(i);
    }

    std::cout << "Set contains 50: " << mySet.contains(50) << std::endl;
    std::cout << "Set size: " << mySet.size() << std::endl;
    std::cout << "Set implementation: " << mySet.name() << std::endl;

    mySet.remove(50);
    std::cout << "Set contains 50: " << mySet.contains(50) << std::endl;

    for (int i = 51; i < 120; ++i) {
        mySet.remove(i);
    }

    std::cout << "Set size: " << mySet.size() << std::endl;
    std::cout << "Set implementation: " << mySet.name() << std::endl;

    return 0;
}
