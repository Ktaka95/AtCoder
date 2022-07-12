#include <bits/stdc++.h>
using namespace std;

int main() {
	int N, S;
	cin >> N >> S;

	vector<int> apple(N);
	vector<int> pineapple(N);
	for (int i = 0; i < N; i++) {
		cin >> apple.at(i);
	}
	for (int i = 0; i < N; i++) {
		cin >> pineapple.at(i);
	}

	int count = 0;
	for (int a : apple) {
		for (int p : pineapple) {
			if (a + p == S) {
				count++;
			}
		}
	}
	cout << count << endl;
}

