
See:

```cpp
#include <iostream>
#include <array>
#include <vector>

template<int dim>
struct multi_index_t
{
	std::array<int, dim> size_array;
	template<typename ... Args>
	multi_index_t(Args&& ... args) : size_array(std::forward<Args>(args) ...) {}

	struct iterator
	{
		struct sentinel_t {};

		std::array<int, dim> index_array = {};
		std::array<int, dim> const& size_array;
		bool _end = false;

		iterator(std::array<int, dim> const& size_array) : size_array(size_array) {}

		auto& operator++()
		{
			for (int i = 0; i < dim; ++i)
			{
				if (index_array[i] < size_array[i] - 1)
				{
					++index_array[i];
					for (int j = 0; j < i; ++j)
					{
						index_array[j] = 0;
					}
					return *this;
				}
			}
			_end = true;
			return *this;
		}
		auto& operator*()
		{
			return index_array;
		}
		bool operator!=(sentinel_t) const
		{
			return !_end;
		}
	};

	auto begin() const
	{
		return iterator{ size_array };
	}
	auto end() const
	{
		return typename iterator::sentinel_t{};
	}
};

template<typename ... index_t>
auto multi_index(index_t&& ... index)
{
	static constexpr int size = sizeof ... (index_t);
	auto ar = std::array<int, size>{std::forward<index_t>(index) ...};
	return multi_index_t<size>(ar);
}

template<typename T>
auto multi_index_arr(std::vector<T>& index) {
	static constexpr int size = sizeof (index);
	return multi_index_t<size>(index);
}

using namespace std;

int main() {
	int n;
	cin >> n;
	vector<int> arr = { 1, 2, 3, 4 };

	for (auto m : multi_index_arr<int>(arr)) {
		for (int i = 0; i < n; ++i) {
			cout << m[i] << " ";
		}
		cout << endl;
	}

	system("pause");
	return 0;
}
```
