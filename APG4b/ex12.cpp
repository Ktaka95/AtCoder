#include <bits/stdc++.h>
using namespace std;

int main() {
	string S;
	cin >> S;

	int n = 1;
	for (int i = 0; i < S.size(); i++) {
		if (S.at(i) == '+') {
			n++;
		}
		else if (S.at(i) == '-') {
			n--;
		}
	}
	cout << n << endl;
}
