#include <bits/stdc++.h>
using namespace std;

int main() {
	vector<int> vec(5);

	for (int i = 0; i < 5; i++) {
		cin >> vec.at(i);
	}
	int old = vec.at(0);
	for (int i = 1; i < 5; i++) {
		if (old == vec.at(i)) {
			cout << "YES" << endl;
			return (0);
		}
		else {
			old = vec.at(i);
		}
	}
	cout << "NO" << endl;
}

