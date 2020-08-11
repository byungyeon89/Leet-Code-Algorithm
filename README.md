# Leet-Code-Algorithm
리트코드(LeetCode) 사이트 알고리즘 소스코드

**[목차 바로가기](https://github.com/byungyeon89/Leet-Code-Algorithm/blob/master/chart.md)**

## 소스

https://leetcode.com/ 의 알고리즘 중 `Medium` 난이도에서 쉬운 순서대로 풀이

## 문제 추가 원칙

1. `master`에서 만든다.

2. 문제출처 url의 문제 고유 문자열을 이용하여 폴더를 만든다.

    ex) https://leetcode.com/problems/max-increase-to-keep-city-skyline/
         -> `max-increase-to-keep-city-skyline`
         
3. 문제 제목은 # 을 달아 제목으로 지정하고 나머지 내용들은 보기 편하게 작성한다.(코드라면 마크다운의 코드로, 들여쓰기 혹은 기호 등등 되도록 그대로)

## 문제 풀이 원칙

1. `본인이름/문제이름`으로 브랜치를 생성하여 그곳에서 작성한다.

2. `소스코드만`을 업로드한다.
    
    ex) java -> .java, c++ -> .cpp, js -> .js, 등과 같이 소스코드만을 올릴 것이며 **프로젝트폴더를 업로드 하지말아야 한다.**
    
3. 파일명은 `본인이름_문제이름.[확장자]` 로 한다.

4. `문제이름`은 camel convention을 따른다.

## PR 원칙

1. `본인이름/main`브랜치를 생성한다.

2. 문제 풀이를 완료한 브랜치를 `본인이름/main`으로 합친다. (git merge)

    example
    
    ```bash
    creco$ git checkout creaticoding/main
    creco$ git pull origin creaticoding/problem-example
    creco$ git push origin creaticoding/main
    ```

3. 저장소 메인 사이트로 접속 후 PR을 날린다. https://github.com/AlogorithmStudy/Leetcode

4. 미팅 때 코드리뷰를 진행한다.

5. **코드리뷰가 완료된 PR만을 Merge한다.**



참여자: 정석호, 김지훈, 박연지

문제리스트: https://leetcode.com/problemset/algorithms/?difficulty=Medium 에서 Acceptance 높은 순서대로
