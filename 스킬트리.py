#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

//
int solution(char* skill, char* st[], size_t skill_trees_len) {
    int answer = 0;
    int skills[26];
    for(int i = 0; i < 26; i++) skills[i] = 0;
    int cnt = 1;
    for(int i = 0; skill[i] != NULL; i++) {
        skills[skill[i] - 'A'] = cnt++;
    }
    for(int i = 0; i < skill_trees_len; i++) {
        cnt = 1; bool flag = true;
        for(int j = 0; st[i][j] != NULL; j++) {
           if(!skills[st[i][j] - 'A']) continue;
           if(skills[st[i][j] -'A'] == cnt) cnt++;
            else {flag = false; break;}
        }
        if(flag) answer++;
    }
    return answer;
}
