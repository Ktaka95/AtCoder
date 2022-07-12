#include <bits/stdc++.h>
using namespace std;

int main() {
	int N, M;
	cin >> N >> M;

	vector<vector<char>> list(N, vector<char>(N, '-'));
	for (int i = 0; i < M; i++) {
		int w, l;
		cin >> w >> l;
		w--;
		l--;
		list.at(w).at(l) = 'o';
		list.at(l).at(w) = 'x';
	}
	
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cout << list.at(i).at(j);
			if (j != N - 1) {
				cout << ' ';
			}
			else {
				cout << endl;
			}
		}
	}
}

