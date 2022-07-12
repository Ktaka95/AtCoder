#include <bits/stdc++.h>
using namespace std;

int main() {
	int x, a, b;
	cin >> x >> a >> b;

	int one, two, three, four;

	one = x + 1;
	two = one * (a + b);
	three = two * two;
	four = three - 1;

	cout << one << endl;
	cout << two << endl;
	cout << three << endl;
	cout << four << endl;
}
