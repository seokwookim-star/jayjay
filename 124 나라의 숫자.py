#include <string>
#include <vector>

using namespace std;

string func(int, string);

string solution(int n) {
    string answer = "";
    if (n == 1) return to_string(1);
    if (n == 2) return to_string(2);
    if (n == 3) return to_string(4);
    return func(n, answer);
}

string func(int n, string answer) {
    int times, remainder;

    // n = 3 * times + remainder;
    times = n / 3;
    remainder = n % 3;

    if (remainder == 0) {
        times--;
        remainder = 3;
    }

    if (times == 1) answer.append(to_string(1));
    else if (times == 2) answer.append(to_string(2));
    else if (times == 3) answer.append(to_string(4));

    if (times > 3) {
        answer = func(times, answer);
    }

    if (remainder == 1) return answer.append(to_string(1));
    if (remainder == 2) return answer.append(to_string(2));
    if (remainder == 0) return answer.append(to_string(4));
}
